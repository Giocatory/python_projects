from pydantic import BaseModel


class MyModel(BaseModel):
    a: int
    b: list[str]


m = MyModel(a=23, b=['a', 'b', 'c'])
print(m.model_dump())  # {'a': 23, 'b': ['a', 'b', 'c']}
