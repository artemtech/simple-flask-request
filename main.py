from flask import Flask
import logging
import requests
import os
import random

app = Flask(__name__)
app.secret_key = 'alsjfoiewcjrowieorxewroewrekfje'

list_urls = os.environ['LIST_URLS'].split(',')

@app.route('/subdir/test-hit', methods=['GET'])
def testIndex():
  current_url = random.choice(list_urls)
  response = requests.get(current_url)  
  return f"{current_url}", 200

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  app.run(host='0.0.0.0', port=8990)
