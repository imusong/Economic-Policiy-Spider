import pymysql
from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

db = pymysql.connect("localhost","root","Zys0212017","mydatabase" )

cursor = db.cursor()

sql = "SELECT * FROM policy" 
cursor.execute(sql)
results = cursor.fetchall()

POLICIES=[]


for row in results:
    policy={}
    policy['id']= uuid.uuid4().hex,
    policy['title'] =str(row[0]),
    policy['time'] =str(row[1]),
    policy['article']=str(row[2])
    # print(row[0])
    POLICIES.append(policy)    
        
    

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



@app.route('/policies', methods=['GET'])
def all_books():
    response_object = {'status': 'success'}
    
    response_object['policies'] = POLICIES
    return jsonify(response_object)



if __name__ == '__main__':
    app.run()
