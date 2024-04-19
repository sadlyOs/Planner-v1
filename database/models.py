from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, BigInteger, String

Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    lang = Column(String(2), default='ru')
    

    