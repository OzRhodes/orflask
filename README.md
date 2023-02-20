# orflask


### Create Secret_Key from

>>>import secrets
>>>secrets.token_hex(16)
>>>provides16bytesofsecret

1. Created a dir 
2. Created the App
3. export FLASK-APP=app.py # this needs to be run from the folder
4. export FLASK_DEBUG=1
5. created templates folder
6. created a simple index.html 
7. created a base.html 
8. created a simple about, blog, contact html page
9. created a login page
10. add import render_template in app.py
11. added return render_template('file.html') for each route for each route i app.py
12. added dumy data as a list of dictionaries to add to the blog post template  
13. changed the blog.html to have a ist of posts
14. added 'if title' for all pages
15. added bootstrap
16. added nav bar
17. Added static folder
18. Added import url_for in app.py