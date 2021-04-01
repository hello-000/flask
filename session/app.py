from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)
app.secret_key = "test"

@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        return '''
                  登录用户名是: %s <br>
                  <b>点击这里<a href='/logout'>注销<a/></b>
               ''' % username
    return "您暂未登录,<br><a href = '/login'></b>" + "点击这里登录</b></a>"

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return '''
   <form action = "" method = "post">
      <p><input type ="text" name ="username"/></p>
      <p><input type ="submit" value ="登录"/></p>
   </form>
   '''
@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
