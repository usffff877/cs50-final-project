#### Video Demo: https://youtu.be/baA8hSsyFLc

#### Description: This is my final project for CS50, called Mini Dictionary App
This is a small web application built with **Python** and **Flask**.
The idea is simple: the app translates English words into Arabic and keeps track of all searches in an **SQLite database**.

---

### Features:
- Enter an English word and get its meaning in Arabic.
- If the word is not found, the app shows: *"Not found in dictionary"*.
- Every search is saved into the database with a timestamp.
- A dedicated page `/history` displays the search history in reverse chronological order.

---

### Files:
- `app.py` → main application file.
- `templates/layout.html` → base template.
- `templates/index.html` → home page for searching words.
- `templates/history.html` → page to display search history.
- `dictionary.db` → SQLite database file.
- `requirements.txt` → required Python libraries.

---

### How to run:
1. Clone this repository:
   ```bash
   git clone https://github.com/usffff877/cs50-final-project.git
   cd cs50-final-project
