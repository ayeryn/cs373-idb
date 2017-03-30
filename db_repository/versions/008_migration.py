from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
house = Table('house', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR),
    Column('region', VARCHAR),
    Column('words', VARCHAR),
    Column('current_lord', VARCHAR),
    Column('heir', VARCHAR),
    Column('overlord', VARCHAR),
)

house = Table('house', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('region', String),
    Column('words', String),
    Column('current_lord', String),
    Column('title', String),
    Column('overlord', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['house'].columns['heir'].drop()
    post_meta.tables['house'].columns['title'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['house'].columns['heir'].create()
    post_meta.tables['house'].columns['title'].drop()
