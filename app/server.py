import json
from flask import (
	Flask,
	request,
	render_template,
	make_response,
	jsonify
)


# init Flask app instance
app = Flask(
	__name__
)


# ping route (for testing)
@app.route('/ping', methods=['GET'])
def ping():
	return jsonify({ 'output': 'hi there' })


# run the app if executed as main file to python interpreter
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    