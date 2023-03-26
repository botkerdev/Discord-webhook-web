from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        message = request.form['message']
        data = {
            'content': message
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 204:
            return '메세지 전송이 완료되었습니다!'
        else:
            return '메세지 전송에 오류가 발생했습니다..'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
