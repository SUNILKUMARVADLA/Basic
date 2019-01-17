from flask import Flask,jsonify,request,json,url_for,redirect
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask_pymongo import PyMongo
import datetime
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import jwt
import plivo
from flask import flash
import os
from random import randint
# import ObjectId;

app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'vadlasunilkumar225@gmail.com'
app.config['MAIL_PASSWORD'] = '9963563365'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
app.config['MONGO_DBNAME'] = 'reactloginreg'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/reactloginreg'
app.config['JWT_SECRET_KEY'] = 'secret'
auth_id = "MAOTLIMZFLOWFHZMQWNT"
auth_token = "YTcxNDg5MzgwZWJmNTQyMDE5ZjE5OWUxNWFkNjI5"
client = plivo.RestClient(auth_id='MAOTLIMZFLOWFHZMQWNT', auth_token='YTcxNDg5MzgwZWJmNTQyMDE5ZjE5OWUxNWFkNjI5')
# s = URLSafeTimedSerializer('Thisisasecret!')
mongo = PyMongo(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
CORS(app)
def setr_value(r):
    global globvar 
    globvar = r
def setm_value(email):
    global globm
    globm=email
    print(globm)
@app.route('/users/register',methods=["POST"])
def register():
    users=mongo.db.newUsers
    email= request.get_json()['email']
    password= bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    pnum=request.get_json()['pnum']
    created = datetime.datetime.utcnow()
    response =users.find_one({'email':email})
    if response:
        result=jsonify({'result':"email already existed"}),409
        return result
    else:
         password= bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
         created = datetime.datetime.utcnow()
         user_id = users.insert({
                 'email':email,
                 'password': password,
                 'created': created,
                 'confirmed':False,
                 'mconfirmed':False
                 })
         
        # token = s.dumps(email, salt='email-confirm')
         setm_value(email)
         token=jwt.encode({'email':email.encode(),"exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=10)},app.config['JWT_SECRET_KEY'])
         msg = Message('Confirm Email', sender='vadlasunilkumar225@gmail.com', recipients=[email])
         link = url_for('confirm_email', token=token, _external=True)
         msg.body = 'Your link is {}'.format(link)
         print("helllllllllll")
         print(token)
        #  range_start = 10**(10-1)
        #  range_end = (10**10)-1
        #  r=str(randint(range_start, range_end))
         r=str(randint(1000,9999))
         mail.send(msg)
         print("hold onnnnnnnnnnn")
         print(pnum)
         pnum="91"+pnum
         print("hold onnnnnnnnnnn")
         print(pnum)
         message_created = client.messages.create(
                 src='916302623509',
                 dst=pnum,
                 text=r)
         setr_value(r)
         result ="sucess"
         return result
@app.route('/users/otp',methods=["POST"])
def otp():
     OTP= request.get_json()['otp']
     users=mongo.db.newUsers
     res =globvar in OTP
     if(res):
        result="sucess"
        users.find_one_and_update({'email':globm},{"$set":{"mconfirmed":True}},upsert=False)
     else:
        result=jsonify({'result':'No results found'}),409
     return result

@app.route('/confirm_email/<token>')
def confirm_email(token):
    try:
         users=mongo.db.newUsers
         userdata=jwt.decode(token,app.config['JWT_SECRET_KEY'])
         print("heeeeeeeeeeeeeeeee")
         print(userdata)
         setm_value(userdata['email'].encode())
         print("emmmmmmmmmmmm")
         print(userdata['email'])
         if(userdata['email']):
             print("uffffffff")
            #  response=users.find_one({'email': userdata['email']})
            #  print("tusssssss")
            #  print(response)
            #  if(response):
            #     print("thoooooooooooooooo")
            #     print()
            #     response.update({"email":userdata['email'].encode()},{'$set':{"confirmed":True}})
             users.find_one_and_update({'email':userdata['email']},{"$set":{"confirmed":True}},upsert=False)   
             return "sucess"
         else : 
             return "false" 
    except Exception as E:
        return "JWT exception"
   
        

             
@app.route('/users/login',methods=["POST"])
def login():
    users=mongo.db.newUsers
    email= request.get_json()['email']
    password=request.get_json()['password']
    result= ""

    response = users.find_one({'email': email})
    print(response)
    if response:
        if(response['confirmed'] and response['mconfirmed'] ):
            if bcrypt.check_password_hash(response['password'],password):
                # access_token = create_access_token(identity={
                #     '_id' : response['_id']
                myToken=jwt.encode({'email':response['email'].encode()},app.config['JWT_SECRET_KEY'])
                result = jsonify({'token':myToken})
            else:
                result = jsonify({'error':'Invalid Username and Password'}),401
        else:
                result = jsonify({'error':'Not confirmation'}),400
    else:
        result= jsonify({'result':'No results found'}),404
    
    return result

def validaToken():
    token=request.headers.get('Authorization')
    print(token)
    test,token=token.split( )
    print(token)
    userdata= jwt.decode(token,app.config['JWT_SECRET_KEY'])
    print( userdata['email'].encode())
    return userdata['email'].encode()

@app.route('/userlist',methods=['GET'])
def get_all_tasks():
    users=mongo.db.newUsers
    result=[]
    for q in users.find():
        result.append({'_id':str(q['_id']),'email':q['email']})
    return jsonify(result)  

@app.route('/users/update',methods=['PUT'])
def update_task():
    email =  validaToken()
    if(email):
        print("Validated")
        users = mongo.db.newUsers
        first_name = request.get_json()['first_name']
        last_name=request.get_json()['last_name']
        contact_num=request.get_json()['contact_num']
        users.find_one_and_update({'email':email},{"$set":{"first_name":first_name}},upsert=False)
        users.find_one_and_update({'email':email},{"$set":{"last_name":last_name}},upsert=False)
        users.find_one_and_update({'email':email},{"$set":{"contact_num":contact_num}},upsert=False)
        new_task = users.find_one({'email':email})
        result="sucess"
    else:
        result="fail"
    return jsonify({"result":result})

@app.route('/users/delete',methods=['DELETE'])
def delete_task(): 
    email=validaToken()
    users=mongo.db.newUsers
    print("heeeeeeeeeellllllllllllllllll")
    print(email)
    response = users.find_one({'email': email})
    if(email):
        res= users.delete_one({'email':email})
        if(res):
            print("uuuuuuuuuuuuuuuuu")
            print(res)
            result="sucess"
        else:
            result ="fail",402
    return jsonify({'result':result})
if __name__ == '__main__':
    app.run(debug=True)



