import LPyMongo

import LPyObjectConverter
from LPyObjectConverter import Lstring
from LPyObjectConverter import Lsystem

## your code here..



######################################
# Working example - Lstring insertion
# Needs at least a collection "lstrings" in the database to make it work
#
#
# #Initialize the MongoClient
# client = LPyMongo.InitializeMongoClient('localhost', 27017)
# #Getting the instance of the database
# db = client["{your database}"]
#
# #Stocking your Lstring in a variable
# lstr = Lstring("FFFF[FFF[FF]F]") # or your existing Lstring
# #Returning a JSON document of your Lstring
# d = LPyObjectConverter.ConvertLStringToJSON(lstr)
# #Inserting the document into a collection
# LPyMongo.InsertDocumentIntoCollectionByName(db, "lstrings", d)


#############
# Working example - Lsystem insertion
# Needs at least a collection "lstrings" in the database to make it work
#
# 
# #Initialize the MongoClient
# client = LPyMongo.InitializeMongoClient('localhost', 27017)
# #Getting the instance of the database
# db = client["{your database}"]
#
# #Stocking your Lsystem in a variable
# lsys = Lsystem("../FractalExample.lpy") # or your existing Lsystem
# #Returning a JSON document of your Lsystem
# d = LPyObjectConverter.ConvertLSystemToJSON(lsys)
# #Inserting the document into a collection
# LPyMongo.InsertDocumentIntoCollectionByName(db, "lstrings", d)




#########################
# SPIKE TEST - TO BE DONE
#
# import LStringDBCollector
# doc = PyMongo.FindDocumentsInCollectionByName(db, "lstrings")[3]
# lstr = LPyObjectConverter.ConvertJSONToLString(doc)
# print lstr
#
# LStringDBCollector.GetModuleByIDFromObjId(PyMongo.ObjectId("5a04997cd453d47346ff3c7f"), 2)
