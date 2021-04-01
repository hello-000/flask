#!/bin/python3

from flask import Flask, request, redirect, flash
from flask import url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from werkzeug.security import generate_password_hash, check_password_hash
import os,sys
from flask_login import login_user, logout_user, login_required, current_user
from flask_login import UserMixin
from flask_login import LoginManager
from flask import make_response

app=Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/setcookie",methods=['GET','POST'])
def setcookie():
   if request.method == 'POST':
        user = request.form['name']

        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)

        return resp

@app.route("/getcookie")
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
