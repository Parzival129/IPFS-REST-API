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

def showfile(hash:str):
    res = client.cat(hash)
    return res