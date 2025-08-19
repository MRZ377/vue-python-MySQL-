from ..db.initdb import DB
from ..models.usermodel import User
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy import or_

class Userserve:
    def __init__(self):
        self.db = DB()
        self.db.create_tables
        self.Session = self.db.Session

    def getlogin(self, username:str) -> dict | bool:
        """获取用户信息"""
        Session = self.Session()

        try:
            user = Session.query(User).filter_by(UserName = username).first()
            if user:
                return {
                    "username":user.UserName,
                    "password":user.PassWord,
                    "permissions":user.Permissions
                }
            return False
        except SQLAlchemyError as e:
            print(e)
            return False
        finally:
            Session.close()

    def setuser(self, username:str, password:str) -> bool:
        """注册用户信息"""
        session = self.Session()
        try:
            user = User(UserName = username, PassWord = password)
            session.add(user)
            session.commit()
            return True
        except IntegrityError as e:
            session.rollback()
            print(e)
            return False
        except SQLAlchemyError as e:
            session.rollback()
            print(e)
            return False
        finally:
            session.close()

    def deluser(self, username:str, password:str) -> bool:
        """注销用户"""
        session = self.Session()
        try:
            user = session.query(User).filter_by(UserName = username, PassWord = password).first()
            if not user:
                return False
            session.delete(user)
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print(e)
            return False
        finally:
            session.close()

    def changeuser(self, username:str, password:str, new_username:str, new_password:str) -> bool:
        """修改用户信息"""
        session = self.Session()
        try:
            user = session.query(User).filter_by(UserName = username, PassWord = password).first()
            if not user:
                return False
            user.UserName = new_username
            user.PassWord = new_password
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print(e)
            return False
        finally:
            session.close()
            
