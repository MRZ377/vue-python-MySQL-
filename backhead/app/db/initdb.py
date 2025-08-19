from ..db.config import dbconfig
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
from ..models.Base import Base

class DB:
    def __init__(self):
        #初始化链接
        self.baseurl = f"mysql+pymysql://{dbconfig['user']}:{dbconfig['password']}@{dbconfig['host']}:{dbconfig['port']}/?charset={dbconfig['charset']}"
        #创建数据库
        tmp_engine = create_engine(self.baseurl, isolation_level="AUTOCOMMIT")
        with tmp_engine.connect() as conn:
            conn.execute(
                text(f"CREATE DATABASE IF NOT EXISTS `{dbconfig['database']}` CHARACTER SET {dbconfig['charset']}")
            )
        #初始化数据库
        self.dburl = f"mysql+pymysql://{dbconfig['user']}:{dbconfig['password']}@{dbconfig['host']}:{dbconfig['port']}/{dbconfig['database']}?charset={dbconfig['charset']}"
        self.engine = create_engine(self.dburl, echo=False)
        self.Session = sessionmaker(bind=self.engine)
    
    def create_tables(self):
        """创建不存在的表"""
        existing_tables = inspect(self.engine).get_table_names()
        tables_to_create = [table for table in Base.metadata.tables.keys() if table not in existing_tables]
        if tables_to_create:
            Base.metadata.create_all(self.engine, tables=[Base.metadata.tables[table] for table in tables_to_create])
