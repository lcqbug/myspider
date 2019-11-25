# 操作数据库的工具类
# 参考资料 https://sqlalchemy-utils.readthedocs.io/en/latest/database_helpers.html
# 用pymysql驱动有个异常 https://blog.csdn.net/xiaoxiaodechongzi/article/details/103241909
from sqlalchemy import Column, String,INT,Text, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils.functions import database_exists,create_database
import settings
# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'dizigui'
    # (title, num, lecturer, lec_date, content)
    # 表的结构:
    id = Column(INT, primary_key=True,autoincrement=True)
    title = Column(String(20))
    num = Column(String(20))
    lecturer = Column(String(20))
    lec_date = Column(String(20))
    content = Column(Text,nullable=False)

# # 初始化数据库连接:
# engine = create_engine(settings.dizigui_sql)
# # 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)


def init_db():

    # 创建表
    engine = create_engine(
        # 'mysql+pymysql://root:199199@127.0.0.1:3306/blog?charset=utf8',
        settings.dizigui_sql,
        max_overflow=2,  # 超过连接池大小外最多创建的数量,
        pool_size=5,  # 连接池的大小
        pool_timeout=30,  # 池中没有线程最多等待的时间
        pool_recycle=-1,  # 多久之后对线程中的线程进行一次连接的回收(重置)

    )
    if database_exists(settings.dizigui_sql):
        print('数据库已经存在了')
        return
    # 建库
    create_database(engine.url)
    # 建表
    Base.metadata.create_all(engine)

def update_db():
    """
    更新数据库表结构
    :return:
    """

    # 创建表
    engine = create_engine(
        # 'mysql+pymysql://root:199199@127.0.0.1:3306/blog?charset=utf8',
        settings.dizigui_sql,
        max_overflow=2,  # 超过连接池大小外最多创建的数量,
        pool_size=5,  # 连接池的大小
        pool_timeout=30,  # 池中没有线程最多等待的时间
        pool_recycle=-1,  # 多久之后对线程中的线程进行一次连接的回收(重置)

    )

    # 建表  这个会更新数据库表结构
    Base.metadata.create_all(engine)

def drop_db():
    """
    根据类删除数据库表
    """
    engine = create_engine(
        settings.dizigui_sql,
        max_overflow=2,  # 超过连接池大小外最多创建的数量,
        pool_size=5,  # 连接池的大小
        pool_timeout=30,  # 池中没有线程最多等待的时间
        pool_recycle=-1,  # 多久之后对线程中的线程进行一次连接的回收(重置)

    )
    Base.metadata.drop_all(engine)

