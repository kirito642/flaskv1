import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route('/')
def root():
    return '欢迎访问根路由！'

@app.route('/index', methods=['GET', 'POST'])
def index():
    x = request.args.get('x')
    y = request.form.get('y')
    return jsonify({'laowang': True, 'laotong': False})

@app.route('/bad')
def bad():
    return '姐姐真漂亮'

def handler(event, context):
    with app.request_context(event['headers'], event['queryStringParameters'], event['body'], method=event['httpMethod']):
        try:
            response = app.full_dispatch_request()
        except Exception as e:
            response = app.make_response(str(e))
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.get_data(as_text=True)
        }
