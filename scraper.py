import requests
from bs4 import BeautifulSoup
from date_calc import get_date_lst

HEADERS = {
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
"Accept-Language" : "ko-KR,ko"
}

URL = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&"

URLS = {
    "POLITICS": URL + "sid1=100&sid2=269&date=",
    "ECONOMY" : URL + "sid1=101&sid2=263&date=",
    "SOCIETY" : URL + "sid1=102&sid2=257&date=",
    "TECH" : URL + "sid2=230&sid1=105&date="
}

# soup 객체 생성
def make_soup(url):
    res = requests.get(url, headers=HEADERS)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

# article container 추출(ul)
def extract_container(url):
    soup = make_soup(url)
    containers = soup.find("div", {"class": "list_body newsflash_body"}).find_all("ul")
    return containers

# container에서 각각의 article(ul) 추출
def extract_each_article(url, cg, date):
    containers = extract_container(url)
    newspaper_list = [
        "중앙일보", 
        "동아일보", 
        "조선일보", 
        "한겨례", 
        "경향신문"
        ]
    result = []
    for container in containers:
        ul = container.find_all("dl")
        
        for each in ul:
            newspaper = each.find("span", {"class": "writing"}).text.strip()
            if not(newspaper in newspaper_list):
                continue
            title = each.find_all("dt")[-1].text.strip()
            link = each.find("a")["href"]
            result.append({
                "date" : date,
                "category" : cg,
                "title" : title,
                "newspaper" : newspaper,
                "link" : link
            })
    return result

# 마지막 page 찾음
def find_last_page(url):
    soup = make_soup(url)
    next_page = soup.find("div", {"class": "paging"}).find_all("a")

    while True:
        if len(next_page) >= 10:
            next_url = "https://news.naver.com/main/list.naver" + next_page[-1]["href"]
            
            soup = make_soup(next_url)
            next_page = soup.find("div", {"class": "paging"}).find_all("a")
            continue
        else:
            try:
                last_page = int(next_page[-1].text)
            except:
                last_page = int(soup.find("div", {"class" : "paging"}).find("strong").text)
        return last_page

# 각 페이지에서 기사 추출(각 페이지에서 extract_each_article 실행)
def extract_each_page(url, cg, date):
    last_page = find_last_page(url)
    result = []
    for n in range(1, last_page + 1):
        print(f"Now scrapping page {n} / {last_page} in {cg}")
        new_url = url + "&page=" +str(n)
        page_result = extract_each_article(new_url, cg, date)
        result += page_result
    return result

# 사용자 입력 기간 동안의 기사 추출(각 날짜에서 extract_each_date 실행)

def extract_each_date(url, cg, sd, ed):
    date_lst = get_date_lst(sd, ed)
    result = []
    for date in date_lst:
        print(f"Now scraping {date} / {date_lst[-1]} in {cg}")
        new_url = url + date
        date_result = extract_each_page(new_url, cg, date)
        result += date_result
    return result

def extract_politics_section(sd, ed):
    url = URLS["POLITICS"]
    return extract_each_date(url, "정치", sd, ed)

def extract_economy_section(sd, ed):
    url = URLS["ECONOMY"]
    return extract_each_date(url, "경제", sd, ed)

def extract_society_section(sd, ed):
    url = URLS["SOCIETY"]
    return extract_each_date(url, "사회", sd, ed)

def extract_tech_section(sd, ed):
    url = URLS["TECH"]
    return extract_each_date(url, "IT", sd, ed)

def extract_article(sd, ed, cg):
    url = URLS[cg]
    return extract_each_date(url, cg, sd, ed)