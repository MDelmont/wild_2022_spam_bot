#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from modules.conf import Conf

import base64
class Datas():
    def __init__(self, app):
        self.app = app
        self.conf = Conf()
    
    def get_data(self,type):
        
        return None
    def get_dataframe(self):

        return pd.read_csv(f'{self.conf.path_file_dataframe}email-icon.jpg')

    def get_image_ham_spam(self,type):
        path=f'{self.conf.path_file_image}email-icon.jpg'
        if type == 'ham':
            path =  f'{self.conf.path_file_image}email-icon.jpg'
        else:
            path =  f'{self.conf.path_file_image}spam.jpg'
        
        encoded_image = base64.b64encode(open(path, 'rb').read())

        trendImage = 'data:image/jpg;base64,{}'.format(encoded_image.decode())

        return trendImage
