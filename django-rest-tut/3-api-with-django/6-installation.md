# Installation

1. Ensure you are in the root folder of the project and in the venv
2. Create your project
```
django-admin startproject watchmate
```
<!-- (optional) install vs code extension `Tabnine AI Autocomplete` and also `Python Extension Pack`. -->
3. create app app
```
cd watchmate
python manage.py startapp watchlist_app
```
4. run the server
```
python manage.py runserver
```
- grab the ip from the terminal, e.g. `http://127.0.0.1:8000/` and visit it in the browser.