import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w", encoding = "utf-8") #mode w: write 
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"]) #첫줄 작성
    for job in jobs:
        writer.writerow(list(job.values()))
    return 
