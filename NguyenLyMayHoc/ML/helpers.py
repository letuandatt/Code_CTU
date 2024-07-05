import cv2
import nltk
import re
import string
import codecs
import json
import glob
import sys
from numpy import *
import numpy as np
from scipy.cluster.vq import *
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from time import time
import os.path
import imghdr
from skimage import feature
from skimage import exposure
from PIL import Image
import leargist
import matplotlib.pyplot as plt
from keras.applications.resnet50 import ResNet50, preprocess_input as pre_in_resnet
from keras.applications.inception_v3 import InceptionV3, preprocess_input as pre_in_inception
from keras.applications.xception import Xception, preprocess_input as pre_in_xception # TensorFlow ONLY
from keras.applications.vgg16 import VGG16, preprocess_input as pre_in_vgg16
from keras.applications.vgg19 import VGG19, preprocess_input as pre_in_vgg19
from keras.applications import imagenet_utils
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img


class Files:
    def __init__(self,dataset_path, n_classes):
        reload(sys)  # had to deal with 'unicode' issues :/
        sys.setdefaultencoding('utf8')
        self.dataset_path = dataset_path
        self.n_classes = n_classes
        self.dataset = []
        print('Indexing all the files in dataset...')
        self.do_index()
        print('done.')



    def find(self, lst, key, value):
        for i, dic in enumerate(lst):
            if dic[key] == value:
                return i
        return -111



    def generate_indices(self, class_id):

        for filepath in glob.glob(self.dataset_path+ "/"+str(class_id)+'/*.*'):
            filename = filepath[filepath.rfind("/") + 1:]
            fileid =  filename.split('.')[0].replace('descr_','').replace('img_','')
            fileext = filename.split('.')[-1]

            index =  self.find(self.dataset,'file_id',fileid)

            if index != -111:
                if fileext == 'txt':
                    self.dataset[index].update({'text_ext':'txt'})
                else:
                    self.dataset[index].update({'img_ext':fileext})
            else:
                if fileext == 'txt':
                    self.dataset.append({'class_id':class_id,'file_id':fileid,'text_ext':'txt'})
                else:
                    self.dataset.append({'class_id':class_id,'file_id':fileid,'img_ext':fileext})



    def generate_all_indices(self):
        for class_id in range(1,self.n_classes+1):
            self.generate_indices(class_id)



    def save_file(self, path, text):
        with codecs.open(path, 'wb', 'utf-8') as f:
            f.write(text)


    def load_file(self, path):
        if os.path.isfile(path):
            with codecs.open(path, 'rb', 'utf-8', errors='ignore') as f:
                text = f.read()
        else:
            text = ''
        return text


    def save_indices(self):
        path = self.dataset_path + '/indices.json'
        str_ = json.dumps(self.dataset,
                              indent=4, sort_keys=True,
                              separators=(',', ':'), ensure_ascii=False)
        self.save_file(path,str_)



    def load_indices(self):
        path = self.dataset_path + '/indices.json'
        text = self.load_file(path)
        self.dataset = json.loads(text)


    def do_index(self):
        file_path = self.dataset_path + '/indices.json'
        if os.path.isfile(file_path):
            self.load_indices()
        else:
            self.generate_all_indices()
            self.save_indices()


class TextFeaturesHelper:
    def __init__(self):
        self.texts = []
        self.classes = []
        self.file_ids = []

    def load_file(self, path):
        if os.path.isfile(path):
            with codecs.open(path, 'rb', 'utf-8', errors='ignore') as f:
                text = f.read()
        else:
            text = ''
        return text

    def clean(self, text):
        all_tokens = []
        sentences = nltk.sent_tokenize(text)
        for sentence in sentences:
            tokens = nltk.word_tokenize(sentence)
            tokens = [i.strip().lower() for i in tokens if i not in string.punctuation]

            for index, word in enumerate(tokens):
                tokens[index] = re.sub(r'[.|?|$|!|"|`|\'|" "|\xe2\x80\x9c|\xe2\x80\x9d]', r'', word)

            all_tokens = all_tokens + tokens

        return ' '.join(all_tokens)


    def load_texts(self, files):

        self.texts = []
        self.classes = []
        self.file_ids = []
        gen = [ x for x in files.dataset ]

        i = 0
        for rec in gen:
            class_id = rec['class_id']
            path = files.dataset_path+ "/"+str(class_id)+'/descr_'+rec['file_id']+'.'+rec['text_ext']
            #print('Loading '+path)
            self.texts.append(self.clean(self.load_file(path)))
            self.classes.append(class_id)
            self.file_ids.append(rec['file_id'])
            i += 1

        print('Total '+str(i)+' files loaded')




