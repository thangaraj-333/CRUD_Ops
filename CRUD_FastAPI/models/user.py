from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Boolean
from config.db import meta

users = Table(
    'users',meta,
    Column('id',Integer,primary_key=True,autoincrement=True),
    Column('title',String(200),nullable=False),
    Column('description',String(200)),
    Column('completed',Boolean,default=False)
)