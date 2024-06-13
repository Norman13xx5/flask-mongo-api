from flask import Blueprint

books = Blueprint("books", __name__)


@books.route("/", methods=["GET"])
def getBooks():
    return "Books"

@books.route("/<id>", methods=["GET"])
def getBook(id):
    return f"Book {id}"

@books.route("/", methods=["POST"])
def newBook():
    return "New Book"

@books.route("/<id>", methods=["PUT"])
def editBook(id):
    return f"Edit Book {id}"

@books.route("/<id>", methods=["DELETE"])
def deleteBook(id):
    return f"Delete Book {id}"