from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person : Person ={'name': 'John', 'age': 30} #it will also work in case of '30'

print(new_person)