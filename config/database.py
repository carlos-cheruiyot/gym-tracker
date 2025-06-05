from sqlalchemy import create_engine


#creating the database connections

db_url = "sqlite:///db/member.db"

engine = create_engine(db_url, echo=True)
with engine.connect() as connection:
    pass