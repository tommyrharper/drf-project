# drf introduction

1. install the framework
```
pip install djangorestframework
```
2. Add `rest_framework` into your `INSTALLED_APPS` setting.

- serialization is the process of transforming django models into a python dict to be return as json.
- de-serialization is the opposite.

## two types of serializer

1. `serializers.Serializer`
2. `serializers.ModelSerializer`

## two types of views

1. class based => `APIView` class.
   - generic views
   - mixins
   - concrete view classes
   - viewsets
2. function based => `@api_view()`

