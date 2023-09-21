import os
from datetime import datetime
from pytz import timezone
from crawling import parsing_beautifulSoup, extract_data
from github_utils import get_github_repo, upload_github_issue

access_token = os.environ['ZIMMYRABBIT_TOKEN']
repository_name = "Github-Action-With-Python"

seoul_timezone = timezone('Asia/Seoul')
today = datetime.now(seoul_timezone)
today_data = today.strftime("%Y년 %m월 %d일")

yes24_new_product_url = "http://www.yes24.com/24/Category/NewProductList/001001003?sumGb=01"


if __name__ == "__main__":
    soup = parsing_beautifulSoup(yes24_new_product_url)
    issue_title = f"YES24 IT 신간 도서 알림({today_data})"
    #issue_title = f"YES24 IT 신간 도서 알림()"
    upload_contents = extract_data(soup)
    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")
