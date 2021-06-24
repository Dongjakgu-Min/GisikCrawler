from bs4 import BeautifulSoup
import requests


def parse():
    response = requests.get('https://ssudorm.ssu.ac.kr:444/SShostel'
                            '/mall_main.php?viewform=B0001_foodboard_list&board_no=1')
    data = {}

    response.encoding = None
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        menu = soup.select_one('.boxstyle02 > tbody').find_all('td')
        date = soup.select_one('.boxstyle02 > tbody').find_all('th')

        for date in date:
            data[date.get_text().strip()] = []
        key = list(data.keys())

        for i in range(0, len(menu)):
            if i % 4 != 3:
                data[key[int(i / 4)]].append(menu[i].get_text().strip().split())
        return data

    else:
        return None
