from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
character = Table('character', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('titles', String),
    Column('aliases', String),
    Column('father', String),
    Column('mother', String),
    Column('spouse', String),
    Column('allegiances', String),
    Column('played_by', String),
)

episode = Table('episode', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('season', Integer),
    Column('previous_epsiode', String),
    Column('next_episode', String),
    Column('characters', String),
)

house = Table('house', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('region', String),
    Column('words', String),
    Column('current_lord', String),
    Column('heir', String),
    Column('overlord', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['character'].create()
    post_meta.tables['episode'].create()
    post_meta.tables['house'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['character'].drop()
    post_meta.tables['episode'].drop()
    post_meta.tables['house'].drop()
