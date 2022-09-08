from flask import Flask
import requests
import os
import random

app = Flask(__name__)
app.secret_key = 'alsjfoiewcjrowieorxewroewrekfje'

list_urls = os.environ['LIST_URLS'].split(',')

@app.route('/test-hit', methods=['GET'])
def testIndex():
  response = requests.get(random.choice(list_urls))  
  return "Got it", 200

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  app.run(host='0.0.0.0', port=8990)
