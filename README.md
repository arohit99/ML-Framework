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
$ docker run -it -p 8501:8501 --name MLApp app:v3
```

check: http://localhost:8501/
