from flask import Blueprint, request
from requests import get 
from function_jwt import validate_token 

users_github= Blueprint('users_github', __name__)

@users_github.before_request

def verify_token_middleware():
    token = request.headers['Authorization'].split()[1]
    return validate_token(token, output=False)

@users_github.route('/github/user', methods=['POST'])
def user_github():
    data = request.get_json()
    token = data['token'] 
    country = data['country']
    
    response = get('https://api.github.com/search/users?q=location:{}'.format(country))
    
    return response.json()
    