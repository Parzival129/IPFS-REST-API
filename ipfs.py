import ipfshttpclient
import os

client = ipfshttpclient.connect()

def addfile(filename: str):
    res = client.add(filename)
    os.remove(filename)
    return res

def getfile(hash: str):
    res = client.get(hash)
    return res