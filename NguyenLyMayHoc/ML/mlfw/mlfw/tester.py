import glob
import sys
import importlib
import codecs
import json
import nltk
import string
import re
import random
import os.path
from time import time
import joblib
from processors import Files


class Tester:
    def __init__(self,dataset_path, n_classes):
        importlib.reload(sys)  # had to deal with 'unicode' issues :/
        sys.setdefaultencoding('utf8')
        self.dataset_path = dataset_path
        self.n_classes = n_classes
        self.files = Files(dataset_path,n_classes)
        # header and footer html
        self.header = """
            <!doctype html>
            <head>
            <title>Ranked images by scores</title>
            </head>
            <body>
            <table>
            """
        self.footer = """
            </table>
            </body>
            </html>
            """


    def gen_ranked_docs_by_text(self,class_id):
        path = self.files.dataset_path+'/'+str(class_id)+'_ranked_texts.pkl'
        id_score_tuples = joblib.load(path)
        id_score_tuples= sorted(id_score_tuples, key=lambda row: row[1], reverse=True)   # sort by score
        body = '\n'
        for tup in id_score_tuples:
            index = self.files.find(self.files.dataset,'file_id',tup[0])
            if index >= 0:
                if 'img_ext' in self.files.dataset[index] and 'text_ext' in self.files.dataset[index]:
                    img_ext = self.files.dataset[index]['img_ext']
                    text_ext = self.files.dataset[index]['text_ext']
                    img_path = self.files.dataset_path+'/'+str(class_id)+'/'+tup[0]+'.'+img_ext
                    text_path = self.files.dataset_path+'/'+str(class_id)+'/'+tup[0]+'.'+text_ext
                    text = self.files.load_file(text_path)
                    body += "\t<tr>\n"
                    body += "\t\t<td><image src='"+img_path+"' width='300' /></td>"
                    body += "<td><p>"+text+"</p></td>"
                    body += "<td>"+str(tup[1])+"</td>\n"
                    body += "\t<tr>\n"

        html = self.header+body+self.footer
        path = self.files.dataset_path+'/'+str(class_id)+'_ranked_texts.html'
        self.files.save_file(path,html)


    def gen_ranked_docs_by_image(self,class_id):
        path = self.files.dataset_path+'/'+str(class_id)+'_ranked_images.pkl'
        id_score_tuples = joblib.load(path)
        id_score_tuples= sorted(id_score_tuples, key=lambda row: row[1], reverse=True)   # sort by score
        body = '\n'
        for tup in id_score_tuples:
            index = self.files.find(self.files.dataset,'file_id',tup[0])
            if index >= 0:
                if 'img_ext' in self.files.dataset[index] and 'text_ext' in self.files.dataset[index]:
                    img_ext = self.files.dataset[index]['img_ext']
                    text_ext = self.files.dataset[index]['text_ext']
                    img_path = self.files.dataset_path+'/'+str(class_id)+'/'+tup[0]+'.'+img_ext
                    text_path = self.files.dataset_path+'/'+str(class_id)+'/'+tup[0]+'.'+text_ext
                    text = self.files.load_file(text_path)
                    body += "\t<tr>\n"
                    body += "\t\t<td><image src='"+img_path+"' width='300' /></td>"
                    body += "<td><p>"+text+"</p></td>"
                    body += "<td>"+str(tup[1])+"</td>\n"
                    body += "\t<tr>\n"

        html = self.header+body+self.footer
        path = self.files.dataset_path+'/'+str(class_id)+'_ranked_texts.html'
        self.files.save_file(path,html)


    def find(self, lst, key, value):
        for i, pair in enumerate(lst):
            if pair[key] == value:
                return i
        return -111

    def gen_ranked_docs_by_all(self,class_id, lamda1, lamda2):
        path_i = self.files.dataset_path+'/'+str(class_id)+'_ranked_images.pkl'
        path_t = self.files.dataset_path+'/'+str(class_id)+'_ranked_texts.pkl'
        ituples = joblib.load(path_i)
        ttuples = joblib.load(path_t)
        id_score_tuples = []
        for image in ituples:
            i = self.find(ttuples,0,image[0])
            if i != -111:
                text = ttuples[i]
                score = lamda1*image[1]+lamda2*text[1]
                id_score_tuples.append((image[0],score))

        id_score_tuples= sorted(id_score_tuples, key=lambda row: row[1], reverse=True)   # sort by score
        body = '\n'
        for tup in id_score_tuples:
            index = self.files.find(self.files.dataset,'file_id',tup[0])
            if index >= 0:
                if 'img_ext' in self.files.dataset[index] and 'text_ext' in self.files.dataset[index]:
                    img_ext = self.files.dataset[index]['img_ext']
                    text_ext = self.files.dataset[index]['text_ext']
                    img_path = self.files.dataset_path+'/'+str(class_id)+'/'+tup[0]+'.'+img_ext
                    text_path = self.files.dataset_path+'/'+str(class_id)+'/'+tup[0]+'.'+text_ext
                    text = self.files.load_file(text_path)
                    body += "\t<tr>\n"
                    body += "\t\t<td><image src='"+img_path+"' width='300' /></td>"
                    body += "<td><p>"+text+"</p></td>"
                    body += "<td>"+str(tup[1])+"</td>\n"
                    body += "\t<tr>\n"

        html = self.header+body+self.footer
        path = self.files.dataset_path+'/'+str(class_id)+'_ranked_all.html'
        self.files.save_file(path,html)