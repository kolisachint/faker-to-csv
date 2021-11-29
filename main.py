from fastapi import FastAPI,Request
from fastapi.responses import FileResponse
from faker import Faker
from resources.tableschema import TableSchema
from resources.request_response import post_response_json,get_response_json

import uvicorn
import json
import jsonschema
import pandas as pd
import os

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


# Dynamically create columns and data for the input
    dfheader=()
    dfdata=[]
    fields=json.loads(json.dumps(data_json))
    for field in fields:
        dfheader+=(field["name"],)
        dfdata.append(   getattr(Faker(), \
                        field["faketype"].split('.')[1].split('(')[0]   ) ) 

    df = pd.DataFrame(columns=dfheader)

    for i in range(int(numrows)):
        stuff = dfdata
        df.loc[i] = [item() for item in stuff]

    filepath=os.path.dirname(os.path.abspath(__file__))
    df.to_csv(filepath+"/output/"+tablename+".csv",index=False)
    return FileResponse(path=filepath+"/output/"+tablename+".csv", 
        filename=tablename+".csv", media_type='text/csv')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0',port=5000)    
