from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

TODOLIST = []

class Item(BaseModel):
          id: int
          title: str
          state: int
          date: str
          desc: str

@app.get("/todo") #get all items on the TODOLIST
async def list():
    return TODOLIST

@app.get("/todo/{item_id}") #get specific item datas depending on the id
async def root(item_id: int):
     it = find_item(item_id)
     return {(str(it.id)) + "; title: " + str(it.title) + ", date: " + str(it.date) + ", state: " + str(it.state) + ", description: " + str(it.desc)}

@app.post("/todo") #add a todo with a json input
async def create_item(item: Item):
     TODOLIST.append(item)
     return item

@app.delete("/todo/{item_id}") #delete specific item
def delete_todo(item_id: int) -> None:
     item_to_remove = find_item(item_id)

     if item_to_remove is not None:
        TODOLIST.remove(item_to_remove)
     return item_to_remove


def find_item(id): #input id output item
    for it in TODOLIST:
        if it.id == id:
            return it
    return None