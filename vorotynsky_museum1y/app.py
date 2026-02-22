from flask import Flask, render_template

app = Flask(__name__)

# 1) О проекте (главная)
@app.route("/")
@app.route("/about")
@app.route("/introduction")   # совместимость со старой ссылкой
def about():
    return render_template("introduction.html")

# 2) История рода Воротынских
@app.route("/dynasty")
@app.route("/museum")         # совместимость со старой ссылкой
def dynasty():
    return render_template("index.html")

# 3) На службе Отечеству
@app.route("/service")
@app.route("/biography")      # совместимость со старой ссылкой
def service():
    return render_template("biography.html")

# 4) Князь Воротынский и земля Калужская
@app.route("/kaluga")
@app.route("/maps")           # совместимость со старой ссылкой
def kaluga():
    return render_template("maps.html")

# 5) Книги о Воротынском
@app.route("/books")
@app.route("/textbooks")      # совместимость со старой ссылкой
def books():
    return render_template("textbooks.html")

# 6) Памятники
@app.route("/monuments")
def monuments():
    return render_template("monuments.html")

# 7) Галерея изображений
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


if __name__ == "__main__":
    app.run(debug=True)
