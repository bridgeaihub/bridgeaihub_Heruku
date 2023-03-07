from click import command
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os
from werkzeug.utils import secure_filename
from subprocess import check_output
import subprocess

app = Flask(__name__)
app.secret_key = 'sudo'

# Intialize MySQL
mysql = MySQL(app)
@app.route('/', methods=['GET','POST'])
def landing():
    return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0' , port=5000)