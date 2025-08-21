from ..db.initdb import DB
from ..models.bookmodel import Book
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_

class Bookserve:
    def __init__(self):
        self.db = DB()
        self.db.create_tables()
        self.Session = self.db.Session

    def getbooks(self) -> list[dict] | bool:
        """获取前五十行数据"""
        session = self.Session()
        try:
            books = (session.query(Book).order_by(Book.BookID).limit(50).all())
            if books:
                return [
                    {
                        "bookid": book.BookID,
                        "bookname":book.BookName,
                        "bookimage":book.BookImage,
                        "author":book.Author,
                        "category":book.Category,
                        "bookinfo":book.BookInfo,
                        "createdtime":book.CreatedTime.strftime("%Y-%m-%d")
                    }
                    for book in books
                ]
            else:
                return []
        except Exception as e:
            print(str(e))
            return False
        finally:
            session.close()

    def getbookscategory(self,keyword:str) -> list[dict] | bool:
        """获取类别下50本书籍"""
        if not keyword or not keyword.strip():
            return []
        session = self.Session()
        try:
            results = (session.query(Book).filter_by(Category = keyword).limit(50).all())
            if results:
                return [
                    {
                        "bookid": result.BookID,
                        "bookname":result.BookName,
                        "bookimage":result.BookImage,
                        "author":result.Author,
                        "category":result.Category,
                        "bookinfo":result.BookInfo,
                        "createdtime":result.CreatedTime.strftime("%Y-%m-%d")
                    }
                    for result in results
                    ]
            else:
                return []
        except Exception as e:
            print(str(e), flush=True)
            return []
        finally:
            session.close()

    def getsearchbook(self, keyword:str) ->list[dict]:
        """根据关键字搜索对应作者和书名"""
        if not keyword or not keyword.strip():
            return []
        session = self.Session()
        try:
            books = (session.query(Book).filter(or_(Book.BookName.ilike(f"%{keyword}%"),Book.Author.ilike(f"%{keyword}%"))).limit(50).all())

            seen = set()
            result = []
            for b in books:
                if b.BookID in seen:
                    continue
                seen.add(b.BookID)
                result.append(
                    {
                        "bookid": b.BookID,
                        "bookname":b.BookName,
                        "bookimage":b.BookImage,
                        "author":b.Author,
                        "category":b.Category,
                        "bookinfo":b.BookInfo,
                        "createdtime":b.CreatedTime.strftime("%Y-%m-%d")
                    }
                )
            return result
        except Exception as e:
            print(str(e))
            return []
        finally:
            session.close()

    def getbook(self, keyword:str) -> list[dict] | bool:
        """根据id获取书籍详情"""
        if not keyword:
            return[]
        session = self.Session()
        try:
            book = (session.query(Book).filter_by(BookID = int(keyword)).first())
            if book:
                return {
                        "bookid":book.BookID,
                        "bookname":book.BookName,
                        "bookimage":book.BookImage,
                        "author":book.Author,
                        "category":book.Category,
                        "bookinfo":book.BookInfo,
                        "state":book.BookState,
                        "createtime":book.CreatedTime.strftime("%Y-%m-%d"),
                        "updatetime":book.UpdateTime.strftime("%Y-%m-%d")
                    }
                
            else:
                return {}
        except Exception as e:
            print(str(e))
            return False
        finally:
            session.close()

    def getcategory(self) -> dict[str, list[dict]]:
        """获取类别内书籍列表"""
        session = self.Session()
        try:
            categories = (session.query(Book.Category).filter(Book.Category.isnot(None)).distinct().all())
            categorylist = [category[0] for category in categories]
            toplist = []
            for category in categorylist:
                books = session.query(Book).filter(Book.Category == category).all()
                booklist = [
                    {
                        "bookid":book.BookID,
                        "bookname":book.BookName,
                        "author":book.Author
                    }
                    for book in books
                ]
                toplist.append({
                    "category":category,
                    "booklist":booklist
                })
            return toplist
        except Exception as e:
            print(e)
            return []
        finally:
            session.close()

    def getbookid(self, bookname:str, author:str) -> int | bool:
        """获取书籍id"""
        session = self.Session()
        try:
            bookid = session.query(Book).filter(Book.BookName == bookname, Book.Author == author).first()
            if bookid:
                return bookid.BookID
            return False
        except Exception as e:
            print(e)
            return False
        finally:
            session.close()

    def setbook(self, bookname:str, author:str, bookimage:str, category:str, bookinfo:str) -> bool:
        """添加书籍"""
        session = self.Session()
        try:
            book = Book(BookName = bookname, Author = author, BookImage = bookimage, Category = category, BookInfo = bookinfo)
            session.add(book)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            print(str(e))
            return False
        finally:
            session.close()

    def delbook(self, bookid:int) -> bool:
        """删除书籍"""
        session = self.Session()
        try:
            book = session.query(Book).filter(Book.BookID == bookid).first()
            if not book:
                return False
            session.delete(book)
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print(e)
            return False
        finally:
            session.close()

    def changebook(self, bookname:str, bookinfo:str, author:str, bookimage:str, category:str) -> bool:
        """修改书籍信息"""
        session = self.Session()
        try:
            book = session.query(Book).filter_by(Author = author, BookName = bookname).first()
            if not book:
                return False
            book.BookName = bookname
            book.Author = author
            book.BookImage = bookimage
            book.BookInfo = bookinfo
            book.Category = category
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print(e)
            return False
        finally:
            session.close()

    def gettimebook(self) -> list[dict]:
        """获取时间排序的书籍列表"""
        session = self.Session()
        try:
            time = session.query(Book).order_by(Book.CreatedTime.desc()).limit(50).all()
            if time:
                return [
                    {
                        "bookid":book.BookID,
                        "bookname":book.BookName,
                        "author":book.Author,
                        "category":book.Category,
                        "createdtime":book.CreatedTime.strftime("%Y-%m-%d")
                    }
                    for book in time
                ]
            return []
        except SQLAlchemyError as e:
            print(e)
            return []
        finally:
            session.close()
