from flask import Flask,jsonify,request,json
from flask_pymongo import PyMongo
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import jwt
# import ObjectId;

app=Flask(__name__)
app.config['MONGO_DBNAME'] = 'reactloginreg'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/reactloginreg'
app.config['JWT_SECRET_KEY'] = 'secret'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)

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
    else:
        user_id = users.insert({
            'email':email,
            'password': password,
            'created': created
        })



    result = {'email' :email + ' registered'}
    return jsonify({'result' : result})


'''Writing backend for login page'''

@app.route('/users/login',methods=["POST"])
def login():
    users=mongo.db.usersList
    email= request.get_json()['email']
    password=request.get_json()['password']
    result= ""

    response = users.find_one({'email': email})
    print(response)
    if response:
        if bcrypt.check_password_hash(response['password'],password):
            # access_token = create_access_token(identity={
            #     '_id' : response['_id']
            myToken=jwt.encode({'email':response['email'].encode()},app.config['JWT_SECRET_KEY'])
            result = jsonify({'token':myToken})
        else:
            result = jsonify({'error':'Invalid Username and Password'})
    else:
        result= jsonify({'result':'No results found'})
    
    return result

def validaToken():
    token=request.headers.get('Authorization')
    test,token=token.split()
    userdata= jwt.decode(token,app.config['JWT_SECRET_KEY'])
    print( userdata['email'].encode())
    return userdata['email'].encode()

@app.route('/userlist',methods=['GET'])
def get_all_tasks():
    users=mongo.db.usersList
    result=[]
    for q in users.find():
        result.append({'_id':str(q['_id']),'email':q['email']})
    return jsonify(result)  

@app.route('/users/update',methods=['PUT'])
def update_task():
    email =  validaToken()
    if(email):
        print("Validated")
        users = mongo.db.usersList
        first_name = request.get_json()['first_name']
        last_name=request.get_json()['last_name']
        contact_number=request.get_json()['contact_num']
        users.find_one_and_update({'email':email},{"$set":{"first_name":first_name}},upsert=False)
        users.find_one_and_update({'email':email},{"$set":{"last_name":last_name}},upsert=False)
        users.find_one_and_update({'email':email},{"$set":{"contact_number":contact_number}},upsert=False)
        new_task = users.find_one({'email':email})
        result="sucess"
    else:
        result="fail"
    return jsonify({"result":result})

@app.route('/users/delete',methods=['DELETE'])
def delete_task(): 
    email =  validaToken()
    if(email):
        users=mongo.db.users
        response = users.delete_one({'email':email})
        if(response):
            result="sucess"
    else:
        result ="fail",402
    return jsonify({'result':result})
if __name__ == '__main__':
    app.run(debug=True)



