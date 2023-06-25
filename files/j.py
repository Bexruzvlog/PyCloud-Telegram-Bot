import json
  
# Data to be written
dictionary ={
    "1944581117":{
    "audio":[],
    "video":[],
    "document":[],
    "rasm":[]
    }
}
  
with open("sample.json", "w") as outfile:
    json.dump(dictionary,outfile)
