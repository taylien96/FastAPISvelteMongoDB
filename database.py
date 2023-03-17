from model import Item, UpdateItem
from dotenv import load_dotenv
import os
import motor.motor_asyncio

load_dotenv()
MONGO_SERVER = os.getenv('MONGO_URL')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_SERVER)