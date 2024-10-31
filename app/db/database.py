from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from app.db.models import Country, City, TargetType, Target, Mission
from app.settings.config import DB_URL

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)


def init_db():
    with session_maker() as session:
        res1 = session.query(Country).all()
        res2 = session.query(City).all()
        res3 = session.query(TargetType).all()
        res4 = session.query(Target).all()
        res5 = session.query(Mission).all()
        print()
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
