from flask import Flask
import random

app = Flask(__name__)


topics = [
    {'id':1, 'title': 'html', 'body': 'html is ...'},
    {'id':2, 'title': 'css', 'body': 'css is ...'},
    {'id':3, 'title': 'javascropt', 'body': 'javascropt is ...'}
]

@app.route('/')
def index():
    liTags = ''
    for topic in topics:
        #이해돕기위해 liTags = liTags + '<li>'+topic['title']+'</li>'
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
        
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {liTags}
            </ol>
            <h2>Welcome</h2>
            Hello, web
        </body>
    </html>
     '''

     
@app.route('/create')
def create():
    return 'Create'

@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'Read '+id

app.run(debug=True)



""" #직접코딩
@app.route('/')
def index():
    return '''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                <li><a href="/read/1">html</a></li>
                <li><a href="/read/2">css</a></li>
                <li><a href="/read/3">javascropt</a></li>
            </ol>
            <h2>Welcome</h2>
            Hello, web
        </body>
    </html>
     '''
"""

