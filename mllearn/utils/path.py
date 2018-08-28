# -*- coding: utf-8 -*-
"""
create on 2018-04-29 下午4:02

author @heyao
"""

import os

project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
datasets_path = os.path.join(project_path, 'datasets')

_get_data_path = lambda path: os.path.normpath(os.path.join(datasets_path, path))
