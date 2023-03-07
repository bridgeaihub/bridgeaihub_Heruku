from click import command
from flask import Flask, render_template, request, redirect, url_for, session, flash
import re
import os
from werkzeug.utils import secure_filename
from subprocess import check_output
import subprocess

app = Flask(__name__)

# Intialize MySQL
@app.route('/')
def landing():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0' , port=5000)