class ImageHelper:
    def __init__(self, width, model_name="resnet"):
        self.img_width = width
        self.sift_object = cv2.xfeatures2d.SIFT_create()
        # define a dictionary that maps model names to their classes
        # inside Keras
        self.MODELS = {
            "vgg16": VGG16,
            "vgg19": VGG19,
            "inception": InceptionV3,
            "xception": Xception,  # TensorFlow ONLY
            "resnet": ResNet50
        }
        # initialize the input image shape (224x224 pixels) along with
        # the pre-processing function (this might need to be changed
        # based on which model we use to classify our image)
        self.inputShape = (224, 224)
        self.preprocess = imagenet_utils.preprocess_input

        if model_name == "vgg16":
            self.preprocess = pre_in_vgg16
        if model_name == "vgg19":
            self.preprocess = pre_in_vgg19
        if model_name == "inception":
            self.preprocess = pre_in_inception
            self.inputShape = (299, 299)
        if model_name == "xception":
            self.preprocess = pre_in_xception
            self.inputShape = (299, 299)
        if model_name == "resnet":
            self.preprocess = pre_in_resnet

        # esnure a valid model name was supplied via command line argument
        if model_name not in self.MODELS.keys():
            raise AssertionError("The model_name argument should "
                                     "be a key in the `MODELS` dictionary")

        # load our the network weights from disk (NOTE: if this is the
        # first time you are running this script for a given network, the
        # weights will need to be downloaded first -- depending on which
        # network you are using, the weights can be 90-575MB, so be
        # patient; the weights will be cached and subsequent runs of this
        # script will be *much* faster)
        self.Network = self.MODELS[model_name]
        self.model = self.Network(weights="imagenet", include_top=False)


    def is_valid_image(self, path):
        if os.path.isfile(path):
            t = imghdr.what(path)
            if t is not None:
                if t != 'gif':
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def scale(self, image, width):
        if image.shape[1] > width:
            r = float(width)/float(image.shape[1])
            dim = (width,int(r*image.shape[0]))
            return cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
        else:
            return image


    def gray(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray


    def color_feature(self,fn):
        img = cv2.imread(fn)
        hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        hist = hist.flatten()
        return hist


    def sift_feature(self, fn):
        img = cv2.imread(fn)
        si = self.scale(img,self.img_width)
        gi = self.gray(si)
        return self.sift_object.detectAndCompute(gi, None)


    def hog_feature(self,fn, width, height):
        img = cv2.imread(fn)
        dim = (width,height)
        si = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
        gi = self.gray(si)
        return feature.hog(gi, orientations=9, pixels_per_cell=(8, 8),
                        cells_per_block=(1, 1),block_norm='L2-Hys')


    def visualize_hog_feature(self,fn):
        img = cv2.imread(fn)

        (hf, hi) = feature.hog(img, orientations=9, pixels_per_cell=(16, 16),
                        cells_per_block=(1, 1), visualize=True, multichannel=True)
        hogImage = exposure.rescale_intensity(hi, in_range=(0, 10))

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

        ax1.axis('off')
        ax1.imshow(img)
        ax1.set_title('Input image')

        # Rescale histogram for better display
        hog_image_rescaled = exposure.rescale_intensity(hogImage, in_range=(0, 15))

        ax2.axis('off')
        ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
        ax2.set_title('Histogram of Oriented Gradients')
        plt.show()


    def gist_feature(self, fn):
        im = Image.open(fn)
        return leargist.color_gist(im)


    def deep_feature(self, fn):

        # load the input image using the Keras helper utility while ensuring
        # the image is resized to `inputShape`, the required input dimensions
        # for the ImageNet pre-trained network
        image = load_img(fn, target_size=self.inputShape)
        image = img_to_array(image)

        # our input image is now represented as a NumPy array of shape
        # (inputShape[0], inputShape[1], 3) however we need to expand the
        # dimension by making the shape (1, inputShape[0], inputShape[1], 3)
        # so we can pass it through thenetwork
        image = np.expand_dims(image, axis=0)

        # pre-process the image using the appropriate function based on the
        # model that has been loaded (i.e., mean subtraction, scaling, etc.)
        image = self.preprocess(image)

        #now load the output of the NEXT-TO-TOP layer
        outputs = self.model.predict(image)
        features = outputs.flatten()
        return features




class SiftFeatureHelper:
    def __init__(self, img_width=300, n_clusters=400):
        self.img_width = img_width
        self.n_clusters = n_clusters
        self.imghp = ImageHelper(img_width)
        self.rng = random.RandomState(0)
        self.kmeans_obj = MiniBatchKMeans(n_clusters=self.n_clusters, random_state=self.rng, verbose=True)
        self.scale = None
        self.voc = None
        self.idf = None
        self.file_ids = []
        self.features = []
        self.classes = []


    def develop_vocabulary(self,files):
        print('Learning the dictionary... ')

        t0 = time()
        if self.voc is None:
            print self.kmeans_obj
            buff = []
            n_points = 0
            gen = [x for x in files.dataset]
            i = 0
            for rec in gen:

                path = files.dataset_path + "/" + str(rec['class_id']) + '/img_' + rec['file_id'] + '.'+rec['img_ext']
                print('Loading ' + path)
                i = i+1
                if self.imghp.is_valid_image(path):
                    kp, desc = self.imghp.sift_feature(path)
                    if len(kp) > 0:
                        #print img
                        n_points += len(kp)
                        buff.append(desc)
                if (i % 100 == 0 and i > 0) or (i == len(gen)-1):
                    descriptors = array(buff[0]) #stack all features for k-means
                    for j in arange(1,len(buff)):
                        descriptors = vstack((descriptors,buff[j]))
                    self.kmeans_obj.partial_fit(descriptors)
                    buff = []
                    n_points = 0
                    print('Partial fit of %4i out of %i'% (i, len(gen)))

        dt = time() - t0
        print('done in %.2fs.' % dt)
        self.voc = self.kmeans_obj.cluster_centers_
        print "Vocabulary Histogram Generated"


    def set_voc(self, voc):
        self.voc = voc


    def project(self,descriptors):
        """ Project descriptors on the vocabulary
            to create a histogram of words. """

        # histogram of image words
        imhist = zeros((self.n_clusters))
        words,distance = vq(descriptors,self.voc)
        for w in words:
            imhist[w] += 1

        return imhist

    def get_words(self,descriptors):
        """ Convert descriptors to words. """
        return vq(descriptors,self.voc)[0]


    def build_BOW_features_classes(self, files):
        self.file_ids = []
        self.features = []
        self.classes = []

        print('Extracting BOW features ...')

        if self.voc is None:
            print('done! No vocabulary to build BOW features!')
            return [None, None]
        else:
            imwords = []

            t0 = time()
            index = 0
            n_images = 0
            gen = [x for x in files.dataset]
            for rec in gen:
                path = files.dataset_path + "/" + str(rec['class_id']) + '/img_' + rec['file_id'] + '.' + rec['img_ext']
                #print('Loading ' + path)
                if self.imghp.is_valid_image(path):
                    kp, desc = self.imghp.sift_feature(path)
                    if len(kp) > 0:
                        n_images += 1
                        data = desc
                        imwords.append(self.project(data))
                        self.classes.append(rec['class_id'])
                        self.file_ids.append(rec['file_id'])
                if index % 100 == 0:
                    print('Getting BOW of %4i out of %i'% (index, len(gen)))
                index += 1
            dt = time() - t0
            nparray = array(self.standardize(imwords))
            nbr_occurences = sum((nparray > 0)*1 ,axis=0)
            self.idf = log((1.0*n_images) / (1.0*nbr_occurences+1))
            nparray = nparray*self.idf
            print('done in %.2fs.' % dt)
            self.features = nparray


    def standardize(self, histogram):
        self.scale = StandardScaler().fit(histogram)
        return self.scale.transform(histogram)


class OtherFeaturesHelper:

    def __init__(self, img_width=300, color=True, hog=True, gist=True, deep=True):
        self.img_width = img_width
        self.imghp = ImageHelper(img_width, model_name="resnet")

        self.color = color
        self.hog = hog
        self.gist = gist
        self.deep = deep

        self.file_ids = []
        self.features = []
        self.classes = []

    def build_features_classes(self, files):
        self.file_ids = []
        self.features = []
        self.classes = []
        print('Extracting other features ...')
        imwords = []
        t0 = time()
        index = 0
        n_images = 0
        gen = [x for x in files.dataset]
        for rec in gen:
            path = files.dataset_path + "/" + str(rec['class_id']) + '/img_' + rec['file_id'] + '.' + rec['img_ext']

            print(path)
            if self.imghp.is_valid_image(path):
                t1 = time()
                feats = []
                ok = 1
                if self.color == True:
                    colorf = self.imghp.color_feature(path)
                    if len(colorf > 0):
                        feats = concatenate((feats, colorf), axis=None)
                    else:
                        ok = 0
                if self.hog == True:
                    hogf = self.imghp.hog_feature(path, 80, 80)
                    if len(hogf > 0):
                        feats = concatenate((feats, hogf), axis=None)
                    else:
                        ok = 0
                if self.gist == True:
                    gistf = self.imghp.gist_feature(path)
                    if len(gistf > 0):
                        feats = concatenate((feats, gistf), axis=None)
                    else:
                        ok = 0
                if self.deep == True:
                    deepf = self.imghp.deep_feature(path)
                    if len(deepf > 0):
                        feats = concatenate((feats, deepf), axis=None)
                    else:
                        ok = 0

                if ok == 1:
                    n_images += 1
                    imwords.append(feats)
                    self.classes.append(rec['class_id'])
                    self.file_ids.append(rec['file_id'])
                print('Done in %f' % (time()-t1))

            if index % 10 == 0:
                print('Getting image features of %4i out of %i' % (index, len(gen)))
            index += 1

        dt = time() - t0
        nparr = array(self.standardize(imwords))
        print('done in %.2fs.' % dt)
        self.features = nparr

    def standardize(self, histogram):
        self.scale = StandardScaler().fit(histogram)
        return self.scale.transform(histogram)


class FeaturesMerger:
    def __init__(self, lpaths, lfeatures, lclasses, rpaths, rfeatures,rclasses):
        self.lpaths = lpaths
        self.lfeatures = lfeatures
        self.lclasses = lclasses
        self.rpaths = rpaths
        self.rfeatures = rfeatures
        self.rclasses = rclasses
        self.paths = []
        self.features = []
        self.classes = []
        self.merge()

    def merge(self):
        if len(self.lpaths)==0:
            self.paths=self.rpaths
            self.features=self.rfeatures
            self.classes = self.rclasses
        else:
            if len(self.rpaths)==0:
                self.paths = self.lpaths
                self.features = self.lfeatures
                self.classes = self.lclasses
            else:
                for i in range(0, len(self.lpaths)):
                    if self.lpaths[i] in self.rpaths:
                        idx = self.rpaths.index(self.lpaths[i])
                        self.paths.append(self.lpaths[i])
                        self.features.append(concatenate((self.lfeatures[i], self.rfeatures[idx]), axis=None))
                        self.classes.append(self.lclasses[i])





class SVMHelper:

    def __init__(self):
        self.param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
        self.clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced', probability=True), self.param_grid)

    def train(self, trainning_docs, training_classes):
        t0 = time()
        print("Fitting the classifier to the training set")
        self.clf = self.clf.fit(trainning_docs, training_classes)
        print("done in %0.3fs" % (time() - t0))
        print("Best estimator found by grid search:")
        print(self.clf.best_estimator_)

    def test(self, testing_docs):
        print("Predicting image class on the test set")
        t0 = time()
        y_pred = self.clf.best_estimator_.predict_proba(testing_docs)
        print("done in %0.3fs" % (time() - t0))
        return y_pred

