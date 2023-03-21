from model import Item, UpdateItem, Todo
from dotenv import load_dotenv
import os
import motor.motor_asyncio

load_dotenv()
MONGO_SERVER = os.getenv('MONGO_URL')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_SERVER)
dbTodo = client.TodoList
collectionTodo = dbTodo.todo
dbMovie = client.sample_mflix
collectionMovie = dbMovie.movies
dbUsers = client.Users
collectionUsers = dbUsers.profiles
collectionSessions =dbUsers.sessions

async def check_if_user(username):
    document = await collectionUsers.find_one({"username":username})
    print(document)
    return document


async def fetch_one_todo(title):
    document = await collectionTodo.find_one({"title":title})
    print(document)
    return document

async def fetch_one_movie(title):
    document = await collectionMovie.find_one({"title":title})
    print(document)
    return document

async def fetch_all_todos():
    todos = []
    cursor = collectionTodo.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    print(cursor)
    return todos

async def create_todo(todo):
    document = todo
    result = await collectionTodo.insert_one(document)
    print(result)
    return document

async def update_todo(title, desc):
    await collectionTodo.update_one({"title":title},{"$set": {
        "description":desc}})
    document = await collectionTodo.find_one({"title":title})
    print(document)
    return document

async def remove_todo(title):
    await collectionTodo.delete_one({"title": title})
    return {"success" : "true"}