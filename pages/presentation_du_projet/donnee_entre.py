#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dash import html,dcc

import datetime
import logging


class Donnee_entre():
    def __init__(self, app):
        self.app = app

    def get_layout(self):
        return None