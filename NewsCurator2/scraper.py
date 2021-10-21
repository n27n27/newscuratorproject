import requests
from bs4 import BeautifulSoup

class NewsScraper():

    def __init__(self):        

        self.HEADERS = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "Accept-Language" : "ko-KR,ko"
        }

        self.URL = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&"

        self.URLS = {
            "POLITICS": self.URL + "sid1=100&sid2=269&date=",
            "ECONOMY" : self.URL + "sid1=101&sid2=263&date=",
            "SOCIETY" : self.URL + "sid1=102&sid2=257&date=",
            "TECH" : self.URL + "sid2=230&sid1=105&date="
        }

    # soup 객체 생성
    def makeSoup(self, url):
        
        res = requests.get(url, headers=self.HEADERS)
        res.raise_for_status()

        self.soup = BeautifulSoup(res.text, 'html.parser')
        return self.soup

    # article container 추출(ul)
    def extract_container(self):
        self.soup = self.makeSoup()
        self.containers = self.soup.find("div", {"class": "list_body newsflash_body"}).find_all("ul")
        return self.containers

    # container에서 각각의 article(ul) 추출
    def extract_each_article(self):
        self.containers = self.extract_container()
        self.newspaper_list = [
            "중앙일보", 
            "동아일보", 
            "조선일보", 
            "한겨례", 
            "경향신문"
            ]
        self.result = []
        for container in self.containers:
            ul = container.find_all("dl")
            
            for each in ul:
                newspaper = each.find("span", {"class": "writing"}).text.strip()
                if not(newspaper in self.newspaper_list):
                    continue
                title = each.find_all("dt")[-1].text.strip()
                link = each.find("a")["href"]
                self.result.append({
                    # "date" : date,
                    # "category" : cg,
                    "title" : title,
                    "newspaper" : newspaper,
                    "link" : link
                })

        return self.result

    # 마지막 page 찾음
    def find_last_page(self, url):
        soup = self.makeSoup(url)
        next_page = soup.find("div", {"class": "paging"}).find_all("a")

        while True:
            if len(next_page) >= 10:
                next_url = "https://news.naver.com/main/list.naver" + next_page[-1]["href"]
                
                soup = self.makeSoup(next_url)
                next_page = soup.find("div", {"class": "paging"}).find_all("a")
                continue
            else:
                try:
                    self.last_page = int(next_page[-1].text)
                except:
                    self.last_page = int(soup.find("div", {"class" : "paging"}).find("strong").text)
            return self.last_page

    # 각 페이지에서 기사 추출(각 페이지에서 extract_each_article 실행)
    def extract_each_page(self, url, cg, date):
        last_page = self.find_last_page(url)
        self.result = []
        for n in range(1, last_page + 1):
            print(f"Now scrapping page {n} / {last_page} in {cg}")
            new_url = url + "&page=" +str(n)
            page_result = self.extract_each_article(new_url, cg, date)
            self.result += page_result
        return self.result   

    # 사용자 입력 기간 동안의 기사 추출(각 날짜에서 extract_each_date 실행)

    def extract_each_date(self, url, cg, sd, ed):
        date_lst = self.get_date_lst(sd, ed)
        self.result = []
        for date in date_lst:
            print(f"Now scraping {date} / {date_lst[-1]} in {cg}")
            new_url = url + date
            date_result = self.extract_each_page(new_url, cg, date)
            self.result += date_result
        return self.result

    def extract_politics_section(self, sd, ed):
        url = self.URLS["POLITICS"]
        return self.extract_each_date(url, "정치", sd, ed)

    def extract_economy_section(self, sd, ed):
        url = self.URLS["ECONOMY"]
        return self.extract_each_date(url, "경제", sd, ed)

    def extract_society_section(self, sd, ed):
        url = self.URLS["SOCIETY"]
        return self.extract_each_date(url, "사회", sd, ed)

    def extract_tech_section(self, sd, ed):
        url = self.URLS["TECH"]
        return self.extract_each_date(url, "IT", sd, ed)    

    def extract_article(self, sd, ed, cg):
        self.url = self.URLS[cg]
        return self.extract_each_date(self.url, cg, sd, ed)

    
    politics_result = extract_politics_section("2021109", "20211010")
    economy_result = extract_economy_section("20211009", "20211010")
    society_result = extract_society_section("20211009", "20211010")
    tech_result = extract_tech_section("20211009", "20211010")
    all_result = politics_result + economy_result + society_result + tech_result



    def apply_temrs(self, cgs, newspapers, word):    

        showing_result = []
        for cg, newspaper in zip(cgs, newspapers):
            for result in self.all_result:
                if result["category"] == cg:
                    showing_result.append(result)
        print(showing_result)
        print("======================================================================================================")
        for newspaper in newspapers:
            for result in showing_result:
                if result["newspaper"] != newspaper:
                    showing_result.remove(result)
        print(showing_result)            
        if word is not None:
            for result in showing_result:
                if not(word in result["title"]):
                    showing_result.remove(result)
        return showing_result

news1 = NewsScraper()
news1.makeSoup()
news1.extract_container()
print(news1.extract_each_article())