from flask import Flask, render_template, request
import time
import numpy as np
import os
import fasttext
from jamo import h2j, j2hcj


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('write.html')


@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        #현재 넣은값 출력하게 만들었음
        with open("./train_data.txt", "w") as f:
            f.write(content)


        return render_template('result.html', category = category, title=title, content=content)







