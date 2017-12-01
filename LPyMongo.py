from pymongo import MongoClient
from pymongo import CursorType
from bson.objectid import ObjectId

# DUMPER
## Dump documents on screen
def DumpDocuments(docs):
    for doc in docs:
        print(doc)

# INITIALIZER
## Connects to the MongoDB and returns the MongoClient Object
def InitializeMongoClient(host, port):
    return (MongoClient(host, port))

# FINDER
## Finds and returns all documents from the collection
def FindAllDocumentsInCollection(collection):
    docs = collection.find()
    return (list(docs))

def FindAllDocumentsInCollectionByName(database, collectionName):
    collection = database[collectionName]
    docs = collection.find()
    return (list(docs))

## Finds and returns all documents filtered by arguments from the collection
def FindDocumentsInCollection(collection, filter = None,
                              projection = None, skip = 0,
                              limit = 0, no_cursor_timeout = False,
                              cursor_type = CursorType.NON_TAILABLE,
                              sort = None, allow_partial_results = False,
                              oplog_replay = False):
    docs = collection.find(filter, projection, skip, limit, no_cursor_timeout,
                           cursor_type, sort, allow_partial_results, oplog_replay)
    return (list(docs))

def FindDocumentsInCollectionByName(database, collectionName, filter = None,
                                    projection = None, skip = 0,
                                    limit = 0, no_cursor_timeout = False,
                                    cursor_type = CursorType.NON_TAILABLE,
                                    sort = None, allow_partial_results = False,
                                    oplog_replay = False):
    collection = database[collectionName]
    docs = collection.find(filter, projection, skip, limit, no_cursor_timeout,
                           cursor_type, sort, allow_partial_results, oplog_replay)
    return (list(docs))


# INSERTION
## Inserts and returns inserted document from the collection
def InsertDocumentIntoCollection(collection, doc):
    return (collection.insert_one(doc).inserted_id)

def InsertDocumentIntoCollectionByName(database, collectionName, doc):
    collection = database[collectionName]
    return (collection.insert_one(doc).inserted_id)


# DELETION
## Delete one document and returns deleted document informations from the collection
def DeleteOneDocumentFilteredInCollection(collection, filter):
    return (collection.delete_one(filter))

def DeleteOneDocumentFilteredInCollectionByName(database, collectionName, filter):
    collection = database[collectionName]
    return (collection.delete_one(filter))

## Delete all documents and returns deleted documents informations from the collection
def DeleteAllDocumentsFilteredInCollection(collection, filter):
    return (collection.delete_many(filter))

def DeleteAllDocumentsFilteredInCollectionByName(database, collectionName, filter):
    collection = database[collectionName]
    return (collection.delete_many(filter))


# REPLACEMENT
## Replaces one document and returns replaced document informations from the collection
def ReplaceOneDocumentFilteredInCollection(collection, filter, doc, upsert = False):
    return (collection.replace_one(filter, doc, upsert))

def ReplaceOneDocumentFilteredInCollectionByName(database, collectionName, filter, doc, upsert = False):
    collection = database[collectionName]
    return (collection.replace_one(filter, doc, upsert))


# UPDATE
## Updates one document and returns updated document informations from the collection
def UpdateOneDocumentFilteredInCollection(collection, filter, doc, upsert = False):
    return (collection.update_one(filter, doc, upsert))

def UpdateOneDocumentFilteredInCollectionByName(database, collectionName, filter, doc, upsert = False):
    collection = database[collectionName]
    return (collection.update_one(filter, doc, upsert))

## Updates all documents and returns updated documents informations from the collection
def UpdateAllDocumentsFilteredInCollection(collection, filter, doc, upsert = False):
    return (collection.update_many(filter, doc, upsert))

def UpdateAllDocumentsFilteredInCollectionByName(database, collectionName, filter, doc, upsert = False):
    collection = database[collectionName]
    return (collection.update_many(filter, doc, upsert))
