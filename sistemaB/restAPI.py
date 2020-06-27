from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from flask_cors import CORS
import pandas as pd
import jwt, datetime, json

connection = create_engine('mssql://reader_user:Contra_123@34.69.177.195:1433/sistemaB?driver=SQL Server Native Client 11.0')
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ClavePrivadaPolicia'
CORS(app, supports_credentials='false')

def verifyToken(token):
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'])
        return data
    except:
        return False

    return ''

@app.route("/delicuente/antecedentes/<string:cui>", methods=['POST'])
def AllAgentes(cui):
    result = {}
    jsonData = request.get_json()
    try:
        if request.method == 'POST' and verifyToken(jsonData['token']):
            conn = connection.connect()  # CONVERT(VARCHAR(20), fecha_nacimiento, 103)
            sql = "SELECT [cui],[nombres],[apellidos],[fechaDelitoCometido],[fechaAprension],[tiempoPreventivo],[multa],[TipoDelito]FROM [sistemaB].[dbo].[GetAnts]"
            sql = sql + "WHERE cui = '" + cui + "'"
            result = pd.read_sql_query(sql, conn)
            result = json.loads(result.to_json(orient='index'))
            result['message'] = 'OK'
        else:
            result['message'] = 'INVALID PETITION'
    except Exception as e:
        print(e)
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
    app.run(host='0.0.0.0', port='5000')
