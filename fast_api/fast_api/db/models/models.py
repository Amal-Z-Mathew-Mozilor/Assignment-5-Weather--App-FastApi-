from sqlalchemy import create_engine, Column, Integer, String,Float,DateTime,ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from datetime import datetime,timezone
Base = declarative_base()
class User(Base):
    __tablename__= "users"
    id=Column(Integer,primary_key=True,autoincrement=True,index=True)
    password=Column(String)
    email=Column(String,unique=True)
class Weather(Base):
    __tablename__ = "weather"
    id=Column(Integer,primary_key=True,autoincrement=True,index=True)
    city=Column(String)
    country = Column(String) 
    latitude=Column(Float)
    longitude=Column(Float)
    temperature=Column(Float)
    feels_like=Column(Float)
    wind=Column(Float)
    humidity=Column(Float)
    time=Column(DateTime,default=lambda: datetime.now(timezone.utc))
    user_id=Column(Integer,ForeignKey("users.id"))