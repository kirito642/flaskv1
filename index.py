import requests
import flask
from flask import request, jsonify
app = flask.Flask(__name__)
@app.route('/index',methods=['GET','POST'])
def index():
    x=request.args.get('x')
    y=request.form.get('y')
    print(x)
    print(y)
    import json
    return jsonify({'laowang':True,'laotong':False})
@app.route('/bad')
def bad():
    return '姐姐真漂亮'
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
