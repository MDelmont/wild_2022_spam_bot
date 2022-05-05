#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dash import html,dcc


class Detection_des_spams():
    def __init__(self, app):
        self.app = app
    
    def get_layout(self):
        layout = html.Div([
                        dcc.Dropdown(['Scikit Learn', 'Tensor Flow'], 
                        placeholder="Select a module")
                        ])
        return layout