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

## 开始使用
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
