from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/<n1>/<n2>')
def cal(n1,n2):
    try:
        n1 = int(n1)
        n2 = int(n2)
    except:
        return 'only int is accepted'
    return '%d' % (n1*n2)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)