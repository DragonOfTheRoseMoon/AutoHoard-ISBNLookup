import sqlite3
import os
from formats import Book


class DatabaseHandler:
    def __init__(self, db_path="BookHoard.db"):
        self.db_path = db_path
        self._db_check()
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def _db_check(self):
        if not os.path.exists(self.db_path):
            conn = sqlite3.connect(self.db_path)
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    isbn TEXT PRIMARY KEY,
                    title TEXT,
                    authors TEXT,
                    series TEXT DEFAULT "none",
                    publisher TEXT,
                    publish_year INTEGER DEFAULT 0,
                    pages INTEGER DEFAULT 0,
                    read TEXT DEFAULT "NO"
                )
            """)
            conn.commit()
            conn.close()


    def check_for_book_in_database(self, isbn):
        query = "SELECT 1 FROM books WHERE isbn = ? LIMIT 1;"
        self.cur.execute(query, (isbn,))
        result = self.cur.fetchone()
        return result is not None


    def add_book_to_database(self, data):
        query = """
            INSERT INTO books (isbn, title, authors, series, publisher, publish_year, pages)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """
        self.cur.execute(query, (
            data.isbn,
            data.title,
            data.authors,
            data.series,
            data.publisher,
            data.publish_year,
            data.pages
            ))
        self.conn.commit()

        double_check = self.check_for_book_in_database(data.isbn)
        if double_check == True:
            return True
        else:
            return False




#-----------------------------------------------------------------------------------------------------

def main():
    DBhandler = DatabaseHandler("BookHoard.db")
    data = Book(
        isbn=9780135166307,
        title="Effective Python",
        authors="Brett Slatkin",
        publisher="Pearson",
        publish_year=2020,
        pages=320
    )

    exists = DBhandler.check_for_book(data.isbn)
    print(f"the book exists? {exists}")
    add_a_book = DBhandler.add_book(data)
    print(f"was the book added? {add_a_book}")

if __name__ == "__main__":
    main()
