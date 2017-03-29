from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
character = Table('character', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR),
    Column('titles', VARCHAR),
    Column('father', VARCHAR),
    Column('mother', VARCHAR),
    Column('spouse', VARCHAR),
    Column('played_by', VARCHAR),
    Column('house', VARCHAR),
)

character = Table('character', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('titles', String),
    Column('father', String),
    Column('mother', String),
    Column('spouse', String),
    Column('house', String),
    Column('actor', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['character'].columns['played_by'].drop()
    post_meta.tables['character'].columns['actor'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['character'].columns['played_by'].create()
    post_meta.tables['character'].columns['actor'].drop()
