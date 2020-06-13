from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from flask_cors import CORS
import pandas as pd

connection = create_engine('mssql://SA:Elote655@34.69.177.195:1433/sistemaB?driver=SQL Server Native Client 11.0')
app = Flask(__name__)
CORS(app, supports_credentials='false')

@app.route("/delicuente/antecedentes/<string:cui>/", methods=['GET', 'POST'])
def AllAgentes(cui):
    result = {}
    if(request.method == 'GET'):
        conn = connection.connect()#CONVERT(VARCHAR(20), fecha_nacimiento, 103)
        sql = "SELECT [cui],[nombres],[apellidos],[fechaDelitoCometido],[fechaAprension],[tiempoPreventivo],[multa],[TipoDelito]FROM [sistemaB].[dbo].[GetAnts]"
        sql = sql + "WHERE cui = '" + cui + "'"
        result = pd.read_sql_query(sql, conn)
        result = result.to_json(orient ='index')
    return result

@app.route("/socket.io/", methods=['GET', 'POST'])
def prueba():
    return {}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')