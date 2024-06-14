from database.db import mongo
from flask import request, Response, jsonify
from bson import json_util, ObjectId

def newBook():
    data = request.get_json()
    author = data.get("author", None),
    title = data.get("title", None)
    description = data.get("description", None)
    if title and author:
        response = mongo.db.books.insert_one({"author": author, "title": title, "description": description})
        newBook = {
            "_id": str(response.inserted_id),
            "author": author,
            "title": title,
            "description": description
        }
        return newBook
    else:
        return not_found()

def getBooks():
    data = mongo.db.books.find()
    books = json_util.dumps(data)
    return Response(books, mimetype="application/json")

def getBook(id):
    data = mongo.db.books.find_one({"_id": ObjectId(id)})
    book = json_util.dumps(data)
    return Response(book, mimetype="application/json")


def updateBook(id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    filter = {"_id": ObjectId(id)}
    update_result = mongo.db.books.update_one(filter, {"$set": data})

    if update_result.modified_count > 0:
        return jsonify({'message': 'Book updated successfully'}), 200
    else:
        return jsonify({'message': 'Book not found or no updates applied'}), 404

def deleteBook(id):
    mongo.db.books.delete_one({"_id": ObjectId(id)})
    return jsonify({'message': 'Book deleted successfully'})