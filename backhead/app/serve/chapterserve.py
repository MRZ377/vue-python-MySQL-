from ..db.initdb import DB
from ..models.bookchapter import Bookchapters
from sqlalchemy.exc import SQLAlchemyError

class Chapterserve:
    def __init__(self):
        self.db = DB()
        self.db.create_tables()
        self.Session = self.db.Session

    def getchapterlist(self, keyword:str) -> list[dict] | bool:
        """根据书籍id获取章节列表"""
        session = self.Session()

        try:
            chapterlist = (session.query(Bookchapters).filter(Bookchapters.BookID == int(keyword)).all())
            if chapterlist:
                return [
                    {
                        "chapter_no":chapter.ChapterNO,
                        "title":chapter.ChapterTitle,
                        "url":f"/books/{chapter.BookID}/{chapter.ChapterNO}",
                        "createdtime":chapter.CreatedTime.strftime("%Y-%m-%d")
                    }
                    for chapter in chapterlist
                ]
            else:
                return []
        except Exception as e:
            print(e)
            return False
        
    def delchapterlit(self, keyword:str) -> bool:
        """删除对应书籍下所有章节"""
        session = self.Session()

        try:
            list = session.query(Bookchapters).filter_by(Bookchapters.BookID == int(keyword)).all()
            if not list:
                return False
            session.delete(list)
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print(e)
            return False
        finally:
            session.close()

    def delchapter(self, keyword:str, chaptertitle:str) -> bool:
        """删除对应章节"""
        session = self.Session()

        try:
            chapter = session.query(Bookchapters).filter_by(Bookchapters.ChapterTitle == chaptertitle, Bookchapters.BookID == int(keyword)).all()
            if not chapter:
                return False
            session.delete(chapter)
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print(e)
            return False
        finally:
            session.close()

    def setchapter(self, keyword:str, chaptertitle:str, chapterno:int) -> bool:
        """添加章节"""
        session = self.Session()

        try:
            chapter = Bookchapters(BookID = keyword,ChapterTitle = chaptertitle, ChapterNO = chapterno)
            session.add(chapter)
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print(e)
            return False
        finally:
            session.close()

    def gettitle(self, bookid:str, chapterno:str) -> str | bool:
        """获取文章标题"""
        session = self.Session()
        try:
            title = session.query(Bookchapters).filter_by(BookID = bookid, ChapterNO = chapterno).first()
            if title:
                return title.ChapterTitle
            return False
        except SQLAlchemyError as e:
            print(e)
            return False
        finally:
            session.close()

    def changechapter(self, bookid:str, chapter_no:str, new_chapter_no:str, title:str) -> bool:
        """修改章节信息"""
        session = self.Session()
        try:
            chapter = session.query(Bookchapters).filter_by(BookID = bookid, ChapterNO = chapter_no).first()
            if not chapter:
                return False
            chapter.ChapterNO = new_chapter_no
            chapter.ChapterTitle = title
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print(e)
            return False
        finally:
            session.close()
    
    def getchaptertime(self) -> list[dict]:
        """获取时间排序的章节列表"""
        session = self.Session()
        try:
            chapters = session.query(Bookchapters).order_by(Bookchapters.CreatedTime.desc()).limit(50).all()
            if chapters:
                return[
                    {
                        "bookid":chapter.BookID,
                        "title":chapter.ChapterTitle,
                        "chapterno":chapter.ChapterNO,
                        "createdtime":chapter.CreatedTime.strftime("%Y-%m-%d"),
                        "bookname":chapter.books.BookName,
                        "author":chapter.books.Author,
                        "category":chapter.books.Category
                    }
                    for chapter in chapters
                ]
            return []
        except SQLAlchemyError as e:
            print(e)
            return []
        finally:
            session.close()
