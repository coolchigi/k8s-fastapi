from typing import Optional
import json
from fastapi import FastAPI
from pydantic import BaseModel



# simple python application

app = FastAPI()

# need to install splunk otel package in application
# need to install open telemetry/instrimentation pacakge


class Item(BaseModel):
  id: Optional[int] = None
  name: str
  price: float


with open('items.json', 'r') as f:
  items = json.load(f)


@app.get("/")
def read_root():
  return {"Hello ": "From My Kubernetes App"}


@app.get("/items/")
def get_items():
  return items


@app.post("/items/")
def create_item(item: Item):
  item_id = max([p['id'] for p in items]) + 1
  new_item = {"id": item_id, "name": item.name, "price": item.price}
  items.append(new_item)
  with open('items.json', 'w') as f:
    json.dump(items, f)
  return new_item


@app.get("/items/{item_id}")
def get_item(item_id: int):
  item = [i for i in items if i['id'] == item_id]
  return item[0] if len(item) > 0 else {}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
  for i, db_item in enumerate(items):
    if db_item["id"] == item_id:
      items[i] = item.dict()
      with open('items.json', 'w') as f:
        json.dump(items, f)
      return {"message": "Item updated successfully"}
  return {"message": "Item not found"}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
  for i, item in enumerate(items):
    if item["id"] == item_id:
      items.pop(i)
      with open('items.json', 'w') as f:
        json.dump(items, f)
      return {"message": "Item deleted successfully"}
  return {"message": "Item not found"}
