#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dash import html, dcc
from dash.dependencies import Input, Output
from pages.header import Header
from app import App

from pages.detection_des_spams.detection_des_spams import Detection_des_spams
from pages.presentation_du_projet.algorithme import Algoritme
from pages.presentation_du_projet.donnee_entre import Donnee_entre
from pages.presentation_du_projet.perfomance import Performance

application = App()
app = application.app
server = application.server
header = Header()


#layout rendu par l'application
app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    header.menu,
    html.Div(id='page-content')
    ])


def generate_variables(app):
    detect_spam = Detection_des_spams(app)
    algoritme = Algoritme(app)
    data_in = Donnee_entre(app)
    performance = Performance(app)
    return detect_spam, algoritme, data_in, performance

detect_spam, algoritme, data_in, performance= generate_variables(app)


endpoints = {
         '/': detect_spam.get_layout(),
         '/detection_des_spams':  detect_spam.get_layout(),
         '/presentation_du_projet/algorithme': algoritme.get_layout(),
         '/presentation_du_projet/donnee_entree': data_in.get_layout(),
         '/presentation_du_projet/performance': performance.get_layout(),
        }
 
#callback pour mettre à jour les pages
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    try:
        return endpoints[pathname]
    except Exception as error:
        return f"ERROR : {error}"

 
if __name__ == '__main__':
    app.run_server(debug=True)