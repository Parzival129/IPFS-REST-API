from fastapi import FastAPI, File, UploadFile, Depends
from . import models
from .ipfs import addfile, getfile, showfile, linksfile, filecmd
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def Add_to_db(db, res, operation, hashid=None):

    if res == None:
        new_log = models.ipfs_log(operation=operation, hash=hashid)
    else:
        new_log = models.ipfs_log(operation=operation, hash=res['Hash'])
    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return new_log

@app.post("/addfile")
async def upload_file(data: UploadFile = File(...), file: bytes = File(...), db: Session = Depends(get_db)):

    print(f"Uploading {data.filename} to main IPFS network ...")
    f = open('dropbucket/cache/' + data.filename, "wb")
    f.write(file)
    f.close()

    res = addfile('dropbucket/cache/' + data.filename)
    Add_to_db(db, res, 'ADD')
    #Sends server the name of the file as a response
    return {"Filename": data.filename, "Detail": res}


@app.get("/getfile")
async def download_file(hash: str, db: Session = Depends(get_db)):

    print (f"Downloading file of hash: {hash}")
    res = getfile(hash)
    Add_to_db(db, res, 'GET', hashid=hash)

    return {"Hash": hash}

@app.get("/showfile")
def preview_file(hash: str, db: Session = Depends(get_db)):

    print (f"Fetching file of hash: {hash}")
    content = showfile(hash)
    res = {'Hash': hash}
    Add_to_db(db, res, 'CAT')

    return {"Content": content}

@app.get("/linksfile")
def file_links(hash: str, db: Session = Depends(get_db)):

    print(f"Fetching links for file of hash: {hash}")
    res = linksfile(hash)
    Add_to_db(db, None, 'LINK', hashid=hash)

    return res

@app.get("/filecmd")
def MFS_command(command: str, path: str = None, data: str = None, option: bool = False, db: Session = Depends(get_db)):

    res = filecmd(command, [path, data, option])
    Add_to_db(db, None, command.upper(), hashid='N/A')

    return res


