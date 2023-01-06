import os
import json
import sys

class db:
    def getDB(name):
        if name=="{dbcode=success, "+name+"}":
            print("[DB Error]: Cant use ´editValues´ inside ´getDB´ function!", file=sys.stderr)
            return "unknown"
        else:
            if os.path.isfile(name):
                with open(name + ".json", "w") as f:
                    return name
            else:
                print('[DB Error]: Invalid database name!', file=sys.stderr)
                return "unknown"
    
    def createDB(name):
        if name=="{dbcode=success, "+name+"}":
            print("[DB Error]: Cant use ´editValues´ inside ´createDB´ function!", file=sys.stderr)
            return "unknown"
        else:
            if not os.path.isfile(name):
                with open(name + ".json", "w") as f:
                    json.dump("{}", f)
                    return name
            else:
                print("[DB Error]: Database already exists!", file=sys.stderr)
                return "unknown"
            
    def getValues(dbdat):
        if dbdat=="{dbcode==success, "+dbdat+"}":
            print("[DB Error]: Cant use ´editValue´ inside ´getValues´ function!", file=sys.stderr)
            return "unknown"
        else:
            if os.path.isfile(dbdat):
                with open(dbdat + ".json", 'r') as f:
                    dt = json.load(f)
                    return dt
            else:
                print("[DB Error]: Unknown database!", file=sys.stderr)
                return "unknown"

    def editValues(dbdat, key, value):
        if dbdat=="{dbcode=success, "+dbdat+"}":
            return "dbcode = success"
        else:
            if os.path.isfile(dbdat):
                with open(dbdat + ".json", 'r') as f:
                    data = json.load(f)

                data[key] = value

                with open(dbdat + ".json", 'w') as f:
                    json.dump(data, f)

                    return "{dbcode=success, "+dbdat+"}"
            else:
                print("[DB Error]: Unknown database!", file=sys.stderr)
                return "unknown"