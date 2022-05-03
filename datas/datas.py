#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dash import html,dcc


class Datas():
    def __init__(self, app):
        self.app = app
    
    def get_data(self,type):
        return None