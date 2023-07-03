import os

json_text = os.system("pip list --format=json")
print(type(json_text))  # int

# [{"name": "annotated-types", "version": "0.5.0"}, {"name": "pip", "version": "23.1.2"}, {"name": "pydantic",
# "version": "2.0"}, {"name": "pydantic_core", "version": "2.0.1"}, {"name": "setuptools", "version": "68.0.0"},
# {"name": "typing_extensions", "version": "4.7.0"}, {"name": "wheel", "version": "0.40.0"}]
# <class 'int'>
