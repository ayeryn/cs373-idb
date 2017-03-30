from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
house = Table('house', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('region', String),
    Column('words', String),
    Column('current_lord', String),
    Column('title', String),
    Column('overlord', String),
    Column('imageLink', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['house'].columns['imageLink'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['house'].columns['imageLink'].drop()
