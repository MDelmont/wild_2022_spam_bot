#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dash import html,dcc
from modules.conf import Conf
import tensorflow
import joblib
from datas.datas import Datas
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import plotly.express as px
import numpy as np

class Models():
    def __init__(self, app):
        self.app = app
        self.conf = Conf()
        self.datas = Datas(app)
    
    def get_value_model(self,librairie,model,text):
        print(librairie)
        model = self.get_model(librairie,model)
        print(librairie)
        print(self.conf.path_file_model+'vec_model.sav')
        print("-1")
        
        vec_model = joblib.load(self.conf.path_file_model+'vec_model.sav')
        print("1")
        result='ham'
        print(librairie)
        if librairie == 'Tensor Flow':
            print("3")
            result = round(model.predict(vec_model.transform([text]).toarray())[0][0])
        else:
            print("4")
            result = model.predict(vec_model.transform([text]))
       
        print("2")
        return 'spam' if result == 0 else 'ham'

    def get_model(self,librairie,model):
        if librairie == 'Scikit Learn':
            if model == 'Perceptron':
                name='sk_perceptron_model.sav'
            else:
                 name='sk_MLP_identity_adam.sav'

        elif librairie == 'Tensor Flow':
            name='tf_MLP_tanh_32_2_sgd.sav'
        print(self.conf.path_file_model+name)
        model = joblib.load(self.conf.path_file_model+name)
        print('5')
        return model

    def get_model_metrics(self, librairie=None, model_name=None, layer=None, activation=None, neurons_nb=None, solver=None):
        model = self.get_model_param(librairie, model_name, layer, activation, neurons_nb, solver)
        vec_model = joblib.load(self.conf.path_file_model + 'vec_model.sav')
        df = self.datas.get_dataframe()
        X = df['sms_clean']
        y = df['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        X_test_vec = vec_model.transform(X_test)

        if 'Tensor Flow' in model_name:
            y_pred = np.round(model.predict(X_test_vec.toarray())).astype(int)
        else:
            y_pred = model.predict(X_test_vec)
        conf_mat = confusion_matrix(y_true=y_test, y_pred=y_pred, )
        accuracy = metrics.accuracy_score(y_test, y_pred)
        recall = metrics.recall_score(y_test, y_pred)
        f1_score = metrics.f1_score(y_test, y_pred)
        fig = px.imshow(conf_mat, color_continuous_scale=['#79AADB', '#56799C', '#2C3E50', '#32475C', '#1D2A36'],
                        text_auto=True),
        fig.update_layout(title='Confusion matrix {}'.format(model_name), title_x=0.5, title_font_family="Verdana")
        return [accuracy], [recall], [f1_score], fig

    def get_model_param(self, librairie=None, model=None, layer=None, activation=None, neurons_nb=None, solver=None):
        if model == "Perceptron":
            path_model = f"{self.conf.path_file_model}sk_perceptron_model.sav"
        elif librairie == 'Scikit Learn':
            path_model = f"{self.conf.path_file_model}sk_MLP_{activation}_{solver}.sav"
        else:
            path_model = f"{self.conf.path_file_model}tf_MLP_{activation}_{neurons_nb}_{layer}_{solver}.sav"
        model = joblib.load(path_model)

        return model





        