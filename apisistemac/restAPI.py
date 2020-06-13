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
    app.run(host='0.0.0.0', port='5000')