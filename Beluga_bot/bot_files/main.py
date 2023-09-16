# main.py

import os
import bot 
import psycopg2

from dotenv import load_dotenv
load_dotenv()

try:
    conn = psycopg2.connect(
                host = os.environ.get('DB_HOSTNAME'),
                dbname = os.environ.get('DB_DATABASE'),
                user = os.environ.get('DB_USERNAME'),
                password = os.environ.get('DB_PASSWORD'),
                port = os.environ.get('DB_PORT'))

    create_table = '''
        CREATE TABLE IF NOT EXISTS data(
            name VARCHAR(20) NOT NULL,
            datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            today TEXT,
            yesterday TEXT,
            blockers TEXT
        )
    '''

    curr = conn.cursor()
    curr.execute(create_table)
    conn.commit()   
    curr.close()
except (Exception, psycopg2.Error) as error:
    print("Error:", error)
finally:
    if conn:
        conn.close()
if __name__ == '__main__':
    bot.run_bot()
