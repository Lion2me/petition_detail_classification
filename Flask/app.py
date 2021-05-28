from flask import Flask,render_template ,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('write.html')


@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        #현재 넣은값 출력하게 만들었음
        return render_template('result.html', title=title, content=content)






