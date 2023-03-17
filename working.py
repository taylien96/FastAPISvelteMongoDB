from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None
class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None
inventory = {
    
}

@app.get("/")
def home():
    return {"Data": "Test"}

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