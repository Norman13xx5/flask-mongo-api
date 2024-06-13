from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # Modo desarrollo, esto es para que reinicie el servidor apenas exista un cambio en el proyecto.
    app.run(debug=True)