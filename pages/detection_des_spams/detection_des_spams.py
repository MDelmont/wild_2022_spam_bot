#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dash import html,dcc


class Detection_des_spams():
    def __init__(self, app):
        self.app = app
    
    def get_layout(self):
        layout = html.Div([
                        html.Div([
                                html.H1('Détecteur de spams'),
                                ], style={'textAlign':'center'}),
                        html.Div([
                                html.Div([
                                        html.H6('Sélectionner une librairie'),
                                        dcc.Dropdown(
                                                    ['Scikit Learn', 'Tensor Flow'], 
                                                    'Scikit Learn',
                                                    clearable=False,
                                                    )
                                ], style = {'width' : '50%', 'display': 'inline-block'}
                                        ),
                                html.Div([
                                        html.H6('Sélectionner un modèle'),
                                        dcc.Dropdown(
                                                    ['Perceptron', 'MLP'], 
                                                    'Perceptron',
                                                    clearable=False,
                                                    )
                                ], style = {'width' : '50%', 'display': 'inline-block'}
                                ),   
                                ], style = {'width' : '80%', 'textAlign':'center', 'padding-left' : '10%'}),
                        html.Div([
                                html.Div([html.H6('Saisir le SMS'),
                                dcc.Textarea(placeholder='Saisir le SMS ici', style = {'width' : '50%', 'height' : '200px'}),
                                ], style = {'width' : '100%'}),
                                html.Button('Ham ou Spam?', id='test_button_ham_spam', n_clicks=0, className='btn-primary'),
                                ], style = {'width' : '80%', 'textAlign':'center', 'padding-left' : '10%'}),
                                html.Div([
                                        html.H1('', id='result_ham_spam')
                                        ], style = {'textAlign' : 'center', 'display' : None})
                        ])
        return layout