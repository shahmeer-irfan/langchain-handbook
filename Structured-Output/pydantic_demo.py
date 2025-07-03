from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'nitish'
    age: Optional[int] = None #integer age with NULL default value
    email: EmailStr #automatically validates email string
    #you can add different constraints
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')


new_student = {'age':'32', 'email':'abc@gmail.com'}

student = Student(**new_student) #Pydantic Object

student_dict = dict(student) #converting into python dictionary

print(student_dict['age'])

student_json = student.model_dump_json() #json format

#default values 
#OptionalFields
#Builtin validation
#Field Function
#Returns Pydantic object and converts to json and dictionary