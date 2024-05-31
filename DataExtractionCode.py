from bs4 import BeautifulSoup
import requests
import csv

url='https://www.imdb.com/chart/top/?ref_=nv_mv_250'

headers={"USER_AGENT" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
response= requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

movies = soup.find_all('li', class_="ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent")


csv_filename = "Dataset.csv"

with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
    writer=csv.writer(file)

    header = ['Rank', 'Movie name','Year Of Release','Duration','Rating']
    writer.writerow(header)


    for movie in movies:
        name = movie.find('div',class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title").a.text.split('.')[1]
        rank = movie.find('div',class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title").a.text.split('.')[0]
        year = movie.find('span',class_="sc-b189961a-8 kLaxqf cli-title-metadata-item").text
        yearspan = movie.find('span',class_="sc-b189961a-8 kLaxqf cli-title-metadata-item")
        durationspan = yearspan.find_next_sibling('span',class_="sc-b189961a-8 kLaxqf cli-title-metadata-item") if yearspan else None
        duration = durationspan.text.strip() if durationspan else None 
        rating = movie.find('div',class_="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP cli-ratings-container").span.text
        
        writer.writerow([rank, name, year, duration, rating])

print("csv file has been created successfully", csv_filename)


