from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.dialects.mysql import LONGTEXT
from sql.config import Base

class News(Base):
    __tablename__ = 'newsspide'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255),nullable=False)
    url = Column(String(255),unique=True,nullable=False)
    platform = Column(String(255),nullable=False)
    data = Column(LONGTEXT,nullable=False)
    date = Column(DateTime,nullable=False)



if __name__ == "__main__":
    Base.metadata.create_all() # 将模型映射到数据库中
    print("初始化数据库成功")