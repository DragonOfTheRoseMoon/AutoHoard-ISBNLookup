import requests
import os
import re
from dotenv import load_dotenv
from formats import (Book)



class OLAPI:
    def __init__(self):
        load_dotenv()
        self.headers = {"User-Agent": os.getenv("HEADERS")}
        self.baseurl = "https://openlibrary.org"
    
#-----------------  housekeeping ---------------------------------------------------

    def get_author_info(self, authors_list):
        if not authors_list:
            return ""
        
        names = []
        for author in authors_list:
            key = author.get("key")
            if not key:
                continue
            url = f"{self.baseurl}{key}.json"
            try:
                resp = requests.get(url, headers=self.headers)
                resp.raise_for_status()
                data = resp.json()
                names.append(data.get("name", ""))
            except requests.RequestException:
                continue
        return ", ".join(names)

    def extract_year(self, date_str):
        if not date_str:
            return ""
        match = re.search(r"\b(1[0-9]{3}|20[0-9]{2})\b", date_str)
        return match.group(0) if match else ""

#--------------------- calls --------------------------------------------------------

    def get_book_info_by_isbn(self, isbn):
        url = f"{self.baseurl}/isbn/{isbn}.json"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        data = response.json()

        title = data.get("title", "")
        publishers = data.get("publishers", [])
        if isinstance(publishers, list):
            publisher = ", ".join(
                p["name"] if isinstance(p, dict) else str(p)
                for p in publishers
            )
        else:
            publisher = str(publishers)
        publish_date = data.get("publish_date", "")
        year = self.extract_year(publish_date)
        pages = data.get("number_of_pages", 0)
        authors_list = data.get("authors", [])
        series = data.get("series", [])
        series_name = ", ".join(series) if isinstance(series, list) else str(series)


        return Book(
            isbn=isbn,
            title=title,
            authors=self.get_author_info(authors_list),
            series = series_name,
            publisher=publisher,
            publish_year=year,
            pages=pages
        )



def main():

    ol = OLAPI()
    isbn = "0786918047" 
    Book = ol.get_book_info_by_isbn(f"{isbn}")
    print(Book)

if __name__ == "__main__":
    main()