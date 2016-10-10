from flask import Flask, request, Response, json
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/hello', methods = [ 'GET' ])
def api_hello():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://jyntran.ca'

    return resp

@app.route('/messages', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written"

    else:
        return "415 Unsupported Media Type"

if __name__ == '__main__':
    app.run()
