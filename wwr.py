from bs4 import BeautifulSoup
import requests


def extract_wwr_jobs(term):
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={term}"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("section", class_="jobs")
        for job in jobs:
            company = job.find("span", class_="company")
            position = job.find("span", class_="title")
            location = job.find("span", class_="region")
            if company:
                company = company.string.strip()
            if position:
                position = position.string.strip()
            if location:
                location = location.string.strip()
            if company and position and location:
                job = {
                    'company': company,
                    'position': position,
                    'location': location
                }
                results.append(job)
    else:
        print("Can't get jobs.")
    return results
