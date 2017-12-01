import LPyMongo

client = LPyMongo.InitializeMongoClient('localhost', 27017)
db = client["test_L-Py"]

def GetModuleByIDFromObjId(lstrObjId, moduleId):
    docs = LPyMongo.FindDocumentsInCollectionByName(db, "lstrings", {"_id": lstrObjId, "tree.id": moduleId}, {"tree": {"$elemMatch": {"id": moduleId}}})
    LPyMongo.DumpDocuments(docs)
