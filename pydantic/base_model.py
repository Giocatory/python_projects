from datetime import datetime
from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


external_data = {
    'id': 123,
    'signup_ts': '2023-07-01 13:00',
    'tastes': {
        'apple': 1,
        'banana': 2,
        'orange': 3,
    }
}

user = User(**external_data)

print(user)
# id=123
# name='John Doe'
# signup_ts=datetime.datetime(2023, 7, 1, 13, 0)
# tastes={'apple': 1, 'banana': 2, 'orange': 3}
print(user.id)
# 123
print(user.model_dump())
# {
#     'id': 123,
#     'name': 'John Doe',
#     'signup_ts': datetime.datetime(2023, 7, 1, 13, 0),
#     'tastes': {
#         'apple': 1,
#         'banana': 2,
#         'orange': 3
#     }
# }
