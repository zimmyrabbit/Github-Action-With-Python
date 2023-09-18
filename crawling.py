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

# URL을 지정합니다.
url = 'https://www.yes24.com/24/Category/NewProductList/001001003?sumGb=01'  # 원하는 웹 페이지의 URL로 바꾸세요.

# parsing_beautifulSoup 함수 호출
soup = parsing_beautifulSoup(url)

# 반환된 BeautifulSoup 객체를 사용하여 원하는 데이터를 추출할 수 있습니다.
extracted_data = extract_data(soup)

# 추출된 데이터 출력
print(extracted_data)