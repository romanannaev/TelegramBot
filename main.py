import requests
from bs4 import BeautifulSoup
import re
#from access_postgre import insert_table
from datetime import datetime
from access_postgre import insert_table

def get_response(url):
    """create object soup"""

    response = requests.get(url)
    return response.text


def get_total_info(html):
    """parsing site"""

    soup = BeautifulSoup(html, 'lxml')

    regexp = r'\d{1}'  
    kurs = soup.find('tbody').find('tr').find_all(text = re.compile(regexp))
    #total_kurs = [i.__str__().replace('td', '').replace('>', '').replace('<', '').replace('/', '') for i in kurs]
    
    return kurs

def main_select():
    """local hub functions"""

    url = 'https://select.by/kurs/'
    
    total_gen = get_total_info(get_response(url))
    # b = datetime.today().strftime("%d.%m.%Y")
    # a = datetime.today().strftime("%H:%M:%S")
    # c = "{} {}".format(b, a)
    # info_postgre = []
    # for i in total_gen:
    #     info_postgre.append(i)
    # info_postgre.append(c)

    # insert_table(info_postgre)
    return total_gen
    

if __name__ == "__main__":
    main_select()