from fastapi import FastAPI

app = FastAPI()

# here the web server return html/JSON
# when we send the data from the server to the web it should be in 
# the proper format there comes REST API
@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}