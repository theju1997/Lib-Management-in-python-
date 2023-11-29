import requests
from bs4 import BeautifulSoup
import openpyxl
import threading

# Function to fetch movie data for a given year
def fetch_movie_data(year, workbook):
    url = f'https://en.wikipedia.org/wiki/List_of_Bollywood_films_of_{year}'  # Replace with the appropriate URL
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract movie data from the webpage
        tables = soup.find_all('table', {'class': 'wikitable'})
        movie_data = []

        for table in tables:
            rows = table.find_all('tr')
            for row in rows[1:]:  # Skip the header row
                columns = row.find_all('td')
                if len(columns) >= 3:
                    title = columns[1].text.strip()
                    description = columns[2].text.strip()
                    movie_data.append([year, title, description])

        # Check if there's at least one visible sheet
        if not workbook.sheetnames:
            workbook.create_sheet()

        # Write data to Excel
        sheet = workbook.active
        for data in movie_data:
            sheet.append(data)
    else:
        print(f"Failed to fetch data for year {year}")

if __name__ == "__main__":
    workbook = openpyxl.Workbook()
    workbook.remove(workbook.active)  # Remove the default sheet

    years = range(2000, 2023)  # Modify this range as needed
    threads = []

    for year in years:
        thread = threading.Thread(target=fetch_movie_data, args=(year, workbook))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Save the data to an Excel file
    workbook.save('bollywood_movies.xlsx')
