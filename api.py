from fastapi import FastAPI,HTTPException
from opa_middleware import OPAMiddleware
from pydantic import BaseModel

app=FastAPI()

# adding middleware to the api
app.add_middleware(OPAMiddleware,opa_url="http://localhost:8181")

items = [{"item_1": "fruits"},{"item_2": "vegetables"}]
datas = [{"data_1": "123"}, {"data_2": "456"}]

class Item(BaseModel):
   name: str
   category: str

class Data(BaseModel):
   name: str
   category: str

@app.post("/items")
async def add_item(item:Item):
   items.append({item.name: item.category})
   return {"item": item}  

@app.get("/items")
async def read_items():
  return items

@app.put("/items/{item_name}")
async def update_item(item_name: str, item: Item):
    for index, existing_item in enumerate(items):
        if item_name in existing_item:
            items[index] = {item.name: item.category}
            return {"message": "Item updated successfully", "item": item}
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_name}")
async def delete_item(item_name: str):
    for index, existing_item in enumerate(items):
        if item_name in existing_item:
            items.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found") 

@app.post("/data")
async def add_data(data_item:Data):
   new_data = {data_item.name: data_item.category}
   datas.append(new_data)
   return {"message": "Data added successfully", "new_data": new_data}

@app.get("/data")
async def read_data():
    return datas

@app.put("/data/{data_name}")
async def update_data(data_name: str, data: Data):
    for index, existing_data in enumerate(datas):
        if data_name in existing_data:
            datas[index] = {data.name: data.category}
            return {"message": "Data updated successfully", "data": data}
    raise HTTPException(status_code=404, detail="Data not found")


@app.delete("/data/{data_name}")
async def delete_data(data_name: str):
    for index, existing_data in enumerate(datas):
        if data_name in existing_data:
            datas.pop(index)
            return {"message": "Data deleted successfully"}
    raise HTTPException(status_code=404, detail="Data not found")
