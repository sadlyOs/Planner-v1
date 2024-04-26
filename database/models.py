from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Boolean, Column, BigInteger, DateTime, ForeignKey, Integer, String

Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    lang = Column(String(2), default='ru')
    tasks = relationship("Task", back_populates='user')
    rel = relationship("RelUserTask", back_populates='user')

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    description = Column(String)
    due_datetime = Column(DateTime, default=datetime.utcnow)
    completed = Column(Boolean, default=False)
    expectation = Column(Boolean, default=False)
    user = relationship('User', back_populates="tasks")
    rel = relationship("RelUserTask", back_populates='tasks')
    

class RelUserTask(Base):
    __tablename__ = 'rel'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    task_id = Column(String, ForeignKey('tasks.id'))
    user = relationship('User', back_populates="rel")
    tasks = relationship("Task", back_populates='rel')