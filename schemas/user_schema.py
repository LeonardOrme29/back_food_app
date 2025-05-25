from pydantic import BaseModel, EmailStr

class User(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr

class RegisterResponse(BaseModel):
    message: str
    email: EmailStr
