#coding:utf-8
from flask import Flask
from main import app
app.config.from_pyfile('settings.py')
from apis import views
