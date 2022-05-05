#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dash import html,dcc
from datas.datas import Datas

class Detection_des_spams():
    def __init__(self, app):
        self.app = app
        self.data = Datas(app)
    
    def get_layout(self):
        layout = html.Div([
                    html.Div([
                        html.H1('Détecteur de spams'),
                    ], style={'textAlign':'center'}),
                    
                    html.Div([
                        html.Div([
                            html.H6('Sélectionner une librairie'),
                            dcc.Dropdown(id='librairies_choice',
          
                                options = ['Scikit Learn', 'Tensor Flow'], 
                                value = 'Scikit Learn',
                                clearable = False,
                            )
                        ], style = {'width' : '50%', 'display': 'inline-block'}),
                        html.Div([
                            html.H6('Sélectionner un modèle'),
                            dcc.Dropdown(id='model_choice',
                                options = ['Perceptron', 'MLP'], 
                                value = 'Perceptron',
                                clearable = False,
                            )
                        ], style = {'width' : '50%', 'display': 'inline-block'}), 

                    ], style = {'width' : '80%', 'textAlign':'center', 'padding-left' : '10%'}),

                    html.Div([
                        html.Div([
                            html.H6('Saisir le SMS'),
                            dcc.Textarea(id='sms_text',placeholder='Saisir le SMS ici', style = {'width' : '50%', 'height' : '200px'}),
                        ], style = {'width' : '100%'}),
                        html.Button('Ham ou Spam?', id='test_button_ham_spam', n_clicks=0, className='btn-primary'),
                    ], style = {'width' : '80%', 'textAlign':'center', 'padding-left' : '10%'}),

                    html.Div(id='Div_result_ham_spam',
                    children=[
                            html.H1(children='ham', id='result_ham_spam'),

                            html.Img(id='image-spam-ham',src=self.data.get_image_ham_spam('ham'),style={'height':'150px', 'width':'150px'})     
                    ], style = {'textAlign' : 'center', 'display' : 'none'})
                ])
        return layout
