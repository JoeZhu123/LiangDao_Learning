#创建新的django项目
django-admin.py startproject RiskControl
#新建一个 view.py 文件,也就是后台代码中的LiangDao_view.py
#在其中写HTML的View类函数
#绑定 URL 与视图函数，更改urls.py
#新建templates,将html放在其中，修改settings.py，修改 TEMPLATES 中的 DIRS 为 [BASE_DIR+"/templates",]
#创建APP，定义模型
python manage.py startapp ControlModel
#修改 TestModel/models.py文件
#接下来在settings.py中找到INSTALLED_APPS这一项，添加'ControlModel',
#Run 'python manage.py migrate' to apply them
python manage.py migrate