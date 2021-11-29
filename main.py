from fastapi import FastAPI,Request
from fastapi.responses import FileResponse
from starlette.responses import FileResponse
from faker import Faker
from resources.tableschema import TableSchema
from resources.request_response import post_response_json,get_response_json

import uvicorn
import json
import jsonschema
import pandas as pd

app=FastAPI()
fake=Faker()
schema_json={}
numrows=10

def validate_json(_data, _schema):
    try:
        jsonschema.validate(_data, _schema)
        return True
    except jsonschema.ValidationError as e:
        return e.message


@app.post("/FakeCSVForSchema")
async def fakeCSVForSchema(request:Request):        
    numrows=request.headers.get("NumofRows")
    tablename=request.headers.get("TableName")

    data_json=await request.json()
    valid_json=validate_json(data_json,TableSchema)
    if (valid_json !=True):
        return post_respognse_json["Response_400"] 

    print(numrows)

    fields=json.loads(json.dumps(data_json))
#    for field in fields:
#        outputfile.writelines(field["description"])

# Dynamically create columns and data for the input


    df = pd.DataFrame(columns=('name'
        , 'email'
        , 'bs'
        , 'address'
        , 'city'
        , 'state'
        , 'date_time'
        , 'paragraph'
        , 'Conrad'))

    for i in range(int(numrows)):
        stuff = [fake.name()
            , fake.email()
            , fake.bs()
            , fake.address()
            , fake.city()
            , fake.state()
            , fake.date_time()
            , fake.paragraph()
            , fake.catch_phrase()]

        df.loc[i] = [item for item in stuff]

    df.to_csv("output/"+tablename+".csv")
    return FileResponse(path="output/"+tablename+".csv", 
        filename=tablename+"csv", media_type='text/csv')



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0',port=5000)    
