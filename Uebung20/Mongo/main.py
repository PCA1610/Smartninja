from pymongo import MongoClient
from bson import ObjectId

if __name__ == '__main__':
    client = MongoClient()

    db = client.test_database

    people = db.people

    people.insert({'name': 'Mike', 'food': 'cheese'})
    people.insert({'name': 'John', 'food': 'ham', 'location': 'UK'})
    people.insert({'name': 'Markus', 'food': 'burger'})
    people.insert({'name': 'John', 'food': 'eggs'})
    people.insert({'name': 'Jane', 'food': 'salad'})
    people.insert({'name': 'John', 'food': 'sausages'})

    #peeps = people.find()

    #for person in people.find({"_id": ObjectId("5c508da40ae6964e867b6029")}):
        #print (person['food'])
    people.update_one({"name": "John", "food": "sausages"}, {"$set": {"name": "John", "food": "bread"}})
