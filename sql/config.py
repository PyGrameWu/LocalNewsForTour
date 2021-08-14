Host = 'localhost'
Port = 3306
Username = 'root'
Password = 'root'
DB = 'news'

DB_Url = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}'.format(
    username=Username,
    password=Password,
    host=Host,
    port=Port,
    db=DB
)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_Url)
Base = declarative_base(engine)  # SQLORM基类
session = sessionmaker(engine)()  # 构建session对象