# 请假审批管理系统

## 简介
从https://github.com/one-ccs/leave_approval_management_sys获取


请假管理审批管理系统，包含前后端及数据库操作。///

## 技术栈

前端：HTML、CSS、JavaScript、JQuery、JQuery-Confirm、Bootstrap 5、BootstraTable、BootstrapFileinput、FontAwesome 4

后端：Python、Flask、SQLite 师兄是个大帅逼啊

## 功能

> 1. 所有用户均可修改头像

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
