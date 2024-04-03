from flask import Flask, request
from service_API import CtprvnRltmMesureDnstyService
from service_filtering import Filtering

app = Flask(__name__)
service = CtprvnRltmMesureDnstyService()
service_filtering = Filtering()

@app.route('/CtprvnRltmMesureDnsty',methods=['GET'])
def request_CtprvnRltmMesureDnsty():
    city = request.args.get('city')
    nei = request.args.get('nei')       #쿼리 스트링

    result = service.request_getCtprvnRltmMesureDnsty(city)
    resultFilter= service_filtering.filter_response_nei(nei,result)

    return resultFilter

@app.route('/CtprvnRltmMesureDnsty/total',methods=['GET'])
def request_CtprvnRltmMesureDnsty_total():
    city = request.args.get('city')

    result = service.request_getCtprvnRltmMesureDnsty(city)
    return result


#밑에 있어야 python app.py로 실행시켰을때 제대로 작동
if __name__ == '__main__':
    app.run(debug=True, port=4006)
