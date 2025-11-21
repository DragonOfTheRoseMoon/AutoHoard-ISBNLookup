# AutoHoard

![AutoHoard GUI](https://raw.githubusercontent.com/DragonOfTheRoseMoon/AutoHoard-ISBNLookup/main/images/AutoHoardGUI.PNG)

AutoHoard is a Python application that lets you quickly look up books by ISBN using the OpenLibrary API, review or edit the retrieved details, and store them in a local SQLite3 database. It provides a clean Tkinter/TkBootstrap GUI for easy data entry and management.

---

## 🚀 Features

* **ISBN Lookup** via OpenLibrary API
* **Editable Book Details** before committing to the database
* Ability to use manual entry or a usb barcode scanner to input books more rapidly
* **SQLite3 Database Storage** for saved books
* **Tkinter + TkBootstrap GUI** for a polished interface
* **Dataclass-based Book Model** keeping code clean and structured

![AutoHoard Spec](https://raw.githubusercontent.com/DragonOfTheRoseMoon/AutoHoard-ISBNLookup/main/images/AutoHoard-Spec.PNG)

---

## 🛠️ Tech Stack

* **Python 3.x**
* **requests** – API calls
* **tkinter** – GUI
* **ttkbootstrap** – themed widgets
* **SQLite3** – local database
* **dataclasses** – data modeling

---

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AutoHoard.git
cd AutoHoard
```

### 2. Install dependencies

Make sure you have Python 3 installed.

```bash
pip install -r requirements.txt
```

### 3. Create your `.env` file

AutoHoard requires a user agent header for OpenLibrary API compliance.

Create a `.env` file in the project root:

```env
HEADER="AutoHoard/1.0 (myemail@example.com)"
```

Replace the email with your actual contact email (OpenLibrary requires this for responsible API usage).

---

## ▶️ Running AutoHoard

```bash
python main.py
```

After launching, enter an ISBN into the GUI, fetch the book information, make any necessary edits, and save it to your database. Using a barcode scanner, make sure to focus the ISBN search field and then pressing enter or scanning the barcode with scanner will automatically search. You may also press escape to quickly close the program.

---

## 🗃️ Database

AutoHoard uses a local SQLite3 database file. Data is created upon running the program and will automatically set up the Books table. Table contains ISBN as a primary key, Title, Authors, Series, Publisher, Publish_Year, Pages, and Read defaulting to no. the Read collumn is intended for future proofing for use later for tracking if you have read the book or not through a seperate interface that can connect to this database.

---

## 📚 OpenLibrary API Usage

This project uses the **OpenLibrary Books API**. The required header ensures proper identification:

```
"AutoHoard/1.0 (your-email@example.com)"
```

For documentation: [https://openlibrary.org/dev/docs/api/books](https://openlibrary.org/dev/docs/api/books)

---

## 📜 License

MIT License — free to use, modify, and distribute.

---

## 💡 Future Ideas

* Upgade to Postgre database
* Expand to other forms of API usage for UPC as well

---

Enjoy hoarding your books responsibly! 📚✨
