# -*- coding: utf-8 -*-
import sys
import importlib
import nltk
import string
import re
import random
import os.path
from time import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.naive_bayes import MultinomialNB
import joblib
from helpers import Files, TextFeaturesHelper, SiftFeatureHelper, OtherFeaturesHelper, FeaturesMerger, SVMHelper
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.model_selection import GridSearchCV, ShuffleSplit

class Data:
    def __init__(self, training_path, testing_path, n_classes):
        #importlib.reload(sys)  # had to deal with 'unicode' issues :/
        #sys.setdefaultencoding('utf8')
        self.n_classes = n_classes
        self.training_files = Files(training_path,n_classes)
        self.testing_files = Files(testing_path, n_classes)
        self.training_text_file_ids =[]
        self.training_text_texts = []
        self.training_text_classes = []
        self.training_text_tfidf = []
        self.testing_text_file_ids = []
        self.testing_text_texts = []
        self.testing_text_classes = []
        self.testing_text_tfidf = []
        self.testing_text_predicted = []
        self.testing_text_predicted_prob = []
        self.text_pre = None
        self.prepare_text_data()
        self.do_build_text_tfidf_transformer()
        self.do_training_tfidf_estimate()
        self.do_testing_tfidf_estimate()

        self.training_image_file_ids = []
        self.training_image_classes = []
        self.training_image_tfidf = []
        self.testing_image_file_ids = []
        self.testing_image_classes = []
        self.testing_image_tfidf = []
        self.testing_image_predicted = []
        self.testing_image_predicted_prob = []
        self.prepare_image_data()

    def prepare_text_data(self):
        text_helper = TextFeaturesHelper()
        text_helper.load_texts(self.training_files)
        self.training_text_texts = text_helper.texts
        self.training_text_classes = text_helper.classes
        self.training_text_file_ids = text_helper.file_ids
        self.training_text_tfidf = []
        text_helper.load_texts(self.testing_files)
        self.testing_text_file_ids = text_helper.file_ids
        self.testing_text_texts = text_helper.texts
        self.testing_text_classes = text_helper.classes
        self.testing_text_tfidf = []
        self.text_pre = None

    def do_build_text_tfidf_transformer(self):
        print("Building tf-idf transformer ... ")
        self.text_pre = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()),])
        self.text_pre.fit(self.training_text_texts)
        print("Done")

    def do_training_tfidf_estimate(self):
        self.training_text_tfidf = self.text_pre.transform(self.training_text_texts)

    def do_testing_tfidf_estimate(self):
        self.testing_text_tfidf = self.text_pre.transform(self.testing_text_texts)
        
        
    def prepare_image_data(self):
        image_helper = SiftFeatureHelper(img_width=300, n_clusters=400)
        image_helper_other = OtherFeaturesHelper(img_width=300,color=False, hog=False, gist=False, deep=True)
        print("Building image BOW vocab ... ")
        t0 = time()
        path = self.training_files.dataset_path + '/' + 'voc.pkl'
        if os.path.exists(path):
            voc = joblib.load(path)
            image_helper.set_voc(voc)
        else:
            image_helper.develop_vocabulary(self.training_files)
            joblib.dump(image_helper.voc, path)
        print("done in %0.3fs" % (time() - t0))

        print("Building training image features ... ")
        t0 = time()
        image_helper.build_BOW_features_classes(self.training_files)
        image_helper_other.build_features_classes(self.training_files)
        training_sift_classes = image_helper.classes
        training_sift_features = image_helper.features
        training_sift_file_ids = image_helper.file_ids
        training_other_classes = image_helper_other.classes
        training_other_features = image_helper_other.features
        training_other_file_ids = image_helper_other.file_ids
        training_merger = FeaturesMerger(training_sift_file_ids,training_sift_features,training_sift_classes,training_other_file_ids,training_other_features,training_other_classes)
        #training_merger = FeaturesMerger(training_sift_file_ids, training_sift_features, training_sift_classes,[], [], [])
        #training_merger = FeaturesMerger([], [], [],training_other_file_ids, training_other_features, training_other_classes)
        print("done in %0.3fs" % (time() - t0))
        self.training_image_classes = training_merger.classes
        self.training_image_file_ids = training_merger.paths
        self.training_image_tfidf = training_merger.features

        print("Building testing image features ... ")
        t0 = time()
        image_helper.build_BOW_features_classes(self.testing_files)
        image_helper_other.build_features_classes(self.testing_files)
        testing_sift_classes = image_helper.classes
        testing_sift_features = image_helper.features
        testing_sift_file_ids = image_helper.file_ids
        testing_other_classes = image_helper_other.classes
        testing_other_features = image_helper_other.features
        testing_other_file_ids = image_helper_other.file_ids
        testing_merger = FeaturesMerger(testing_sift_file_ids, testing_sift_features, testing_sift_classes, testing_other_file_ids, testing_other_features, testing_other_classes)
        #testing_merger = FeaturesMerger(testing_sift_file_ids, testing_sift_features, testing_sift_classes,[], [], [])
        #testing_merger = FeaturesMerger([], [], [],testing_other_file_ids, testing_other_features, testing_other_classes)
        self.testing_image_file_ids = testing_merger.paths
        self.testing_image_classes = testing_merger.classes
        self.testing_image_tfidf = testing_merger.features



