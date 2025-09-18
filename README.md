# 📚 Online Library Management System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)  
[![Supabase](https://img.shields.io/badge/Backend-Supabase-green)](https://supabase.com/)  
[![Postgres](https://img.shields.io/badge/Database-PostgreSQL-blue)](https://www.postgresql.org/)  

---

## 📌 Problem Statement

This project demonstrates how to build a **real-world Library Management System** using Python and Supabase/Postgres.  
It simulates actual library operations like managing members, handling books, processing borrowing and returns, and generating reports.  

### Requirements:
- Create tables for **Members, Books, and Borrow Records** in Postgres  
- Implement **CRUD operations**:  
  - Register new members  
  - Add, update, search, and delete books  
  - Borrow/return books with stock checks  
- Implement **safe transactions** for borrowing/returning  
- Generate useful reports (overdue books, most borrowed books)  
- Only allow deletion if constraints are met (e.g., no borrowed books)  

---

## 🚀 Features

- 👥 **Member Management** – add, update, delete, and view members  
- 📖 **Book Management** – add, update, search, list, and delete books  
- 🔄 **Borrow & Return** – borrow books with availability checks and return them  
- 📊 **Reports** – view overdue books & most borrowed books  
- 🗄 **Supabase/Postgres Database** – persistent relational data storage  
- 🖥 **Command-Line Interface (CLI)** – menu-driven system for easy interaction  


---

# 🛠 How to Run

clone_repo: |
  git clone https://github.com/AnveshAnnepaga/online-library-system.git
  cd online-library-system

create_virtual_environment: |
  python -m venv venv
  # On macOS/Linux:
  source venv/bin/activate
  # On Windows:
  venv\Scripts\activate

install_dependencies: |
  pip install -r requirements.txt

set_env_variables: |
  # Create a .env file in the project root
  # Add your Supabase credentials as per .env.example

run_application: |
  python main.py


🖥 CLI Menu

1. Add Member
2. Update Member
3. Delete Member
4. List Members
5. Add Book
6. Update Book
7. Delete Book
8. List Books
9. Search Books
10. Borrow Book
11. Return Book
12. Overdue Books
13. Exit

