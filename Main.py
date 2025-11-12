import tkinter as tk
import tkinter.font as tkFont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from EventHandler import EventHandler

#================================================ Main Window ==============================================
def start_move(event):
    global x_offset, y_offset
    x_offset = event.x
    y_offset = event.y

def stop_move(event):
    global x_offset, y_offset
    x_offset = None
    y_offset = None

def on_move(event):
    x = event.x_root - x_offset
    y = event.y_root - y_offset
    root.geometry(f"+{x}+{y}")

root = ttk.Window(themename="vapor")
root.overrideredirect(True)  # Hide OS frame
root.geometry("800x480")
root.configure(bg="#000000")  # Background color

ICON_FILE = "images/app_icon.ico"
try:
    root.iconbitmap(ICON_FILE) 
except tk.TclError:
    print(f"Warning: Could not load icon file '{ICON_FILE}'. Check if the file exists and is a valid .ico format.")

#================================================= Custom Title Bar =====================================================
title_bar = ttk.Frame(root, bootstyle="primary", height=30)
title_bar.pack(fill="x")

title_bar.bind("<ButtonPress-1>", start_move)
title_bar.bind("<ButtonRelease-1>", stop_move)
title_bar.bind("<B1-Motion>", on_move)

title_label = ttk.Label(title_bar, text="~AutoHoard~", bootstyle="inverse-primary")
title_label.pack(side="left", padx=10)

def close_window(event=None):
    root.destroy()
    
root.bind("<Escape>", close_window)

close_button = ttk.Button(title_bar, text="X", bootstyle=(DANGER, OUTLINE), command=close_window)
close_button.pack(side="right", padx=5, pady=2)

#================================================= Housekeeping =======================================================
header_font = tkFont.Font(family="Cousine", size=14, weight="bold")
sub_header_font = tkFont.Font(family="Cousine", size=8, weight="bold")
entry_font = tkFont.Font(family="Cousine", size=10)
status_font = tkFont.Font(family="Cousine", size=10, weight="bold")

#================================================= Overall Layout =====================================================

isbn_frame_title = ttk.Label(root, text="Enter or Scan ISBN", font=header_font, bootstyle=(SECONDARY, "bold"))
isbn_frame = ttk.Labelframe(root, labelwidget=isbn_frame_title, padding=10)
isbn_frame.pack(side=TOP, padx=10, pady=(10, 5), fill=X)

search_entry = ttk.Entry(isbn_frame, font=entry_font, bootstyle=PRIMARY)
search_entry.pack(pady=0, padx=2, fill=X)
search_entry.configure(justify="center")

book_info_frame_title = ttk.Label(root, text="Book Info", font=header_font, bootstyle=(SECONDARY, "bold"))
book_info_frame = ttk.Labelframe(root, labelwidget=book_info_frame_title, padding=10)
book_info_frame.pack(side=TOP, padx=10, pady=5, fill=X)

data_entry_button_frame = ttk.Frame(root, padding=10)
data_entry_button_frame.pack(side=TOP, padx=10, pady=10, fill=X)
data_entry_button_frame.columnconfigure(0, weight=1)
data_entry_button_frame.columnconfigure(3, weight=1)


search_status_label = ttk.Label(isbn_frame, text="", font=status_font, bootstyle=DANGER)
data_status_label = ttk.Label(data_entry_button_frame, text=" ", font=status_font, bootstyle=DANGER, anchor=CENTER)


#========================================= Book Info Entry Grid =============================================
for i in range(6):
    if i < 4:
        book_info_frame.columnconfigure(i, weight=2)
    else:
        book_info_frame.columnconfigure(i, weight=1)

#--------------------------- Field Labels

title_entry_label = ttk.Label(book_info_frame, text="Title", font=sub_header_font, bootstyle=INFO)
title_entry_label.grid(row=0, column=0, columnspan=4, sticky="w", padx=5, pady=2)

