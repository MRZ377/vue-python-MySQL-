## vue项目的启动
cd ./fontend  
npm install  
npm run serve  

## python项目的启动
cd ./backhead  
pip install -r requirements.txt  
python app.py  
启动之前需将.env中的数据库配置文件修改为自己的数据库配置  
在启动之前确保安装了MySQL数据库，个人使用的数据库版本为8.0.42，其他版本是否有冲突未进行测试

## gunicorn启动生产服务器，nginx进行代理和反向代理
npm run build 构建前端项目  
配置nginx和gunicorn文件，需注意对应服务的权限管理，通常nginx和gunicorn运行之后权限不足，无法进行文件夹和数据库的修改  
在数据库中设置对应用户并赋予权限，将backhead中的books文件夹的权限赋予对应服务（需有books文件夹）  
若无books文件夹，需要一键启动，可在app.py中修改基础路径后进行对应文件夹权限的赋予  

个人学习作品
