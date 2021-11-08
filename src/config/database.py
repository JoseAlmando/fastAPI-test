from sqlalchemy import create_engine, MetaData

engine = create_engine('sqlite:///./src/config/database.db', echo=True)  

meta = MetaData() 

conn = engine.connect()