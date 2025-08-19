import os, shutil

def ensure_book_dir(bookid:int, bookdir) -> bool:
    """创建对应书籍id的文件夹存储章节"""
    bookdir = os.path.join(bookdir, str(bookid))
    if not os.path.isdir(bookdir):
        os.makedirs(bookdir)
        return True
    return False

def del_book_dir(bookid:int, bookdir) ->bool:
    """删除对应书籍id的文件夹"""
    bookdir = os.path.join(bookdir, str(bookid))
    if os.path.isdir(bookdir):
        try:
            shutil.rmtree(bookdir)
            return True
        except Exception as e:
            print(e)
            return False
    return False
