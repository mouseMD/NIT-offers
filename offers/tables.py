from sqlalchemy import MetaData, Table, Column, Integer, String, Text

metadata = MetaData()

offers_table = Table(
    'offers',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', Integer, index=True),
    Column('title', String(120)),
    Column('text', Text)
)
