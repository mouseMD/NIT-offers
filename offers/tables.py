import sqlalchemy

metadata = sqlalchemy.MetaData()

offers_table = sqlalchemy.Table(
    'offers',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('user_id', sqlalchemy.Integer),
    sqlalchemy.Column('title', sqlalchemy.String(120)),
    sqlalchemy.Column('text', sqlalchemy.Text)
)
