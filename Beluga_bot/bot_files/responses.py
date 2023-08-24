# responses.py

import os

import requests

from dotenv import load_dotenv
load_dotenv()


def get_response(msg) -> str:
    msg = msg.lower()

    if msg == 'hello' or msg == 'hi' or msg == 'hii' :
        return 'Hello There!'
    
    # for jokes 
    url = "https://dad-jokes-by-api-ninjas.p.rapidapi.com/v1/dadjokes"
    headers = {
        "X-RapidAPI-Key": os.environ.get('API_KEY'),
        "X-RapidAPI-Host": "dad-jokes-by-api-ninjas.p.rapidapi.com"
    }


    if msg == 'joke':
        response = requests.get(url, headers=headers)
        return str( "Here is the Joke :- \n\n" +  response.json()[0]['joke'] )
    

    if msg == 'help':
        return '`Some of the commands :-\n.hello\n.joke`'
    
    return "I don't know! What do you mean...\ntry `.help`" 


