from bs4 import BeautifulSoup
import requests
import time


def findjobs():

    html_response = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=flutter&txtLocation=").text

    # print(html_response)F

    soup = BeautifulSoup(html_response, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):  # for job in jobs:

        posted = job.find("span", class_="sim-posted").text

        if "few" in posted:
            skill_set = job.find(
                "span", class_="srp-skills").text.replace(" ", "")

            info_link = job.header.h2.a["href"]

            company_name = job.find(
                "h3", class_="joblist-comp-name").text.replace(" ", "")
            # print(company_name.text.replace(" ", ""))
            with open(f"posts/{index}.txt", "w") as f:

                # print(f"Company Name : {company_name.strip()}")
                f.write(f"Company Name : {company_name.strip()}\n")
                f.write(f"Skill Set: {skill_set.strip()}\n")
                f.write(f"More Info : {info_link}")

            print(f"File {index}.txt has been created.")


if __name__ == "__main__":
    while True:
        findjobs()
        time.sleep(100)
