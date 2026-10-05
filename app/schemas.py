from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field, StringConstraints

#We want a class that describes incoming data and a class that describes responses.
NameStr =Annotated[str, StringConstraints(min_length=2, max_length=50)] 
StudentIdStr = Annotated[str, StringConstraints(pattern=r"^S\d{7}$")]

#This arrives in, no id is known
class UserCreate(BaseModel):
   # user_id: int = Field(gt=0)    I missed removing this and it cost me hours --XD ;-D    name: NameStr
    email: EmailStr
    age: int = Field(gt=18, lt=120)
    student_id: StudentIdStr

#This is what we return, the id is known as the db created it.
class UserRead(BaseModel): 
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: NameStr 
    email: EmailStr
    age: int 
    student_id: StudentIdStr 
