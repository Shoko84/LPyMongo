from openalea.lpy import *
from datetime import datetime

def GetLStringValuesAsTree(lstring):
    print "lstring:", lstring
    data = []

    for i, item in enumerate(lstring):
        childrenArray = []
        if isinstance(lstring.children(i), int):
            childrenArray.append(lstring.children(i))
        else:
            childrenArray = lstring.children(i)
        data.append({
            "moduleName": item.name,
            "argsValues": tuple(item),
            "id": i,
            "children" : childrenArray,
            "parent": lstring.parent(i)
        })
        print ("index:", i, "Nom:", item.name, "Enfants:", childrenArray, "parent:", lstring.parent(i))
    return (data);

def ConvertLStringToJSON(lstring, fileName = None, nIteration = 0):
    return ({
        "fileName": fileName,
        "history": [{
            "dateCreated": datetime.utcnow(),
            "iteration": nIteration,
            "tree": GetLStringValuesAsTree(lstring)
        }]
    })


def ConvertLSystemToJSON(lsystem):
    obj = {
        "fileName": lsystem.filename,
        "history": []
    }
    for i in range(lsystem.derivationLength):
        obj["history"].append({
            "dateCreated": datetime.utcnow(),
            "iteration": i,
            "tree": GetLStringValuesAsTree(lsystem.iterate(i))
        })
    return (obj)

def ConvertJSONTreeToLString(tree):
    s = ""
    for item in tree:
        s += str(item["moduleName"]);
        if (len(item["argsValues"]) != 0):
            s += "(" + ",".join(map(str, item["argsValues"])) + ")"
    return Lstring(s)
