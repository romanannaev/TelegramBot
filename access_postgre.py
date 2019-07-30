import psycopg2
from datetime import datetime 
def insert_table(info):
    """insert total_kurs in table"""

    con = psycopg2.connect(
    database = 'postgres',
    user = 'postgres',
    password = '20021992',
    host = '127.0.0.1',
    port = '5432'
    )
    
    print ('database opened successufully')

    cur = con.cursor()
    dt = datetime.now()
    cur.execute('insert into all_currency(usd_client, usd_bank, euro_client, euro_bank, rub_client, rub_bank, data_time) \
    values(%s,%s,%s,%s,%s,%s,)', info)
    
    con.commit()
    
    print('record inserted successfully')
    
    con.close()