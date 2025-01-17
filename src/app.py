from flask import Flask, jsonify
from dotenv import load_dotenv 
from routes.auth import routes_auth
from routes.user_github import users_github
load_dotenv()

app = Flask(__name__) 

app.register_blueprint(routes_auth, url_prefix='/api')
app.register_blueprint(users_github, url_prefix='/api')

@app.route('/', methods=['GET'])
def index ():
    return jsonify({'message':'Welcome to FLASK TO JWT API'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 
    