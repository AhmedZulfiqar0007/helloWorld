from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome! Go to /hello to see the Hello World page.'

@app.route('/hello')
def hello():
    return 'Hello World from Ahmed Zulfiqar! This is my first HTML page.'

if __name__ == '__main__':
    app.run()
