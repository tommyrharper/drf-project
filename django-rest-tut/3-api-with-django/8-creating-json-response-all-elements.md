# Creating json response all elements

1. go to `views.py` and create a `movie_list` function
2. hook up the urls in `watchmate/urls.py`:
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('watchlist_app.urls')),
]
```
3. add urls to `watchlist_app/urls.py`
4. return `JsonResponse` from `movie_list` function in `views.py`
- note `JsonResponse` requires a dictionary as an argument.