from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# simple Querry
@app.get("/")
def greet():
    return{
        "message":"Hello, FastAPI"
    }


# Parameteried Querry
@app.get("/add/{num1}+{num2}")
def add(num1 : int  , num2 : int):
    return{
        "result" : num1 + num2
    }

#optional Querry
@app.get("/power/{num}")
def power(num : int  , pow : Optional[int] = 1):
    return{
        "result" : num ** pow
    }

# examples


@app.get("/fullname/{first_name}_{last_name}")
def FullName(first_name : str , last_name : str):
    return{
        "full_name" : first_name.title() + " " + last_name.title()
    }