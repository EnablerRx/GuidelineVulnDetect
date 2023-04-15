import requests
import logging
import re
from urllib.parse import urljoin
import json
from os import makedirs
from os.path import exists
import time

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

INDEX_URL = 'https://paperswithcode.com/api/v0/proceeding_pgrs/?tasks=&authors=&order_by=title&page_number={page}&proceeding_slug=naacl-2019-6'
#INDEX_URL = 'https://paperswithcode.com/api/v0/proceeding_pgrs/?tasks=&authors=&order_by=title&page_number=2&proceeding_slug=acl-2022-5'
BASE_URL = 'https://paperswithcode.com'
 
def scrape_api(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)
    except:
       print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')
       time.sleep(3)
       time.sleep(3)



def scrape_index(page):
    url = INDEX_URL.format(page = page)
    return scrape_api(url)


def scrape_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)
    except:
       print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')
       time.sleep(3)
       time.sleep(3)




def parse_pdf(html):
    #print(html)
    pattern = re.compile('<a href="(https://arxiv.org/pdf/.*?.pdf)"')
    pdf_items = re.findall(pattern, html)
    if not pdf_items:
        pattern_2 = re.compile('<a href="(.*?.pdf)')
        pdf_items = re.findall(pattern_2, html)
        if not pdf_items:
            return[]
    print(pdf_items[0])
    return pdf_items[0]

def downloadPDF(url, title):
    #get请求
    try:
        pdf = open(str(title)+'.pdf','wb')
        res = requests.get(url)
        for chunk in res.iter_content(100000):
            pdf.write(chunk)
        pdf.close()
    except requests.exceptions.ConnectionError:
       print('ConnectionError -- please wait 3 seconds')
       time.sleep(3)
    except requests.exceptions.ChunkedEncodingError:
       print('ChunkedEncodingError -- please wait 3 seconds')
       time.sleep(3)    
    except:
       print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')
       time.sleep(3)
       time.sleep(3)



PAGE = 80


def main():
    for page in range(1, PAGE+1):
        index_data = scrape_index(page)
        # print(index_data)
        for i in index_data.get('data'):
            paper = i.get('paper')
            #print(paper)
            j = paper.get('link')
            title = paper.get('title')
            #id = paper.get('id')
            print(title)
            title_1 = title.replace('\\',' ')
            title_2 = title_1.replace('/',' ')
            title_3 = title_2.replace(':',' ')
            title_4 = title_3.replace('*',' ')
            title_5 = title_4.replace('?',' ')
            title_6 = title_5.replace('"',' ')
            title_7 = title_6.replace('<',' ')
            title_8 = title_7.replace('>',' ')
            title_9 = title_8.replace('|',' ')

            detail_url = urljoin(BASE_URL, j)
            #print(detail_url)
            html = scrape_page(detail_url)
            pdf_url = parse_pdf(html)
            downloadPDF(pdf_url, title_9)

        

if __name__ == '__main__':
    main()
