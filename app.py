from flask import Flask

app = Flask(__hello_world__)



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Ahmed Zulfiqar!'


if __name__ == '__main__':
    app.run()
