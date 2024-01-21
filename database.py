import pymongo
from config import Config
from datetime import datetime


class Database:

    def __init__(self, uri, database_name):
        self._client = pymongo.MongoClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.user

    def new_user(self, id):
        return dict(
            _id=int(id),
            file_id=None,
            caption=None
        )

    def add_user(self, b, m):
        u = m.from_user
        if not self.is_user_exist(u.id):
            user = self.new_user(u.id)
            self.col.insert_one(user)

    def is_user_exist(self, id):
        user = self.col.find_one({'_id': int(id)})
        return bool(user)

    def total_users_count(self):
        count = self.col.count_documents({})
        return count

    def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    def delete_user(self, user_id):
        self.col.delete_many({'_id': int(user_id)})

    def set_thumbnail(self, id, file_id):
        self.col.update_one({'_id': int(id)}, {'$set': {'file_id': file_id}})

    def get_thumbnail(self, id):
        user = self.col.find_one({'_id': int(id)})
        return user.get('file_id', None)

    def set_caption(self, id, caption):
        self.col.update_one({'_id': int(id)}, {'$set': {'caption': caption}})

    def get_caption(self, id):
        user = self.col.find_one({'_id': int(id)})
        return user.get('caption', None)


db = Database(Config.DB_URL, Config.DB_NAME)
