# flask-tea
Flask Web API Wheel.

## 项目结构
- /app 应用包
  - /api 接口包
  - /config 配置包
  - /exception 异常处理包
  - /lib 工具包
  - /model 模型包
  - /service 业务包
  - /static 静态资源目录
  - /template 模板目录
  - /validator 校验包
- /log 日志目录
- /test 测试包
- .flaskenv Flask环境变量文件
- starter.py 启动文件

**包名规范：** 一律使用小写单数形式

## 环境变量
|参数|作用|
|---|---|
|APP_NAME|应用名称|
|SECRET_KEY|项目密钥|
|SQLALCHEMY_DATABASE_URI|数据库URI

## 开始使用
```
flask run
flask routes
flask db init
flask db migrate
flask db upgrade
```
