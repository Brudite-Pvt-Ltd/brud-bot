# responses.py

import os
import sqlite3
import requests
import datetime
import psycopg2

from dotenv import load_dotenv
load_dotenv()

def get_response(msg, username) -> str:
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
    
    if msg == 'standup-format':
        return '`.standup\ntoday\n---your answer---\nyesterday\n---your answer---\nblockers\n---your answer---`'

    if msg == 'goodwords':
        return "BSDK MC BKL MKJ Gan*u Tatto ke Saudagar"

    if msg == 'generate_report':
        try:
            conn = psycopg2.connect(
                    host = os.environ.get('DB_HOSTNAME'),
                    dbname = os.environ.get('DB_DATABASE'),
                    user = os.environ.get('DB_USERNAME'),
                    password = os.environ.get('DB_PASSWORD'),
                    port = os.environ.get('DB_PORT'))

            get_record = '''
                SELECT name, datetime, today, yesterday, blockers
                FROM data
                WHERE datetime::date = %s
            '''

            today_date = datetime.date.today()
            formatted_date = today_date.strftime("%Y-%m-%d")
            print("Formatted Today:", formatted_date)

            curr = conn.cursor()
            curr.execute(get_record, (formatted_date,  ))
            records = curr.fetchall()

            for record in records:
                print(record)

            conn.commit()
            curr.close()
        except (Exception, psycopg2.Error) as error:
            print("Error:", error)
        finally:
            if conn:
                conn.close()

        path = os.path.dirname(__file__) + '\\bot_data'
        if os.path.isdir(path) == False:
            os.mkdir(path)



        return "File generated"

    new_msg = msg.split('\n')
    if new_msg[0] == 'standup':
        map = { 'today' : '', 'yesterday' : '', 'blockers' : ''}
        new_msg = new_msg[::-1]
        
        ans = ''
        for it in new_msg:
            # removing the wide spaces from starting and ending...
            it = it.strip()
            if it == 'yesterday' or it == 'blockers' or it == 'today':
                if ans != '':
                    map[it] = ans[:-2]
                ans = ''
            else:
                if it != '' :
                    ans += it + ', '

        if map['today'] or map['yesterday'] or map['blockers']:
            
            data = (
                username,
                str(datetime.datetime.now()),
                map['today'],
                map['yesterday'],
                map['blockers']
            )

            ### to store the data into database
            try:
                conn = psycopg2.connect(
                        host = os.environ.get('DB_HOSTNAME'),
                        dbname = os.environ.get('DB_DATABASE'),
                        user = os.environ.get('DB_USERNAME'),
                        password = os.environ.get('DB_PASSWORD'),
                        port = os.environ.get('DB_PORT'))

                curr = conn.cursor()
                curr.execute("INSERT INTO data VALUES (%s, %s, %s, %s, %s)", data)
                conn.commit()
                curr.close()
            except (Exception, psycopg2.Error) as error:
                print("Error:", error)
            finally:
                if conn:
                    conn.close()
            
            return "Thank for updates"
        else:
            return "Stand up is not correct"

    return "I don't know! What do you mean...\ntry `.help`" 


