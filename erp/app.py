import mysql.connector as mys
import time
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('studentlogin.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mycon = mys.connect(host='localhost', user='root',
                            passwd='root', database="erp")
        mycursor = mycon.cursor()
        mycursor.execute("select * from studentlogin")
        for i in mycursor:
            if username == i[0] and password == i[1]:
                return render_template('erp.html')
            else:
                return render_template('studentlogin.html')

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except:
        pass
