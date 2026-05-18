from pymongo import MongoClient
import os


class Dictionary:
    def __init__(self):
        client = MongoClient(os.environ.get("MONGODB_URI"))
        db = client["python_katas"]
        self.collection = db["dictionary"]

    def newentry(self, word, definition):
        self.collection.update_one(
            {"word": word}, {"$set": {"definition": definition}}, upsert=True
        )

    def look(self, word):
        result = self.collection.find_one({"word": word})
        if result:
            return result["definition"]
        return f"Can't find entry for {word}"
