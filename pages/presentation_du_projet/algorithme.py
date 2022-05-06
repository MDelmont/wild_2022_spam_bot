#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dash import html,dcc

import datetime
import logging


class Algoritme():
    def __init__(self, app):
        self.app = app

    def get_layout(self):
        layout = html.Div([

            html.Div([
                html.H1("Les algorithmes"),
            ], style={'textAlign': 'center'}),

            html.Div([
                html.Div([
                    html.H6('Sélectionner une librairie'),
                    dcc.Dropdown(id='librairies_choice',
                                 options=['Scikit Learn', 'Tensor Flow'],
                                 value='Scikit Learn',
                                 clearable=False,
                                 )
                ], style={'width': '50%', 'display': 'inline-block'}),
                html.Div([
                    html.H6('Sélectionner un modèle'),
                    dcc.Dropdown(id='model_choice',
                                 options=['Perceptron', 'MLP'],
                                 value='Perceptron',
                                 clearable=False,
                                 )
                ], style={'width': '50%', 'display': 'inline-block'}),

            ], style={'width': '80%', 'textAlign': 'center', 'padding-left': '10%'}),

            html.Div([
                html.H3('Sélectionner les paramètres'),
                html.Div([
                    html.H6("Sélectionner la fonction d'activation"),
                    dcc.Dropdown(id='ts_MLP_activation',
                                 options=[{'label': i, 'value': i} for i in ['tanh','relu','sigmoid']],
                                 value='tanh',
                                 clearable=False,
                                 )
                ], style={'width': '25%', 'display': 'inline-block'}),
                html.Div([
                    html.H6("Sélectionner le nombre de neurones"),
                    dcc.Dropdown(id='ts_MLP_neurones',
                                 options=[{'label': i, 'value': i} for i in ['32', '64', '100']],
                                 value='32',
                                 clearable=False,
                                 )
                ], style={'width': '25%', 'display': 'inline-block'}),
                html.Div([
                    html.H6("Sélectionner le nombre de couches"),
                    dcc.Dropdown(id='ts_MLP_couches',
                                 options=[{'label': i, 'value': i} for i in ['1', '2']],
                                 value='1',
                                 clearable=False,
                                 )
                ], style={'width': '25%', 'display': 'inline-block'}),
                html.Div([
                    html.H6("Sélectionner le solveur'"),
                    dcc.Dropdown(id='ts_MLP_solveur',
                                 options=[{'label': i, 'value': i} for i in ['adam','sgd','RMSprop']],
                                 value='adam',
                                 clearable=False,
                                 )
                ], style={'width': '25%', 'display': 'inline-block'}),

            ], id='ts_MLP', style={'display':"none", 'width': '80%', 'textAlign': 'center', 'padding-left': '10%'}),

            html.Div([
                html.H3('Sélectionner les paramètres'),
                html.Div([
                    html.H6("Sélectionner la fonction d'activation"),
                    dcc.Dropdown(id='sk_MLP_activation',
                                 options=[{'label': i, 'value': i} for i in ['identity', 'logistic', 'relu', 'tanh']],
                                 value='tanh',
                                 clearable=False,
                                 )
                ], style={'width': '50%', 'display': 'inline-block'}),
                html.Div([
                    html.H6("Sélectionner le solveur"),
                    dcc.Dropdown(id='sk_MLP_solveur',
                                 options=[{'label': i, 'value': i} for i in ['adam','sgd']],
                                 value='adam',
                                 clearable=False,
                                 )
                ], style={'width': '50%', 'display': 'inline-block'}),

            ], id='sk_MLP', style={"display": "none", 'width': '80%', 'textAlign': 'center', 'padding-left': '10%'}),

            html.Div([
                html.Div([
                    html.H3("Accuracy"),
                    html.H4(id="accuracy")
                ], style={'width': '25%', 'display': 'inline-block'}),
                html.Div([
                    html.H3("F1-score"),
                    html.H4(id="f1_score")
                ], style={'width': '25%', 'display': 'inline-block'}),
                html.Div([
                    html.H3("Recall"),
                    html.H4(id="recall")
                ], style={'width': '25%', 'display': 'inline-block'}),
                html.Div([
                    html.H3("Confusion Matrix"),
                    dcc.Graph(id="graph_conf_mat")
                ], style={'width': '25%', 'display': 'inline-block'}),

            ], id="result_algo", style={"display": "block", 'width': '80%', 'textAlign': 'center', 'padding-left': '10%'})
        ])
        return layout