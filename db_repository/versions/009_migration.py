from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
episode = Table('episode', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR),
    Column('season', INTEGER),
    Column('previous_epsiode', VARCHAR),
    Column('next_episode', VARCHAR),
    Column('characters', VARCHAR),
)

episode = Table('episode', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('season', Integer),
    Column('predecessor', String),
    Column('successor', String),
    Column('characters', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['episode'].columns['next_episode'].drop()
    pre_meta.tables['episode'].columns['previous_epsiode'].drop()
    post_meta.tables['episode'].columns['predecessor'].create()
    post_meta.tables['episode'].columns['successor'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['episode'].columns['next_episode'].create()
    pre_meta.tables['episode'].columns['previous_epsiode'].create()
    post_meta.tables['episode'].columns['predecessor'].drop()
    post_meta.tables['episode'].columns['successor'].drop()
