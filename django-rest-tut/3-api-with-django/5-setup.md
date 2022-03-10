# Setup django rest

1. Create virtual .env (in this instance the name is menv for movie virtual environment)
```
python -m venv menv
```
2. Enter into venv
```
source menv/bin/activate
```
- you can now check if you have any installed packages:
```
pip freeze
```
- you should see nothing.

3. Go to djangoproject.com and install the latest version of django, e.g.
```
pip install Django==4.03
```
4. Update pip
```
python -m pip install --upgrade pip
```
- you can now use `pip freeze` to see the installed packages
  