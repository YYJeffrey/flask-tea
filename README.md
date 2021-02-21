# Flask-Tea
Flask Web API Wheel.

## 项目结构
- /app 应用包
  - /api 接口包
  - /config 配置包
  - /lib 工具包
    - enums.py 枚举模块
    - exception.py 异常处理模块
    - red_print.py 红图模块
    - token.py 令牌模块
    - schema.py 视图结构模块
  - /model 模型包
  - /patch 补丁包
  - /service 业务包
  - /static 静态资源目录
  - /template 模板目录
  - /validator 校验包
- .flaskenv Flask环境变量文件
- .env 专属环境变量文件
- starter.py 启动文件

**包名规范：** 一律使用小写单数形式

## 前期准备

1. 开发环境
    - MySQL 5.7.28
    - Python 3.7.9
    - Pipenv 2020.11.15
    - Pycharm 2019.3

2. 安装依赖

    ```shell script
    pipenv install
    ```

3. 配置Pycharm

    将以下环节变量配置在Pycharm启动项下或系统环境变量下

    |参数|作用|
    |---|---|
    |APP_NAME|应用名称|
    |SECRET_KEY|项目密钥|
    |SQLALCHEMY_DATABASE_URI|数据库URI|
    
    配置Pycharm的启动项，分别填写每一个运行项的模块名、参数和环境变量
    
    <div>
        <img alt="pycharm" src="media/image/pycharm.png" width="520px" />
    </div>

    
4. 建立数据库

    创建一个名为 **tea** 的数据库，字符集 **utf8mb4**，排序规则 **utf8mb4_general_ci**

## 开发使用
```shell script
# 初始化数据库
flask db init

# 生成迁移脚本
flask db migrate

# 更新数据库模型
flask db upgrade

# 查看注册的路由
flask routes

# 运行项目
flask run
```

## 生产使用
```shell script
# 运行
gunicorn -c gconfig.py starter:app

# 停止
ps aux | grep gunicorn | awk '{print $2}' | xargs kill -9
```

## Docker部署
```shell script
# 导出依赖
pipenv lock -r >> requirements.txt

# 构建Dockerfile
docker build -t flask-tea .

# 运行Docker容器
docker run -d -p 5000:5000 --name flask-tea flask-tea
```

## 前端调用
填写请求头
```shell script
X-App-Name: FLASK-TEA
Authorization: Token eyJhbGciOiJIUzUxMiIsImlhdCI6MTYxMzI3OTgzMywiZXhwIjoxNjEzODg0NjMzfQ.eyJ1c2VyX2lkIjoiNzZkMGUzMWQwOGJmNDFkZGEyYzRmYTc1Nzg4NjVlZGMifQ.Fls-CVfHRYKYae7cu01pBqTzZu9Zt6HGM_BQkXas5pMF039XhUwuWr6xlEd_vKVmhVEzUFFGfQgJ4tUnXCQ5Zw
```

## 文章
[Flask构建Web API Wheel（一）—— Python版本选择](https://www.yejiefeng.com/articles/2021/01/27/1611747209253.html)

[Flask构建Web API Wheel（二）—— 虚拟环境工具选择](https://www.yejiefeng.com/articles/2021/01/29/1611924269587.html)

[Flask构建Web API Wheel（三）—— Flask及其依赖选择](https://www.yejiefeng.com/articles/2021/01/31/1612090572278.html)

[Flask构建Web API Wheel（四）—— 项目结构组织及启动](https://www.yejiefeng.com/articles/2021/02/02/1612278302145.html)

[Flask构建Web API Wheel（五）—— 多环境配置](https://www.yejiefeng.com/articles/2021/02/03/1612366632442.html)

[Flask构建Web API Wheel（六）—— 数据库操作基类](https://www.yejiefeng.com/articles/2021/02/16/1613448163988.html)

[Flask构建Web API Wheel（七）—— 异常处理](https://www.yejiefeng.com/articles/2021/02/16/1613450751289.html)

[Flask构建Web API Wheel（八）—— WTForms校验](https://www.yejiefeng.com/articles/2021/02/16/1613455540067.html)

[Flask构建Web API Wheel（九）—— 认证授权](https://www.yejiefeng.com/articles/2021/02/16/1613459929904.html)

[Flask构建Web API Wheel（十）—— 项目生产部署](https://www.yejiefeng.com/articles/2021/02/20/1613834443684.html)
