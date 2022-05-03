#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash
import dash_bootstrap_components as dbc
import logging
from datetime import datetime
import pytz

class App():
    def __init__(self):
  
        self.start_time = datetime.now()
        self.launch_time = pytz.timezone('Europe/Paris').localize(datetime.now()).strftime('%Y-%m-%d_%H_%M')

        logging.basicConfig(filename=f"outlogs_{self.launch_time}.log",level=logging.INFO)

        logging.info(f"[ INITIALISATION : APP for SPAM DETECT {self.launch_time} ]")
        
        #bootstrap_theme=[dbc.themes.BOOTSTRAP,'https://bootswatch.com/5/flatly/bootstrap.min.css']
        # meta_tags are required for the app layout to be mobile responsive
        
        self.app = dash.Dash(__name__, 
                             suppress_callback_exceptions=True,
                            meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}],
                            #external_stylesheets=bootstrap_theme
                            )
        self.server = self.app.server