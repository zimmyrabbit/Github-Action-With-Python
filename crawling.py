import requests
from bs4 import BeautifulSoup

print('dd')

def parsing_beautifulSoup(url):

    data = requests.get(url)

    html = data.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def extract_data(soup):

    upload_contents = ''
    new_items = soup.select(".goodsTxtInfo")
    url_prefix = "http://www.yes24.com"

    for new_item in new_items :
        item_name = new_item.select("a")[0].text
        url_suffix = new_item.select("a")[1].attrs['href']
        url = url_prefix + url_suffix
        price = new_item.select(".priceB")[0].text

        content = f"<a href={url}" + item_name + "</a>" + ", " + price + "<br/>\n"
        upload_contents += content
    
    return upload_contents