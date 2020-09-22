import json
from flask import (
    Flask,
    request,
    render_template,
    make_response,
    jsonify
)
import config.scrape_config as scrape_config


# init Flask app instance
app = Flask(
    __name__
)


# ping route (for testing)
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({ 'output': 'hi there' })


# get Samtrygg results
@app.route('/get_samtrygg_results', methods=['GET'])
def get_samtrygg_results():
    filepath = '/' + scrape_config.SAMTRYGG_DATASTORE_FILENAME
    with open(filepath) as f:
        json_string = f.read()
        return json_string


# run the app if executed as main file to python interpreter
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    