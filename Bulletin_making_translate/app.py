from pymongo import MongoClient
# import jwt
# import datetime
# import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
# from werkzeug.utils import secure_filename
# from datetime import datetime, timedelta

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbprac

# 홈페이지 불러오기
@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5500, debug=True)