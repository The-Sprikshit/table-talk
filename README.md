# 🗂️ MySQL Site Info Manager with Python

## 📌 Project Overview

This project is a **command-line database manager** built using Python and MySQL. It allows users to **store, view, search, update, and delete** information about websites or digital resources in a **real-time, offline MySQL database** on your local system.

---

## 🛠️ Technologies Used

- Python
- MySQL (using PyMySQL connector)
- Command Line Interface (CLI)

---

## 🧠 Key Highlights

- 💾 **Real-Time Data Storage**  
  All inputs are stored immediately in your **offline MySQL database** without needing an internet connection.

- 🛡️ **Fully Local & Secure**  
  Data is managed entirely on your system, giving you complete control.

---

## 🎯 Features

- 🔧 **Initialize Database**  
  Automatically sets up a table (`Allnames`) if it doesn’t exist.

- 📝 **Add New Site**  
  Save any site’s name and its purpose to the local database.

- 🔍 **Search Functionality**  
  Search by either **site name** or **purpose** using keywords.

- 📋 **View All Names**  
  List all the site names you've entered.

- ✏️ **Update/Delete Records**  
  Modify existing records or delete them completely with ease.

- 🧠 **Interactive CLI**  
  Simple prompts guide the user through all available actions.

---

## 🧮 Table Schema

**Table Name**: `Allnames`  
| Column   | Type         | Description               |
|----------|--------------|---------------------------|
| name     | VARCHAR(255) | Name of the site/tool     |
| purpose  | TEXT         | Details or purpose of use |

---

## 🖥️ Real-Time Data Flow

- Data is added/updated **instantly** using SQL queries.
- MySQL acts as the local storage backend — **no external API or cloud**.
- Every operation (add/search/update/delete) is committed to the database **on the spot**.

---

## 🚀 How to Run

### 🧩 Prerequisites

- MySQL installed and running locally
- Python installed
- PyMySQL module:  
  `pip install pymysql`

### ▶️ Steps

1. Ensure your MySQL database `Sql_Project` exists (or the script will create the required table).
2. Run the Python script:  
   `python site_info_manager.py`
3. Follow the interactive prompts.

---

## ✅ Sample Use Cases

- Organize sites for learning, tools, or personal use
- Maintain a list of frequently visited platforms with their purpose
- Track internal URLs and tools for a project or organization

---

## 🧰 Future Improvements

- GUI using Tkinter or PyQt
- CSV import/export
- Multi-user support with login
- Enhanced data categories or tags

---

## 👨‍💻 Author

Developed by a BCA fresher passionate about building real-world Python + MySQL applications.  
🎓 Hands-on learning of database CRUD operations with real-time execution.

