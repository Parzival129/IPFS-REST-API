from webbrowser import get
from fastapi import FastAPI, File, UploadFile, Form
from ipfs import addfile, getfile

app = FastAPI()

@app.post("/addfile")
async def upload_file(data: UploadFile = File(...), file: bytes = File(...)):

    print(f"Uploading {data.filename} to main IPFS network ...")

    f = open('cache/' + data.filename, "wb")
    f.write(file)
    f.close()

    res = addfile('cache/' + data.filename)
    #Sends server the name of the file as a response
    return {"Filename": data.filename, "Detail": res}


@app.get("/getfile")
async def download_file(hash: str):

    print (f"Downloading file of hash: {hash}")
    res = getfile(hash)

    return {"Hash": hash}
