#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dash import html,dcc
from modules.conf import Conf
import joblib
class Models():
    def __init__(self, app):
        self.app = app
        self.conf = Conf()
    
    def get_value_model(self,librairie,model,text):

        model = self.get_model(librairie,model)
        print(self.conf.path_file_model+'vec_model.sav')
        vec_model = joblib.load(self.conf.path_file_model+'vec_model.sav')
        result='ham'
        
        if librairie == 'Tensorflow':
            result = round(model.predict(vec_model.transform([text]).toarray())[0][0])
        else:
            result = round(model.predict(vec_model.transform([text]).toarray())[0][0])

        return 'spam' if result == 0 else 'ham'

    def get_model(self,librairie,model):
        if librairie == 'Scikit Learn':
            if model == 'Perceptron':
                name='sk_perceptron_model.sav'
            else:
                 name='sk_MLP_identity_adam.sav'
        else:
            name= 'tf_MLP__tanh_32_2_sgd.sav'
        print(self.conf.path_file_model+name)
        return joblib.load(self.conf.path_file_model+name)






        