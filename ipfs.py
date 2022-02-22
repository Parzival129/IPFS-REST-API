import ipfshttpclient
import os
import io

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

def linksfile(hash: str):
    res = client.ls(hash)
    return res

def filecmd(command, params: list):

    if command == 'ls':
        return client.files.ls(params[0]) # path to list files

    elif command  == 'write':
        client.files.write(params[0], io.BytesIO(params[1].encode()), create=params[2]) # path to write data, data itself, wether or not to create the file if it doesn't exist
        return {'Detail': f'Successfully added: {params[0]} to MFS'}

    elif command == 'rm':
        return client.files.rm(params[0], recursive=params[2]) # path to file to delete, boolean to recursively delete directory

    elif command == 'read':
        return client.files.read(params[0]) # path to file to read

    elif command == 'stat':
        return client.files.stat(params[0]) # path to file to get information on

    elif command == 'mkdir':
        client.files.mkdir(params[0]) # path to where to create the directory
        return {'Detail': f'Successfully added: {params[0]} to MFS'}

    elif command == 'mv':
        return client.files.mv(params[0], params[1]) # path of initial file, path to where to send file

    elif command == 'cp':
        return client.files.cp(params[0], params[1]) # path of file to copy, path of where to copy it too


