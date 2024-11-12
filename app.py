# This code creates a simple FastAPI application

from fastapi import FastAPI #This imports the FastAPI class, which is the core of the framework used to build APIs.

app = FastAPI() #This line initializes an instance of the FastAPI class. The app object is used to define and configure the API routes.


@app.get("/")
# This is a route decorator that tells FastAPI to handle HTTP GET requests to the root URL (/). 
# This means when someone accesses the base URL of the application, this function will be executed.



# This defines an asynchronous function that will be executed when the root URL is accessed. 
# The async keyword allows for non-blocking operations, making it efficient for handling I/O-bound tasks.
async def root():
    return {"message": "Hello World, this is example"}
#This is the response sent back when the root URL is accessed. It returns a JSON object with a message key and the value "Hello World". 
# FastAPI automatically converts this Python dictionary into a JSON response
