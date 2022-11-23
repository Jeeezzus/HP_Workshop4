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

@app.get("/todo")
async def list():
    return TODOLIST

@app.get("/todo/{item_id}")
async def root(item_id: int):
     it = find_item(item_id)
     return {(str(it.id)) + "; title: " + str(it.title) + ", date: " + str(it.date) + ", state: " + str(it.state) + ", description: " + str(it.desc)}

@app.post("/todo")
async def create_item(item: Item):
     TODOLIST.append(item)
     return item

@app.delete("/todo/{item_id}")
def delete_todo(item_id: int) -> None:
     item_to_remove = find_item(item_id)

     if item_to_remove is not None:
        TODOLIST.remove(item_to_remove)
     return item_to_remove


def find_item(id):
    for it in TODOLIST:
        if it.id == id:
            return it
    return None