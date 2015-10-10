binbin-cms-django
=================

条件
====

docker,docker-compose

使用
====

创建docker
----------

```
git clone https://github.com/lotosbin/binbin-cms-django.git
cd binbin-cms-django
docker-compose up -d
```

创建数据库
----------

```
docker-compose run web /bin/bash
```

在docker中执行

```
python manager.py syncdb
```

参考
====

https://django-chinese-docs.readthedocs.org/en/latest/
