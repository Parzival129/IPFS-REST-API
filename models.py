from .database import Base
from sqlalchemy import Column, Integer, String

class ipfs_log(Base):
    __tablename__ = 'ipfs-logs'
    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String)
    hash = Column(String)