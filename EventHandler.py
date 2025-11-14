from OL_Data_Pull import OLAPI
from formats import Book
from DatabaseHandler import DatabaseHandler


class EventHandler():

    def __init__(self, search_entry, title_entry, series_entry, isbn_entry, authors_entry, publisher_entry,\
                publish_year_entry, pages_entry, search_status_label, data_status_label):
        self.search_entry = search_entry
        self.title_entry = title_entry
        self.series_entry = series_entry
        self.isbn_entry = isbn_entry
        self.authors_entry = authors_entry
        self.publisher_entry = publisher_entry
        self.publish_year_entry = publish_year_entry
        self.pages_entry = pages_entry
        self.search_status_label = search_status_label
        self.data_status_label = data_status_label
        
        self.olapi = OLAPI()
        self.DBHandler = DatabaseHandler("BookHoard.db")


    def gather_field_data(self):
        title_text = self.title_entry.get()
        series_text = self.series_entry.get()
        isbn_text = self.isbn_entry.get()
        authors_text = self.authors_entry.get()
        publisher_text = self.publisher_entry.get()
        publish_year_text = self.publish_year_entry.get()
        pages_text = self.pages_entry.get()

        return Book(
        isbn=isbn_text,
        title=title_text,
        authors=authors_text,
        series= series_text,
        publisher=publisher_text,
        publish_year=publish_year_text,
        pages=pages_text
        )



    def update_search_status(self, msg, style):
        self.search_status_label.config(text=msg, bootstyle=style) 
        #later use: self.update_search_status("Message Goes Here")


    def update_data_status(self, msg, style):
        self.data_status_label.config(text=msg, bootstyle=style)
        #later use: self.update_data_status("Message Goes Here")

    def clear_all_fields(self):
        self.search_entry.delete(0, "end")
        self.title_entry.delete(0, "end")
        self.series_entry.delete(0, "end")
        self.isbn_entry.delete(0, "end")
        self.authors_entry.delete(0, "end")
        self.publisher_entry.delete(0, "end")
        self.publish_year_entry.delete(0, "end")
        self.pages_entry.delete(0, "end")
        self.update_search_status("", style="")
        self.update_data_status("All fields cleared!", style="SUCCESS")
        return 

    def search_book_by_ISBN(self, isbn):
        
        def is_valid_isbn(isbn):
            isbn = isbn.strip().upper()
            if len(isbn) == 10:
                return isbn[:9].isdigit() and (isbn[9].isdigit() or isbn[9] == 'X')
            elif len(isbn) == 13:
                return isbn.isdigit()
            return False
        
        self.clear_all_fields()
        self.update_data_status("", style="")
        isbn = isbn.strip().upper()

        if not is_valid_isbn(isbn):
            self.update_search_status("Invalid ISBN: Must be 10 or 13 characters", style="DANGER")
            return
        
        try:
            book = self.olapi.get_book_info_by_isbn(isbn)
        except Exception as e:
            self.update_search_status(f"Error fetching book: {e}", style="DANGER")
            return

        if book:
            self.title_entry.insert(0, book.title)
            self.series_entry.insert(0, book.series)
            self.isbn_entry.insert(0, str(book.isbn))
            self.authors_entry.insert(0, book.authors)
            self.publisher_entry.insert(0, book.publisher)
            self.publish_year_entry.insert(0, str(book.publish_year))
            self.pages_entry.insert(0, str(book.pages))

            self.update_search_status("Book found!", style="SUCCESS")
        else:
            self.update_search_status("No book found.", style="DANGER")
            
        
    def add_to_db(self):
        data = self.gather_field_data()

        if data:
            check = self.DBHandler.check_for_book_in_database(data.isbn)
            if not check:
                add_book = self.DBHandler.add_book_to_database(data)
                if add_book:
                    self.clear_all_fields()
                    self.update_search_status("", style="")
                    self.update_data_status("Book added to database!", style="SUCCESS")
                    return
                else:
                    self.update_data_status("Book could not be added to database!", style="DANGER")
                    self.update_search_status("", style="")
                    return
            else:
                self.update_data_status("Book ISBN information already in the database!", style="DANGER")
                self.update_search_status("", style="")
                return
        else:
            self.update_data_status("Unable to get data from fields!", style="DANGER")
            self.update_search_status("", style="")
            return