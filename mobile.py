import plivo
from flask import Flask, jsonify, request, json, url_for, redirect
app = Flask(__name__)
auth_id = "MAOTLIMZFLOWFHZMQWNT"
auth_token = "YTcxNDg5MzgwZWJmNTQyMDE5ZjE5OWUxNWFkNjI5"
client = plivo.RestClient(auth_id='MAOTLIMZFLOWFHZMQWNT', auth_token='YTcxNDg5MzgwZWJmNTQyMDE5ZjE5OWUxNWFkNjI5')

message_created = client.messages.create(
    src='916302623509',
    dst='919177575115',
    text='1234'
)
if __name__ == '__main__':
    app.run(debug=True)
