#!flask/bin/env python
#coding:utf-8

#引入Form基类
from flask_wtf import Form
#引入Form元素父类
from wtforms import StringField,PasswordField
#引入Form验证父类
from wtforms.validators import DataRequired, Length

__author__ = 'kikay'

class BaseLogin(Form):
    name=StringField('name',validators=[DataRequired(message=u"no blank")
        ,Length(10,20,message=u'10~20')],render_kw={'placeholder':u'input username'})
    password=PasswordField('password',validators=[DataRequired(message=u"pass not bull")
        ,Length(10,20,message=u'10~20')],render_kw={'placeholder':u'input pwd'})
