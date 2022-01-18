
from flask import Flask  ## flask를 설치해야 빨간 밑줄 삭제됨

app = Flask(__name__)
@app.route('/')  ## 기본페이지 요청 http://172.20.40.117:8080
def hell() :
    return "hello Flask:D  hohoho<h1>"  ## 클라이언트에 html로 바꿔 응답

@app.route('/test')  ## http://172.20.40.117:8080/test
def test() :
    ## 수행할 로직이 들어오는 곳
    return "test"

if __name__ == '__main__' :
   app.run("0.0.0.0",port = 8080)