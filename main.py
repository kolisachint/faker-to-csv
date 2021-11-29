from fastapi import FastAPI,Request
from fastapi.responses import FileResponse
from faker import Faker
from resources.tableschema import TableSchema
from resources.request_response import post_response_json,get_response_json

import uvicorn
import json
import jsonschema
import pandas as pd

app=FastAPI()
faker=Faker()
schema_json={}


def validate_json(_data, _schema):
    try:
        jsonschema.validate(_data, _schema)
        return True
    except jsonschema.ValidationError as e:
        return e.message


@app.post("/FakeCSVForSchema")
async def fakeCSVForSchema(request:Request):        
    data_json=await request.json()
    valid_json=validate_json(data_json,TableSchema)
    if (valid_json !=True):
        return post_response_json["Response_400"] 
    
    fields=json.loads(json.dumps(data_json))


    with open("output/table.csv","w") as outputfile:
        for i in range(1):
            for field in fields:
                outputfile.writelines(field["description"])
    return FileResponse(path="output/table.csv", filename="table.csv", media_type='text')



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0',port=5000)    
