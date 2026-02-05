from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome! Go to /hello to see the Hello World page.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()
