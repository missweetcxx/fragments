# coding: utf-8
from sqlalchemy import BigInteger, Column, Integer, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    task = Column(Text, nullable=False)
    priority = Column(Integer)
    owner = Column(Text, nullable=False)
    create_time = Column(BigInteger, nullable=False)
    update_time = Column(BigInteger, nullable=False)
    status = Column(Integer)


class RegisterUser(Base):
    __tablename__ = 'register_user'

    id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    birthday = Column(Text)
    forbidden = Column(Integer, nullable=False, server_default=text("'0'"))
    update_time = Column(Text)
    create_time = Column(Text)