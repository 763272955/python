# -*- coding:utf-8 -*-

import os

class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

class Development_Config(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/employeesys'

config = {
'development': Development_Config,
'default': Development_Config
}