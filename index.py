#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sre_parse import State
from dash import html, dcc
from dash.dependencies import Input, Output, State
from pages.header import Header
from app import App

from pages.detection_des_spams.detection_des_spams import Detection_des_spams
from pages.presentation_du_projet.algorithme import Algoritme
from pages.presentation_du_projet.donnee_entre import Donnee_entre
from pages.presentation_du_projet.perfomance import Performance
from pages.presentation_du_projet.pre_processing import Pre_processing
from datas.models.models import Models
from datas.datas import Datas



application = App()
app = application.app
server = application.server
header = Header()
models = Models(app)
data =Datas(app)
app.n_click_button = 0
#patate
#layout rendu par l'application
app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    header.menu,
    html.Div(id='page-content' )
    ])


def generate_variables(app):
    detect_spam = Detection_des_spams(app)
    algoritme = Algoritme(app)
    data_in = Donnee_entre(app)
    performance = Performance(app)
    pre_processing = Pre_processing(app)
    return detect_spam, algoritme, data_in, performance,pre_processing

detect_spam, algoritme, data_in, performance,pre_processing= generate_variables(app)


endpoints = {
         '/': detect_spam.get_layout(),
         '/detection_des_spams':  detect_spam.get_layout(),
         '/presentation_du_projet/algorithme': algoritme.get_layout(),
         '/presentation_du_projet/donnee_entree': data_in.get_layout(),
         '/presentation_du_projet/performance': performance.get_layout(),
         '/presentation_du_projet/pre_processing': pre_processing.get_layout(),
        }
 
#callback pour mettre à jour les pages
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    try:
        return endpoints[pathname]
    except Exception as error:
        return f"ERROR : {error}"


@app.callback(Output('model_choice', 'options'),
            Output('model_choice', 'value'),
            Input('librairies_choice', 'value'),
            State('model_choice', 'value'))
def update_model_choice(value_lib,value_model):

    try:
        if value_lib == 'Scikit Learn':
    
            return ['Perceptron', 'MLP'],value_model
        else:
            return ['MLP'],'MLP'

    except Exception as error:
        return f"ERROR : {error}"




@app.callback(Output('result_ham_spam', 'children'),
            Output('image-spam-ham', 'src'),
            Output('Div_result_ham_spam', 'style'),
            Input('test_button_ham_spam', 'n_clicks'),
            Input('librairies_choice', 'value'),
            Input('model_choice', 'value'),
            Input('sms_text','value'),
            Input('image-spam-ham', 'src'),)
def update_model_choice(n_clicks,librairies_choice,model_choice,sms_text,src):

    try:
        if n_clicks  and sms_text and app.n_click_button < n_clicks:
      
            app.n_click_button = n_clicks

            responce = models.get_value_model(librairies_choice,model_choice,sms_text)
 
            return responce , data.get_image_ham_spam(responce),{'textAlign' : 'center', 'display' : 'block'}
        else:
            return '',src,{'textAlign' : 'center', 'display' : 'none'}

    except Exception as error:
        return f"ERROR : {error}"
 
if __name__ == '__main__':
    app.run_server(debug=True)