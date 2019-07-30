import psycopg2 
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

    #print("{} {}".format(b, a))
    cur.execute("insert into all_currency(usd_client, usd_bank, euro_client, euro_bank, rub_client, rub_bank, date_time) \
    values(%s, %s, %s, %s, %s, %s, %s);", info)               
    #cur.execute("insert into all_currency(usd_client, usd_bank, euro_client, euro_bank, rub_client, rub_bank,date_time) \
    #values({d[0]},{d[1]},{d[2]},{d[3]},{d[4]},{d[5]},{e});".format(d = info, e = c))               
    #cur.execute("insert into all_currency(date_time) values(%s);",(c,))
    con.commit()
    
    print('record inserted successfully')
    
    con.close()