import requests as rq
import urllib3
from bs4 import BeautifulSoup
from pprint import pprint

import utils


def main():
    # logger = utils.logger.getLogger('log1.log')

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


    # soup = BeautifulSoup(doc_html, 'html.parser')
    trs = soup.find_all("tr", class_="tr-i")
    for tr in trs:
        # import pdb; pdb.set_trace()
        tds = tr.find_all("td")
        print(tr.find_all("td")[0].span.text)
        print(tr.find_all('td')[0].find_all('div',class_='small')[0].text.strip())
        print(tr.fin)
        break




if __name__ == "__main__":
    main()
