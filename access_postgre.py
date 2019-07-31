import psycopg2 
from data_bd import access
def insert_table(info):
    """insert total_kurs in table"""

    con = access
    
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

def select_info(info_date):
    con = access
    print('opened bd successfully')
    cur = con.cursor()
    cur.execute("select * from all_currency where date_time >= %s:: date;", (info_date,))
    rec = cur.fetchall()
    print('select from bd successfully ')
    con.close()
    return rec