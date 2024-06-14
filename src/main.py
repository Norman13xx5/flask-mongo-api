from flask import Flask, render_template
from dotenv import load_dotenv
import os
from database.db import mongo
from routes.booksRoutes import books

load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

app.register_blueprint(books, url_prefix="/books")

if __name__ == "__main__":
    # Modo desarrollo, esto es para que reinicie el servidor apenas exista un cambio en el proyecto.
    app.run(debug=True)