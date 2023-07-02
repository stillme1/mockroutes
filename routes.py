from asyncio import sleep
import time
from flask import Flask, jsonify
from flask_cors import CORS
import string, random

app = Flask(__name__)
CORS(app)

def randomString():
	length = random.randint(2, 40)
	res = ''.join(random.choices(string.ascii_lowercase, k=length))
	return res

@app.route('/addDocuments', methods=['POST'])
def postDocumentUrl():
	# time.sleep(2)
	decide = random.randint(1, 3)
	return jsonify({'message': 'access denied'}), 401
	return jsonify({
		'status': 'success',
		'data': {
			'token': randomString(),
			'notificationEmails': ["firstEmail@email.com", "second@email.com", "third@email.com"]
		}
   	})
	# return jsonify({'status': 'success'})

@app.route('/serviceUserEmail')
def getEmail():
	# time.sleep(5)
	# return "", 400
	return jsonify({'email': '{}@trilogy.com'.format(randomString())})

app.run(debug=True, port=5000)
