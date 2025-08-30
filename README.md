# Mini Dictionary App

## Video Demo
https://youtu.be/baA8hSsyFLc

## Description
This project is my final submission for CS50x. I built a **Mini Dictionary App** using **Flask (Python)**, **SQLite**, and **HTML templates**. The purpose of this project is to create a simple but functional web application that can translate a few English words into Arabic, while also recording every search in a database for later viewing.

When a user types in an English word on the main page, the application checks the built-in dictionary and returns the Arabic meaning. If the word is not available in the dictionary, the app displays a message saying it is not found. At the same time, every search is saved into a **SQLite database** with three details: the word, its meaning, and a timestamp that shows when the search was performed.

The user can then visit a separate **history page**, where all past searches are displayed in reverse chronological order (newest first). This makes the project more than just a translator; it also works like a simple "search log" that tracks activity.

---

## Features
- A clean home page with a search form where users can enter an English word.
- A built-in dictionary that translates a limited set of English words into Arabic (for example: *hello → مرحبا*, *computer → حاسوب*).
- Automatic saving of each search into a SQLite database.
- A `/history` page that lists all past searches along with timestamps.
- Simple and clear HTML templates with a consistent layout.
- Database initialization on startup (the `history` table is created automatically if it does not exist).

---

## Why I Chose This Project
I wanted my final project to be something **small, useful, and educational**.
- First, I wanted to practice working with **Flask**, because it is a very popular web framework in Python.
- Second, I wanted to use a **database (SQLite)** to learn how to store and retrieve data dynamically, instead of only using static variables.
- Third, I thought a dictionary app would be simple but still demonstrate important concepts such as **routes, templates, forms, and persistent storage**.

This project helped me understand the connection between a web application, user input, and databases. I also learned how to organize files properly in a Flask app (Python file, templates folder, requirements, and database).

---

## How to Run
1. Clone or download the project.
2. Make sure you have Python installed.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
