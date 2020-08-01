from page1 import doc_html
from bs4 import BeautifulSoup
from pprint import pprint

def main():
    soup = BeautifulSoup(doc_html, 'html.parser')
    trs = soup.find_all("tr", class_="tr-i")
    for tr in trs:
        print(tr.find_all("td")[0].text)



if __name__ == "__main__":
    main()