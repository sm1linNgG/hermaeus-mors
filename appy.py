from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Подключение к базе
connection = sqlite3.connect('my_database.db', check_same_thread=False)
cursor = connection.cursor()


# Функция для получения товаров определённой категории
def productDB(category):
    cursor.execute("SELECT * FROM product WHERE category=?", (category,))
    return cursor.fetchall()

# Функция для главной (главная + новинки/тишки/худи по имени)
def productDB_main():
    cursor.execute("""
        SELECT * FROM product
        WHERE category='главная'
           OR name LIKE '%новинки%'
           OR name LIKE '%тишка%'
           OR name LIKE '%худи%'
    """)
    return cursor.fetchall()

# Главная страница
@app.route('/')
def index():
    shop = productDB_main()
    return render_template("index.html", shop=shop)

# Каталог (все товары)
@app.route('/catalog')
def catalog():
    cursor.execute("SELECT * FROM product")
    shop = cursor.fetchall()
    return render_template("catalog.html", shop=shop)

# Футболки
@app.route('/T-shorts')
def Tshirts():
    shop = productDB("футболка")
    return render_template("T-short.html", shop=shop)

# Худи
@app.route('/hoodie')
def hoodie():
    shop = productDB("худи")
    return render_template("hoodie.html", shop=shop)

# Аксессуары
@app.route('/accessories')
def accessories():
    shop = productDB("аксессуар")
    return render_template("accessories.html", shop=shop)


if __name__ == '__main__':
    app.run(debug=True)

