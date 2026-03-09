from fastapi import FastAPI, Query, Path,HTTPException, status, Body
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from database import cars

class Car(BaseModel):
    make:Optional[str]
    model:Optional[str]
    year: Optional[int] = Field(...,ge=1970,le=2026)
    price: Optional[float]
    engine: Optional[str] = "V4"
    autonomous: Optional[bool]
    sold: Optional[List[str]]

app = FastAPI()

@app.get("/")
def root():
    return {"Welcome to": "Your first API in FastAPI"}

@app.get("/cars", response_model=List[Dict[int,Car]])
def get_cars(number: Optional[int] = Query(10, ge=1, le=100)):
    # response = []
    # for id , car in list(cars.items())[:int(number)]:
    #     to_add = {}
    #     to_add[id] = car
    #     response.append(to_add)
    # return response

    ## List comprehension apporoach 
    return [{id: car} for id , car in list(cars.items()) ] [:int(number)]

@app.get("/cars/{id}", response_model=Car)
def get_car_by_id(id: int=Path(...,ge=0,lt=1000)):
    car = cars.get(id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Could not find car by ID")
    return car


@app.post("/cars", status_code=status.HTTP_201_CREATED)
def add_cars(body_cars: List[Car] = Body(...), min_id:int = Body(0)):
    if not body_cars:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)
    current_max_id = max(cars) if cars else 0
    next_id = max(current_max_id, min_id) + 1

    for car in body_cars:
        cars[next_id] = car
        next_id += 1
    return {"mesage": f'Sucessfully added {len(body_cars)} cars'}

@app.put("/cars/{id}", response_model=Dict[int,Car])
def update_car(id:int=Path(...), update_car: Car=Body(...)):
    if id not in cars:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with ID {id} not found"
            )
    stored_car = cars[id]
    stored_car_model = Car(**stored_car)

    update_dict = update_car.model_dump(exclude_unset=True)

    update_car = stored_car_model.model_copy(update=update_dict)

    cars[id] = jsonable_encoder(update_car)

    return {id: cars[id]}

@app.delete("/cars/{id}", status_code=status.HTTP_200_OK)
def delete_car(id:int=Path(...)):
    if id not in cars:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Car with ID {id} not found"
                             )
    del cars[id]
        

