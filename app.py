import flask
import json
from flask import render_template
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/test_flask', methods=['POST'])
def test_flask():
    req_data = request.get_json()
    return req_data
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#testing a merge
#adding one more