isbn_label = ttk.Label(book_info_frame, text="ISBN", font=sub_header_font, bootstyle=INFO)
isbn_label.grid(row=0, column=4, columnspan=2, sticky="w", padx=5, pady=2)

authors_label = ttk.Label(book_info_frame, text="Authors", font=sub_header_font, bootstyle=INFO)
authors_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=2)

publisher_label = ttk.Label(book_info_frame, text="Publisher", font=sub_header_font, bootstyle=INFO)
publisher_label.grid(row=2, column=2, columnspan=2, sticky="w", padx=5, pady=2)

publish_year_label = ttk.Label(book_info_frame, text="Year", font=sub_header_font, bootstyle=INFO)
publish_year_label.grid(row=2, column=4, sticky="w", padx=5, pady=2)

pages_label = ttk.Label(book_info_frame, text="Pages", font=sub_header_font, bootstyle=INFO)
pages_label.grid(row=2, column=5, sticky="w", padx=5, pady=2)


#--------------------------- Entry Fields

title_entry = ttk.Entry(book_info_frame, font=entry_font, bootstyle=PRIMARY, width=50)
title_entry.grid(row=1, column=0, columnspan=4, sticky="EW", padx=5, pady=2)
title_entry.configure(justify="left")

isbn_entry = ttk.Entry(book_info_frame, font=entry_font, bootstyle=PRIMARY, width=20)
isbn_entry.grid(row=1, column=4, columnspan=2, sticky="EW", padx=5, pady=2)
isbn_entry.configure(justify="left")

authors_entry = ttk.Entry(book_info_frame, font=entry_font, bootstyle=PRIMARY, width=30)
authors_entry.grid(row=3, column=0, columnspan=2, sticky="EW", padx=5, pady=2)
authors_entry.configure(justify="left")

publisher_entry = ttk.Entry(book_info_frame, font=entry_font, bootstyle=PRIMARY, width=25)
publisher_entry.grid(row=3, column=2, columnspan=2, sticky="EW", padx=5, pady=2)
publisher_entry.configure(justify="left")

publish_year_entry = ttk.Entry(book_info_frame, font=entry_font, bootstyle=PRIMARY, width=15)
publish_year_entry.grid(row=3, column=4, sticky="EW", padx=5, pady=2)
publish_year_entry.configure(justify="left")

pages_entry = ttk.Entry(book_info_frame, font=entry_font, bootstyle=PRIMARY, width=15)
pages_entry.grid(row=3, column=5, sticky="EW", padx=5, pady=2)
pages_entry.configure(justify="left")


#========================================= class initiation and functionality =============================================



handler = EventHandler(
    search_entry,
    title_entry,
    isbn_entry,
    authors_entry,
    publisher_entry,
    publish_year_entry,
    pages_entry,
    search_status_label,
    data_status_label
    )



search_button = ttk.Button(isbn_frame, text="Search", width=35, bootstyle=(PRIMARY, OUTLINE), command=lambda: handler.search_book_by_ISBN(handler.search_entry.get()))
search_button.pack(side=TOP, padx=5, pady=(18,5))

search_entry.bind(
    "<Return>",
    lambda event: handler.search_book_by_ISBN(search_entry.get())
    )

search_status_label.pack(side=TOP, padx=5, pady=(1,0))

confirm_button = ttk.Button(data_entry_button_frame, text="Confirm", width=35, bootstyle=(SUCCESS, OUTLINE), command=handler.add_to_db)
confirm_button.grid(row=0, column=1, sticky="ew", padx=5, pady=(15, 5))

clear_button = ttk.Button(data_entry_button_frame, text="Clear", width=35, bootstyle=(DANGER, OUTLINE), command=handler.clear_all_fields)
clear_button.grid(row=0, column=2, sticky="ew", padx=5, pady=(15, 5))


data_status_label.grid(row= 1, column=1,columnspan=2, sticky="EW")



#========================================== run ==================================================================



root.mainloop()
