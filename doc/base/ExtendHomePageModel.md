给home页面追加一个body字段

# 修改home/models.py
1. 追加一个body字段为richtext，代码如下
    ```
    from django.db import models

    from wagtail.core.models import Page
    from wagtail.core.fields import RichTextField
    from wagtail.admin.edit_handlers import FieldPanel


    class HomePage(Page):
        body = RichTextField(blank=True)

        content_panels = Page.content_panels + [
            FieldPanel('body', classname="full"),
        ]
    ```

2. Run python manage.py makemigrations
   会在migrations目录下自动生成一个字段定义的文件
    ![](img/2021-05-01-23-27-02.png) 
3. then python manage.py migrate to update the database
   会生成数据库表的字段

# 修改home page template
文件在templates目录下命名规则为app名/model名.html
例如
![](img/2021-05-01-23-36-02.png)

追加mysite/templates/home/home_page.html如下

```
{% extends "base.html" %}

{% load wagtailcore_tags %}

{% block body_class %}template-homepage{% endblock %}

{% block content %}
    {{ page.body|richtext }}
{% endblock %}
```

# 在页面上编辑home page
填写title，body
![](img/2021-05-01-23-53-28.png)
点击save，publish

![](img/2021-05-01-23-54-28.png)
访问 localhost:8000 显示如下页面

![](img/2021-05-01-23-56-00.png)