# ML-Framework

After the dockerfile is created, we can deploy the app to heroku using the following steps:
- from project root directory
- 
$ heroku login
$ heroku container:login
$ heroku create mlappframework
$ heroku container:push -a mlappframework web
$ heroku container:release -a mlappframework web
$ heroku open