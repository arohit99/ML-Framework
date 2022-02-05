# ML-Framework

After the dockerfile is created, we can deploy the app to heroku using the following steps:


- from project root directory

```bash
$ heroku login
$ heroku container:login
$ heroku create mlappframework
$ heroku container:push -a mlappframework web
$ heroku container:release -a mlappframework web
$ heroku open
```

```bash
$ docker build -t app:latest .
$ docker run -it -p 8501:8501 --name MLApp app:latest
```

check: http://localhost:8501/
check: https://mlappframework.herokuapp.com
