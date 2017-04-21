from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
alcohol = Table('alcohol', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
)

ingredient = Table('ingredient', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
)

recipe = Table('recipe', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('alcohol_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['alcohol'].create()
    post_meta.tables['ingredient'].create()
    post_meta.tables['recipe'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['alcohol'].drop()
    post_meta.tables['ingredient'].drop()
    post_meta.tables['recipe'].drop()
