# -*- coding: utf-8 -*-
"""
create on 2018-04-29 下午4:04

author @heyao
"""

from collections import namedtuple

import pandas as pd

from mllearn.utils.path import _get_data_path


def load_titanic():
    _datasets = namedtuple('titanic', "train target test target_names feature_names")
    target_column_name = 'Survived'
    train_path = _get_data_path('titanic/train.csv')
    test_path = _get_data_path('titanic/test.csv')
    df_train = pd.read_csv(train_path)
    df_test = pd.read_csv(test_path)
    feature_names = list(df_test.columns)
    train = df_train[df_test.columns]
    target = df_train[target_column_name].values
    target_names = list(set(df_train[target_column_name].values))
    return _datasets(train, target, df_test, target_names, feature_names)


def load_yelp_review_polarity():
    _datasets = namedtuple('yelp_review_polarity', 'train target test target_names feature_names')
    target_column_name = 'target'
    train_path = _get_data_path('yelp_review_polarity/train.csv')
    test_path = _get_data_path('yelp_review_polarity/test.csv')
    df_train = pd.read_csv(train_path, names=['target', 'content'])
    df_test = pd.read_csv(test_path, names=['target', 'content'])
    feature_names = list(df_test.columns)
    train = df_train[df_test.columns]
    target = df_train[target_column_name].values
    target_names = list(set(df_train[target_column_name].values))
    return _datasets(train, target, df_test, target_names, feature_names)


if __name__ == '__main__':
    data = load_titanic()
    print(data.train, '\n', data.target, '\n', data.test, '\n', data.target_names, '\n', data.feature_names)
    data = load_yelp_review_polarity()
    print(data.target, data.target_names)
