#!/usr/bin/python3
from pymongo import MongoClient
import sys
## Just hardcode
client = MongoClient(sys.argv[1])
result=client.db_name.command('ping')
if result is None:
    print("Problem")
    sys.exit(2)
sys.exit (0)
