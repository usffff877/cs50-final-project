import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# دالة للاتصال بقاعدة البيانات
def get_db():
    conn = sqlite3.connect("dictionary.db")
    conn.row_factory = sqlite3.Row
    return conn

# دالة لإنشاء الجدول لو مش موجود
def init_db():
    conn = get_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            meaning TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()
    print("✅ تم إنشاء الجدول (history) أو موجود بالفعل.")

# القاموس البسيط
DICTIONARY = {
    "hello": "مرحبا",
    "world": "العالم",
    "computer": "حاسوب",
    "book": "كتاب",
    "love": "حب",
    "school": "مدرسة"
}

# الصفحة الرئيسية
@app.route("/", methods=["GET", "POST"])
def index():
    meaning = None
    word = None
    if request.method == "POST":
        word = request.form.get("word", "").lower()
        meaning = DICTIONARY.get(word, "غير موجود في القاموس")

        # حفظ البحث في قاعدة البيانات
        conn = get_db()
        conn.execute("INSERT INTO history (word, meaning) VALUES (?, ?)", (word, meaning))
        conn.commit()
        conn.close()

    return render_template("index.html", word=word, meaning=meaning)

# صفحة history
@app.route("/history")
def history():
    conn = get_db()
    rows = conn.execute("SELECT * FROM history ORDER BY timestamp DESC").fetchall()
    conn.close()
    return render_template("history.html", history=rows)

if __name__ == "__main__":
    init_db()   # هنا يتأكد يعمل الجدول قبل ما السيرفر يشتغل
    app.run(debug=True)
