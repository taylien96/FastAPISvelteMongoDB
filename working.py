from fastapi import FastAPI, Path

app = FastAPI()

inventory = {
    1: {
        "name": "milk",
        "price": 3.99
    }
}

@app.get("/")
def home():
    return {"Data": "Test"}

@app.get("/about/{item_id}")
def about(item_id: int = Path(None, description="The Id of the item you want")):
    return inventory[item_id]

@app.get("/get_name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
        return {"data" : "no exist"}