#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
 
class Conf():
    def __init__(self):
        self.file_parent = Path(__file__).parent.parent
        self.path_file_image = f"{self.file_parent}\datas\images\\"
        self.path_file_dataframe = f"{self.file_parent}\datas\dataframe\\"
        self.path_file_model = f"{self.file_parent}\datas\models\\"
        self.red = '#e74c3c'
        self.bleu = '#2c3e50'
        pass