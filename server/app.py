from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True) #해당 파일 코드를 수정할 때마다 Flask가 변경된 것을 인식하고 재시작함
