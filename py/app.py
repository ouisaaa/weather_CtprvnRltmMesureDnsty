from flask import Flask, request,make_response
from service_API import CtprvnRltmMesureDnstyService
from service_filtering import Filtering
from flask_cors import CORS

app = Flask(__name__)
# CORS(app, resources={r"/CtprvnRltmMesureDnsty*": {"origins": ["http://localhost:5000","http://localhost:3000"], "methods": ["GET"], "allowed_headers": ["Content-Type"]}})


service = CtprvnRltmMesureDnstyService()
service_filtering = Filtering()

@app.route('/CtprvnRltmMesureDnsty',methods=['GET'])
def request_CtprvnRltmMesureDnsty():
    city = request.args.get('city')
    nei = request.args.get('nei')       #쿼리 스트링

    result = service.request_getCtprvnRltmMesureDnsty(city)
    resultFilter= service_filtering.filter_response_nei(nei,result)

    response=make_response(resultFilter)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")

    return response


@app.route('/CtprvnRltmMesureDnsty/total',methods=['GET'])
def request_CtprvnRltmMesureDnsty_total():
    city = request.args.get('city')

    result = service.request_getCtprvnRltmMesureDnsty(city)
    return result


#밑에 있어야 python app.py로 실행시켰을때 제대로 작동
if __name__ == '__main__':
    app.run(debug=True, port=4006)
