from datetime import datetime
from typing import List, Optional, Union
from fastapi import FastAPI, File, Form, UploadFile
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from forms import loginForm

from models import user
from core import database, hashing, JWTtokens
from schemas import authentication_schema

router = APIRouter(
    tags=["User Authentication"]
)


# Login
@router.post('/user-login/{user_type}')
# request:.... means that the 'request' depends upon "OAuth2PasswordRequestForm"
# whatever is returned by 'oau..' will be the value of 'request'
def login(user_type: int, response: Response, data: authentication_schema.Login, db: Session = Depends(database.get_db)):
    hired_user = db.query(user.User).filter(
        user.User.email == data.email, user.User.user_type == user_type).first()

    print(hired_user)

    # check if this user exists
    if not hired_user:
        print("yaha gayo ta?")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid Credentials")

    # checking for the password
    if not hashing.Hash.verify_password(data.password, hired_user.password):
        print("yaha gayo ki k")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect Password")

    # if email/username and password is correct.
    # get the token generated by 'create_access_token()'
    # access_token_expires = timedelta(minutes=30)  # for setting expiry time.
    access_token = JWTtokens.create_access_token(
        data={"sub": hired_user.email})
    response.set_cookie("hiredToken", access_token)
    return {"msg": "Success"}

    # return {"access_token": access_token, "token_type": "bearer"}


@router.get('/user-logout')
async def logout(response: Response):
    # Remove the user
    response.delete_cookie("hiredToken")

    return {"msg": "success"}
