from flask import Flask,jsonify,request,json
from flask_pymongo import PyMongo
from bson import ObjectId
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token


app=Flask(__name__)
app.config['MONGO_DBNAME'] = 'reactloginreg'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/reactloginreg'
app.config['JWT_SECRET_KEY'] = 'secret'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)

@app.route('/users/register',methods=["POST"])
def register():
    users=mongo.db.usersList
    email= request.get_json()['email']
    password= bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    created = datetime.utcnow()
    response =users.find_one({'email':email})
    if response:
        result=jsonify({'result':"email already existed"}),409
    else
        user_id = users.insert({
            'email':email,
            'password': password,
            'created': created
        })

    # new_user = users.find_one({'_id': user_id})

    result = {'email' :email+ ' registered'}
    return jsonify({'result' : result})


'''Writing backend for login page'''

@app.route('/users/login',methods=["POST"])
def login():
    users=mongo.db.usersList
    email= request.get_json()['email']
    password=request.get_json()['password']
    result= ""

    response = users.find_one({'email': email})

    if response:
        if bcrypt.check_password_hash(response['password'],password):
            access_token = create_access_token(identity={
                'email' : response['email']
            })
            result = jsonify({'token': access_token})
        else:
            result = jsonify({'error':'Invalid Username and Password'})
    else:
        result= jsonify({'result':'No results found'})
    
    return result
@app.route('/userlist',methods=['GET'])
def get_all_tasks():
    users=mongo.db.usersList
    result=[]
    for field in users.find():
        result.append({'_id':str(field['_id']),'email':field['email']})
    return jsonify(result)  
@app.route('/profile/update/<id>',methods=['PUT'])
def update_task(id):
    users = mongo.db.usersList
    first_name = request.get_json()['first_name']
    last_name=request.get_json()['last_name']
    contact_number=request.get_json()['contact_number']
    users.find_one_and_update({'_id':ObjectId(id)},{"$set":{"first_name":first_name}},upsert=False)
    users.find_one_and_update({'_id':ObjectId(id)},{"$set":{"last_name":last_name}},upsert=False)
    users.find_one_and_update({'_id':ObjectId(id)},{"$set":{"contact_number":contact_number}},upsert=False)
    new_task = users.find_one({'_id':ObjectId(id)})

    result ={"result":new}

    return jsonify({"result":result})
@app.route('/user/<id>',methods=['DELETE'])
def delete_task(id):
    users=mongo.db.users
    response = users.delete_one({'_id':ObjectId(id)})
    if response.deleted_count ==1:
        result={'message':'record deleted'}
    else:
        result ={'message':'record not found'}
    return jsonify({'result':result})
if __name__ == '__main__':
    app.run(debug=True)



