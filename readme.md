# 请假审批管理系统

## 简介
从https://github.com/one-ccs/leave_approval_management_sys获取


请假管理审批管理系统，包含前后端及数据库操作。///

## 技术栈

前端：HTML、CSS、JavaScript、JQuery、JQuery-Confirm、Bootstrap 5、BootstraTable、BootstrapFileinput、FontAwesome 4

后端：Python、Flask、SQLite

## 功能
 1. 所有用户均可修改头像

### 登录 / 注册

1. 根据 id 登录并自动识别角色、获得对应权限、展示对应界面
2. 只提供学生注册功能（未来将取消该功能）

### 学生端

1. 请假
2. 销假
3. 查看历史请假信息

### 辅导员端

1. 可以直接通过请假时长在 3 天以内的请假条
2. 请假时长大于等于 3 天的请假条将由教务处再次确认
3. 驳回请假条
4. 同意销假申请
5. 同意及驳回均可批量操作
6. 查看所负责的所有学生请假信息

### 教务处端

1. 拥有辅导员的所有权限
2. 可直接通过请假时长超过 3 天的请假条

### 考勤端

1. 查看班级考勤信息

### 管理员端

1. 添加、删除、修改学生信息
2. 添加、删除、修改教师信息
3. 以上所有操作均可批量执行

## 部署

1. 电脑上安装 Python 3.7+

2. Python 安装 Flask 包，安装命令：pip install flask（在 cmd 中输入）

3. 双击 launch.py 运行服务器

4. 浏览器打开网址 [localhost:5000](http://localhost:5000/)


## 项目结构说明
请假系统为python flask 开发，数据库为sqlite3，以下为项目结构：

```
│─ .gitignore                       # git 忽略文件列表
│─  data_creator.py                  # 创建 data.db 数据库
│─  generate_password.py             # 生成加密密码
│─  launch.py                        # 启动文件
│─  readme.md                        # 项目文档

├─.idea                            # IDEA项目配置文件夹
├─app                              # Flask 项目主体
│  │  app.py                       # Flask 主程序
│  │  __init__.py                  # 程序初始化文件
│  │
│  ├─classes                       # 数据库模型
│  │  │  database.py               # 数据库模型
│  │  │  datetime.py               # 时间模型
│  │  │  role.py                   # 用户角色模型
│  │  │  student.py                # 学生模型
│  │  │  teacher.py                # 教师模型
│  │  │  user.py                   # 用户模型
│  │  │  __init__.py               # 初始化文件
│  │  │
│  │  └─__pycache__
│  │
│  ├─views                         # 视图文件
│  │  │  admin.py                  # 管理员视图
│  │  │  assistant.py              # 辅导员视图
│  │  │  attendance.py             # 学生考勤视图
│  │  │  errorhandle.py            # 错误处理视图
│  │  │  office.py                 # 教务处视图
│  │  │  student.py                # 学生视图
│  │  │  __init__.py               # 初始化文件
│  │  │
│  │  └─__pycache__
│  │
│  └─__pycache__
│
├─db                              # 数据库存放路径
│      data.db                     # 数据库文件

├─doc                             # 数据库设计文档
│      datadb参考手册.pdf

└─www                             # 网站前端
    ├─static                      # 静态资源
    │  │  favicon.ico             # 网站图标
    │  │
    │  ├─css                      # 样式文件
    │  │      bootstrap-icons.css # bootstrap 图标样式
    │  │      bootstrap-table.min.css # bootstrap 表格样式
    │  │      bootstrap.min.css   # bootstrap 样式
    │  │      bootstrap.min.css.map
    │  │      fileinput.min.css    # 文件上传插件
    │  │      font-awesome.min.css # font-awesome 图标样式
    │  │      jquery-confirm.min.css # 确认对话框插件
    │  │      static.css           # 自定义样式
    │  │
    │  ├─fonts                    # 字体文件
    │  │      bootstrap-icons.woff # bootstrap 图标字体
    │  │      bootstrap-icons.woff2
    │  │      fontawesome-webfont.woff # font-awesome 字体
    │  │      fontawesome-webfont.woff2
    │  │
    │  ├─img                     # 图片资源
    │  │  └─sundry
    │  │          camera.png
    │  │          default_headimg.webp
    │  │          loading-sm.gif
    │  │          loading.gif
    │  │          upload.png
    │  │
    │  ├─js                     # JavaScript 文件
    │  │      bootstrap-fileinput-theme.min.js # 文件上传插件
    │  │      bootstrap-fileinput-zh-CN.min.js
    │  │      bootstrap-fileinput.min.js
    │  │      bootstrap-table-zh-CN.min.js    # bootstrap 表格插件
    │  │      bootstrap-table.js
    │  │      bootstrap-table.min.js
    │  │      bootstrap.bundle.min.js        # bootstrap 插件
    │  │      bootstrap.bundle.min.js.map
    │  │      jquery-confirm.min.js           # 确认对话框插件
    │  │      jquery.min.js                   # jquery 插件
    │  │      static.js                       # 自定义 JavaScript
    │  │
    │  └─user_upload                          # 用户上传的头像
    │      └─headimg
    │              1202.webp
    │
    └─templates                                # HTML 模板
        │  admin.html
        │  assistant.html
        │  attendance.html
        │  base.html                           # 基础模板
        │  index.html
        │  office.html
        │  session.html
        │  student.html
        │
        └─includes                             # 模板 include 文件
                headcard.html
                top_navbar.html

```
