from flask import Blueprint

from services.bookServices import newBook, getBooks, getBook, updateBook, deleteBook

books = Blueprint("books", __name__)


@books.route("/", methods=["GET"])
def get_Books():
    return getBooks()

@books.route("/<id>", methods=["GET"])
def get_Book(id):
    return getBook(id)

@books.route("/", methods=["POST"])
def new_Book():
    return newBook()

@books.route("/<id>", methods=["PUT"])
def update_Book(id):
    return updateBook(id)

@books.route("/<id>", methods=["DELETE"])
def delete_Book(id):
    return deleteBook(id)