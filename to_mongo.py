# -*- conding:utf-8 -*-
__author__ = 'wangdaodao'


import pymongo
from settings import MONGO_DB, MONGO_URL, MONGO_TABLE


class MongoPipeline(object):
    conn = pymongo.MongoClient(MONGO_URL)

    def to_mongo(self, item):
        collection_name = MONGO_TABLE
        db = self.conn[MONGO_DB]
        for tt in item:
            db[collection_name].insert(dict(tt))
        print('done!')

    def from_mongo(self):
        collection_name = MONGO_TABLE
        db = self.conn[MONGO_DB]
        collection = db.get_collection(collection_name)
        document = collection.find()
        return document

    def close_mongo(self):
        self.conn.close()


# x = MongoPipeline()
# x.to_mongo({'name':22222, 'sex':'female'})
