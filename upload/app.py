#!/bin/python3

from pypinyin import lazy_pinyin
import os
from flask import Flask, render_template, request,redirect,url_for,send_from_directory
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('upload/'+secure_filename(f.filename))
        return redirect(url_for('list_file'))
    else:
        return render_template('upload.html')

@app.route('/listfile')
def list_file():
    files = os.listdir('upload')
    return render_template('listfile.html',files = files) 

@app.route('/download/<filename>')
def download(filename):
    fname = filename.encode('cp936')
    return send_from_directory('upload', filename, mimetype='application/octet-stream')

if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0')

