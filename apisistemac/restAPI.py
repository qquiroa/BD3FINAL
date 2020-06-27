<<<<<<< HEAD
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from flask_cors import CORS
import jwt, datetime, json

connection = create_engine('mysql+pymysql://qquiroa:elote655@34.72.22.112:3306/sistemac')
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ClavePrivadaBanco'
CORS(app, supports_credentials='false')

def verifyToken(token):
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'])
        return data
    except:
        return False

    return ''


@app.route("/pagos/<string:cui>", methods=['POST'])
def User(cui):
    result = {}
    jsonData = request.get_json()
    try:
        if request.method == 'POST' and verifyToken(jsonData['token']):
            conn = connection.connect()
            sql = "SELECT * FROM pago WHERE CUI = '" + cui + "'"
            query = conn.execute(sql)
            query = [i for i in query.cursor.fetchall()]
            paid = False
            if len(query) > 0:
                paid = True
            result = {'paid': paid, 'message': 'OK'}
        else:
            result['message'] = 'INVALID PETITION'
    except:
        result['message'] = 'INCOMPLETE DATA'

    return result

@app.route("/Login", methods=['POST'])
def Login():
    jsonData = request.get_json()
    try:
        if jsonData['user'] == 'usuario_renap' and jsonData['pwd'] == 'contra':
            token = jwt.encode({'user': jsonData['user'],
                                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},
                               app.config['SECRET_KEY'])
            return jsonify({'token': token.decode('UTF-8'), 'message': 'OK'})
        else:
            return jsonify({'message': 'INVALID DATA'})
    except:
        return jsonify({'message': 'ERROR'})


if __name__ == '__main__':
=======
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from flask_cors import CORS

connection = create_engine('mysql+pymysql://qquiroa:elote655@34.72.22.112:3306/sistemac')
app = Flask(__name__)
CORS(app)

@app.route("/pagos/<string:cui>", methods=['GET'])
def User(cui):
    if(request.method == 'GET'):
        conn = connection.connect()
        sql = "SELECT * FROM pago WHERE CUI = '" + cui + "'"
        query = conn.execute(sql)
        result = {'data' : [i for i in query.cursor.fetchall()]}

    return jsonify(result)

if __name__ == '__main__':
>>>>>>> ed768ce654e57ff4317daf0544c0f14660818a5b
    app.run(host='0.0.0.0', port='5000')