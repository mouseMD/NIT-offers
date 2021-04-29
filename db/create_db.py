from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, inspect

DB_URL = 'postgresql://admin:admin@localhost/offers'
engine = create_engine(DB_URL)

metadata = MetaData(engine)

table = Table('offers', metadata,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('user_id', Integer, index=True),
              Column('title', String(120)),
              Column('text', Text)
              )

inspector = inspect(engine)
if 'users' in inspector.get_table_names():
    table.drop(engine)
table.create(engine)

for _t in metadata.tables:
    print("Table: ", _t)
