#to start uvicorn working:app --reload

from fastapi import FastAPI, Path, Query, HTTPException, status, Body
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from model import Item, UpdateItem, Todo, UserBase, UserIn
from auth.jwt_handler import signJWT



app = FastAPI()

from database import(
    fetch_all_todos,
    fetch_one_movie,
    fetch_one_todo,
    create_todo,
    update_todo,
    remove_todo,
    check_if_user,
    create_user
)

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=['*'],
    allow_headers={'*'}
)

inventory = {
    
}

@app.get("/")
def home():
    return {"Data": "Test"}

@app.post("/api/signup", response_model=UserBase)
async def user_signup(user : UserIn):
    response = await check_if_user(user.username)
    print(response)
    if response == None:
        create = await create_user(user.dict())
        if create:
            return signJWT(user.username)
        raise HTTPException(400, "something went wrong, bad request")
    raise HTTPException(409, f"the name is taken")
    
@app.post("/api/login")
async def user_login(user: UserIn):






@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo(title: str):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"no todo item with {title}")

#response model helps the program know what we should be sending back!
@app.post('/api/todo', response_model=Todo)
async def post_todo(todo:Todo):
        response = await create_todo(todo.dict())
        if response:
            return response
        raise HTTPException(400, "something went wrong, bad request")

@app.put('/api/todo/{title}', response_model=Todo)
async def put_todo(title:str, desc:str):
    response = await update_todo(id, title, desc)
    if response:
        return response
    raise HTTPException(404, f"couldnt find the todo mate")


@app.delete("/api/todo/{title}")
async def delete_todo(title: str):
    response = await remove_todo(id)
    if response:
        return {'response' : 'deleted'}
    raise HTTPException(400, "it fricked up")












@app.get("/about/{item_id}")
def about(item_id: int = Path(None, description="The Id of the item you want")):
    return inventory[item_id]

@app.get("/get_name")
def get_item(name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Problem" : "item id already exists."}

    # inventory[item_id] = {"name": item.name, "brand": item.brand, "price": item.price}
    #is the same as
    inventory[item_id] = item
    return inventory[item_id]
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error":"Item id does not exist"}
    inventory[item_id] = item
    #if you dont want to change null values go through individuallly like
    #item.name ! = none
    #inventory[item_id].name = name  
    return inventory[item_id]
@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The id of the item deleted")):
    if item_id not in inventory:
        return {"error" : "item aint ther dawg"}
    del inventory[item_id]
    return{"success" : "zappppped"}