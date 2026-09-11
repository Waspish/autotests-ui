from pydantic import BaseModel, HttpUrl, ValidationError


class MyModel(BaseModel):
    url: HttpUrl


m = MyModel(url="http://www.example.com")
print(m.url)
# > http://www.example.com/

try:
    MyModel(url="ftp://invalid.url")
except ValidationError as e:
    print(e)
    """
    1 validation error for MyModel
    url
      URL scheme should be 'http' or 'https'
        [type=url_scheme, input_value='ftp://invalid.url', input_type=str]
    """
