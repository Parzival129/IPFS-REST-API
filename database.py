from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHMEMY_DATABASE_URL = 'sqlite:///./ipfs-log.db'

engine = create_engine(SQLALCHMEMY_DATABASE_URL, connect_args={
    'check_same_thread':False
})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base var for interaction
Base = declarative_base()
