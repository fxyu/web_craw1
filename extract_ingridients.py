import requests as rq
import urllib3
from bs4 import BeautifulSoup
from pprint import pprint

import utils

import pickle
import json
import string


def main():
    class App(dict):
        def __str__(self):
            return json.dumps(self)

    # logger = utils.logger.getLogger('log1.log')
    baseUrl = "http://www.cosdna.com"
    url = "http://www.cosdna.com/cht/cosmetic_18cf249693.html" # KIEHL'S (契爾氏) 亞馬遜白泥淨膚面膜RARE EARTH DEEP PORE CLEANSING MASQUE
    # response = rq.get(url) # 用 requests 的 get 方法把網頁抓下來
    # html_doc = response.text # text 屬性就是 html 檔案

    http = urllib3.PoolManager()
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
    # header variable
    headers = { 'User-Agent' : user_agent }

    # creating request
    req = http.request('GET',url,headers=headers)
    soup = BeautifulSoup(req.data.decode('utf-8'), "lxml") # 指定 lxml 作為解析器
    # print(soup.prettify()) # 把排版後的 html 印出來


    items = []

    # soup = BeautifulSoup(doc_html, 'html.parser')
    trs = soup.find_all("tr", class_="tr-i")
    for tr in trs:
        # import pdb; pdb.set_trace()
        tds = tr.find_all("td")
        item = {
            'engName' : tds[0].find('span',class_='colors').text.strip(),
            'chtName' : tds[0].find_all('div',class_='small')[0].text.strip(),
            'shortDesc': tds[1].text.strip(),
            'acne' : checkEmtpy(tds[2].a.text.strip()), 
            'irritant' : checkEmtpy(tds[3].a.text.strip()),
            'Safety' : [span.text for span in tds[4].find_all('span')],
            'link' : tds[0].a['href'],
        }

        # Enter detail website
        details = http.request('GET',baseUrl+item['link'],headers=headers)
        soup_details = BeautifulSoup(details.data.decode('utf-8'), "lxml")

        # import pdb; pdb.set_trace()
        details_dec = {
            'altName' : soup_details.find('div',class_='mb-2').text.translate({ord(c): None for c in string.whitespace}),
            'desc' : soup_details.find('div',class_='linkb1').text.strip(),
            'moleWeight' : checkEmtpy(soup_details.find_all('span',class_='badge-light')[0].text.split('：')[-1]),
            'CasNo' : checkEmtpy(soup_details.find_all('span',class_='badge-light')[2].text.split('：')[-1]),
            'source' : checkEmtpy(soup_details.find('div',class_='text-muted').text),
        }

        item = {**item, **details_dec}

        # pprint(item)
        print(f'done { item["chtName"] }')
        items += [App(item)]

    ## to json    
    # items_json = App(items)

    ## Save to file
    with open('example.txt','w+') as file:
        json.dump(items, file)

def checkEmtpy(sinput):
    if sinput == '':
        return None
    return sinput

if __name__ == "__main__":
    main()