class Text:
    def __init__(self, data):
        self.data = data

    def do_test_clasifiers(self):

        names = ["Nearest Neighbors", "Linear SVM", "RBF SVM",
                 "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
                 "Naive Bayes"]

        #names = ["Nearest Neighbors", "Linear SVM",
        #         "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
        #         "Naive Bayes"]

        #param_grid = {'C': [0.1, 0.5, 1, 5, 10, 100, 1e3, 5e3, 1e4, 5e4, 1e5],
        #                   'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1, 0.5, 1.0, 1.5, 2.0, 2.5], }

        param_grid = {'C': [0.025, 0.1, 1, 5 , 1e3, 5e3, 1e4, 5e4, 1e5],
                      'gamma': [0.0001, 0.01, 1.0, 1.5], }
        cv = ShuffleSplit()
        classifiers = [
            KNeighborsClassifier(3),
            #SVC(kernel="linear", C=0.025),
            GridSearchCV(SVC(kernel='linear', class_weight='balanced', probability=True), param_grid, cv=3),
            GridSearchCV(SVC(kernel='rbf', class_weight='balanced', probability=True), param_grid, cv=3),
            DecisionTreeClassifier(max_depth=5),
            RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
            MLPClassifier(alpha=1, max_iter=1000),
            AdaBoostClassifier(),
            MultinomialNB()]

        X_train = self.data.training_text_tfidf
        y_train = self.data.training_text_classes
        X_test = self.data.testing_text_tfidf
        y_test = self.data.testing_text_classes

        for name, clf in zip(names, classifiers):
            score = 0
            t0 = time()
            clf.fit(X_train, y_train)
            if name == "RBF SVM":
                score = clf.best_estimator_.score(X_test, y_test)
            else:
                score = clf.score(X_test, y_test)
            print( name + ":"+str(score)+":"+str(time() - t0))



class Image:
    def __init__(self, data):
        self.data = data

    def do_test_clasifiers(self):

        names = ["Nearest Neighbors", "Linear SVM", "RBF SVM",
                 "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
                 "Naive Bayes"]

        #names = ["Nearest Neighbors", "Linear SVM",
        #         "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
        #         "Naive Bayes"]

        param_grid = {'C': [0.025, 0.1, 1, 5 ], #, 1e3, 5e3, 1e4, 5e4, 1e5],
                           'gamma': [0.0001, 0.01, 1.0, 1.5], }
        cv = ShuffleSplit()
        classifiers = [
            KNeighborsClassifier(3),
            SVC(kernel="linear", C=0.025, probability=True),
            GridSearchCV(SVC(kernel='rbf', class_weight='balanced', probability=True), param_grid, cv=3),
            DecisionTreeClassifier(max_depth=5),
            RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
            MLPClassifier(alpha=1, max_iter=1000),
            AdaBoostClassifier(),
            GaussianNB()]

        X_train = self.data.training_image_tfidf
        y_train = self.data.training_image_classes
        X_test = self.data.testing_image_tfidf
        y_test = self.data.testing_image_classes

        for name, clf in zip(names, classifiers):
            score = 0
            pred_image = []
            t0 = time()
            clf.fit(X_train, y_train)
            if name == "RBF SVM":
                score = clf.best_estimator_.score(X_test, y_test)
                pred_image = clf.best_estimator_.predict_proba(X_test)
            else:
                score = clf.score(X_test, y_test)
                pred_image = clf.predict_proba(X_test)
            print(name + ":" + str(score) + ":" + str(time() - t0))

            #print pred_image
