import requests
from bs4 import BeautifulSoup
#html에서 데이터를 추출하는데에는 beautifulsoup 사용
#find는 찾은 첫번째 값. find_all은 전부
LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div",{"class" : "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[0 : -1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_pages):
    jobs = []
    for page in range(last_pages):
        result = requests.get(f"{URL}start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("a", {"class": "job_seen_beacon"})
        for result in results: #result는 html 리스트
            title = (result.find("h2", {"class" : "jobTitle"}).find("a")["title"])
            company = result.finf("span", {"class": "company"})
            company_anchor= company.find("a")
            if company_anchor is not None:
                company = (str(company_anchor.string))
            else:
                company = (str(company.string))
            company = company.strip()  
            print(company)

            # title.find("span", title = True)은 title이 있는 span을 찾아라
        
        
    

