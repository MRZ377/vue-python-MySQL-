from flask import Flask,request,jsonify
from app.serve.bookserve import Bookserve
from app.serve.chapterserve import Chapterserve
from app.serve.userserve import Userserve
from app.serve.utial import ensure_book_dir,del_book_dir
from flask_cors import CORS
import os, bcrypt

app = Flask(__name__)
CORS(app)
BOOKS_DIR = os.path.join(os.path.dirname(__file__), 'books')
os.makedirs(BOOKS_DIR, exist_ok=True)

bookserve = Bookserve()
chapterserve = Chapterserve()
userserve = Userserve()

@app.route('/api/chaptertime', methods=['GET'])
def chaptertimelist() -> list[dict]:
    chapter = chapterserve.getchaptertime()
    return chapter

@app.route('/api/timelist', methods=['GET'])
def timelist() -> list[dict]:
    timelist = bookserve.gettimebook()
    return jsonify(timelist)

@app.route('/api/books', methods=['GET'])
def books() -> list[dict]:
    try:
        booklist = bookserve.getbooks()
        if booklist:
            return jsonify(booklist), 200
        else:
            return [], 500
    except Exception as e:
        print(str(e))
        return [], 500
    
@app.route('/api/categories/', methods=['GET'])
def categorybooks() -> list[dict]:
    keyword = request.args.get("category", "").strip()
    data = bookserve.getbookscategory(keyword)
    return jsonify(data), 200

@app.route('/api/search', methods=['GET'])
def search() ->list[dict]:
    keyword = request.args.get("q", "").strip()
    books = bookserve.getsearchbook(keyword)
    return jsonify(books), 200

@app.route('/api/top', methods=['GET'])
def top() -> list[dict]:
    try:
        categorylist = bookserve.getcategory()
        return jsonify(categorylist)
    except Exception as e:
        print(e)
        return [], 500

@app.route('/api/addbook', methods=['POST'])
def addbook() -> dict:
    data = request.json
    bookname = data.get("bookname")
    author = data.get("author")
    bookimage = data.get("bookimage")
    category = data.get("category")
    bookinfo = data.get("bookinfo")
    try:
        result = bookserve.setbook(bookname=bookname, author=author, bookimage=bookimage, category=category, bookinfo=bookinfo)
        bookid = bookserve.getbookid(bookname, author)
        if result:
             if ensure_book_dir(bookid=bookid, bookdir=BOOKS_DIR):
                return jsonify({"message":"添加成功"}), 200
        return jsonify({"message":"添加失败"}), 500
    except Exception as e:
        print(str(e))
        return jsonify({"message":"数据库错误"}), 500

@app.route('/api/addchapter', methods=['POST'])
def addchapter() -> dict:
    bookname = request.form.get('bookname','').strip()
    author = request.form.get('author','').strip()
    chaptername = request.form.get('chaptername','').strip()
    file = request.files.get('file')

    if not all([bookname, chaptername, author, file]):
        return jsonify({'message':'缺少参数'}), 400
    
    bookid = bookserve.getbookid(bookname, author)
    if not bookid:
        return jsonify({"message":"书籍不存在"}), 404
    
    book_path = os.path.join(BOOKS_DIR, str(bookid))
    existing_files = [f for f in os.listdir(book_path) if os.path.isfile(os.path.join(book_path, f))]
    numbers = [int(os.path.splitext(f)[0]) for f in existing_files if os.path.splitext(f)[0].isdigit()]
    next_num = max(numbers, default=0) + 1

    _,ext = os.path.splitext(file.filename or '')
    save_name = f'{next_num}{ext.lower()}'
    save_path = os.path.join(book_path, save_name)
    file.save(save_path)

    result = chapterserve.setchapter(keyword=bookid, chaptertitle=chaptername, chapterno=next_num)
    if result:
        return jsonify({"message":"章节添加成功"}), 200
    return jsonify({"message":"章节添加失败"}), 500

@app.route('/api/delbook', methods=['POST'])
def delbook():
    data = request.json
    bookname = data.get("bookname")
    author = data.get("author")
    try:
        bookid = bookserve.getbookid(bookname, author)
        result = bookserve.delbook(bookid)
        Cresult = chapterserve.delchapterlit(bookid)
        if result:
            if Cresult:
                if del_book_dir(bookid=bookid, bookdir=BOOKS_DIR):
                    return jsonify({"message":"删除成功"}), 200
        return jsonify({"message":"删除失败"}), 500
    except Exception as e:
        print(e)
        return jsonify({"message":"数据库错误"}), 500

@app.route('/api/content/<int:bookid>', methods=['GET'])
def chapters(bookid) -> list[dict]:
    try:
        chapterlist = chapterserve.getchapterlist(bookid)
        return jsonify(chapterlist), 200
    except Exception as e:
        print(e)
        return jsonify([])

@app.route('/api/book/<int:bookid>', methods=['GET'])
def getbook(bookid) -> list[dict]:
    try:
        book = bookserve.getbook(bookid)
        return jsonify(book), 200
    except Exception as e:
        print(e)
        return {}

@app.route('/api/content/<int:bookid>/<int:chapter_no>', methods=['GET'])
def getcontent(bookid, chapter_no) -> dict:
    file_path = os.path.join(BOOKS_DIR, str(bookid), f'{chapter_no}.html')
    title = chapterserve.gettitle(bookid, chapter_no)
    book = bookserve.getbook(bookid)
    if title:
        if not os.path.exists(file_path):
            return jsonify({"message":"抱歉，当前章节不存在"}), 404
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return jsonify({"content":content,"title":title,"bookname":book['bookname']})

@app.route('/api/login', methods=['POST'])
def login() -> dict:
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = userserve.getlogin(username)
    if not user:
        return jsonify({"message":"用户名或密码错误"}), 401
    if not bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        return jsonify({"message":"用户名或密码错误"}), 401
    return jsonify({"message":"登录成功","permission":user['permissions'], "username":user['username']}), 200
    
@app.route('/api/register', methods=['POST'])
def register() -> dict:
    data = request.get_json(silent=True) or {}
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    if not username and not password:
        return jsonify({"message":"用户名或密码为空"}), 400
    hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=6)).decode('utf-8')
    try:
        result = userserve.setuser(username=username, password=hash_password)
        if not result:
            return jsonify({"message":"用户已存在"}), 409
        return jsonify({"message":"注册成功"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message":"数据库错误"}), 500

if __name__ == '__main__':
    app.run(debug=True)