<p align="center">
  <h1 align="center"><b> 👨‍💻 Kubernetes Application Built using the FastApi Library </b></h1>
💭 A very guide on how to deploy your applications on Kubernetes
</p>

<details open="open">
  <summary><h2 style="display: inline-block">Project Details</h2></summary>
  <ol>
    <li><a href="#tech-stack">Tech Stack</a>
    </li>
    <li><a href="#project-description">Introduction</a></li>
    <li><a href="#prerequisitesn">Prerequisites</a></li>
    <li><a href="#fastapi">Setting Up the FastAPI Application</a></li>    
    <li><a href="#docker_fastapi">Dockerizing the FastAPI Application</a></li>
    <li><a href="#Kubernetes">Kubernetes</a></li>
    <li><a href="#minikube">Local Dev with Minikube</a></li>
    <li><a href="#challenges-closing">Challenges & Closing</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

- Built using the FastApi Python Library
- Docker
    - Built app and tag with `docker build -t k8s-fastapi" .`
    - Run the app using `docker run --port 8000:80  k8s-fastapi`
- To be deployed on K8s cluster

### Project Details
---------------- 
This is the K8s-FastApi application built using Kubernetes & the FastAPI library. This project aims to showcase how to deploy a FastApi application on a local Kubernetes cluster - Minikube

### Introduction  🤔
---------------- 
Why a FastApi application? The FastAPI library makes it easier to set up rest endpoints enabling the developer to focus on other aspects of the project. It's fast, lightweight, and very intuitive to use. As someone big on documentation, it automatically generates detailed API documentation based on the Python-type hints in your code. This not only serves as documentation but also helps developers understand the API's structure and use it effectively. Some notable mentions:
- FastAPI includes built-in support for OAuth and JWT (JSON Web Tokens), making it easier to implement authentication and authorization in your applications.
- Seamless integration with other services such as Docker, GraphQL, and other frontend frameworks

###  🛠️ Prerequisites
---------------- 
Excited? Me too! But before we embark on this journey, let's make sure you've got the essentials:
- **Your Coding Toolbox:** Bring along your Python skills and a pinch of experience with other libraries.
- **Kubernetes Basics:** No need to be a pro; we're here to guide you through the Kubernetes landscape.
- **Docker Know-How:** A basic understanding of containers and images will do wonders.
- **Minikube Setup:** Don't worry; there's got a simple minikube guide for [Minikube Installation](https://minikube.sigs.k8s.io/docs/start/).

### Tech Stack
---------------- 
- Kubernetes
- Docker
- Python FastApi Library

### Setting Up the FastAPI Application
---------------- 
We'll walk through the process of setting up a FastAPI application that manages a list of items. In this section, we will show you how to set up a simple FastAPI application that can perform CRUD (Create, Read, Update, Delete) operations on a JSON file. The JSON file would serve as our `mock` database. Ideally you would want to use a SQL or NO-SQL database for this purpose

## Prerequisites
To follow this guide, you will need:

- Python 3.6 or higher installed on your system.
- A text editor or IDE of your choice.
- A terminal or command prompt to run the commands.

## Creating the project directory and files
First, create a new directory for your project and navigate to it. For example:
```bash
mkdir fastapi-crud
cd fastapi-crud
```
Next, create a virtual environment and activate it. For example:
```
python -m venv env
source env/bin/activate # Linux or macOS
env\Scripts\activate # Windows
```

Then, install FastAPI and its dependencies using pip:

```python
pip install fastapi[all]
```

This will install FastAPI, Uvicorn (an ASGI server), Pydantic (a data validation library), and other optional packages.

Now, create a file named `items.json` in your project directory and paste the following content:

```json
[
  {
    "id": 1,
    "name": "Apple",
    "price": 0.99
  },
  {
    "id": 2,
    "name": "Banana",
    "price": 0.79
  },
  {
    "id": 3,
    "name": "Orange",
    "price": 0.89
  }
]
```
This file will serve as our mock database for storing items.

Finally, create a file named main.py in your project directory and paste the code that is provided:
[main.py](./app/main.py#L1-L23)
```python
from typing import Optional
import json
import os
from fastapi import FastAPI
from pydantic import BaseModel

# Update the file path to point to the correct location
file_path = os.path.join(os.path.dirname(__file__), 'items.json')
app = FastAPI()

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float

with open(file_path, 'r') as f:
    items = json.load(f)

```
In the following code, we are setting up a Pydantic model named `Item`. It specifies the structure of an item, including an `optional id`, a required `name`, and a **required** `price`.

#### Get
[main.py](./app/main.py#L27-L34)
These lines create two routes, one for the welcome message and the other one to return all the items in the JSON file

#### Post
[main.py](./app/main.py#L37)
This endpoint creates a new item and adds it to the JSON file, generating a  unique id for the item if not provided or already exists

#### Delete
[main.py](./app/main.py#L69)
This endpoint deletes an existing item by its id, returning a success message if the item is found and deleted. Else, it returns an error message if the item is not found
### Put
[main.py](./app/main.py#L58)

## Running the application
To run the application, use the following command:

```python 
uvicorn main:app --reload
```

This will start the Uvicorn server on http://127.0.0.1:8000 and reload the application whenever you make changes to the code.

You can now test your application using a web browser or a tool like curl or Postman. For example, to get all the items, you can use:

```bash
curl http://127.0.0.1:8000/items/
```

To create a new item, you can use:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Mango", "price": 1.29}' http://127.0.0.1:8000/items/
```

To update an existing item, you can use:

curl -X PUT -H "Content-Type: application/json" -d '{"id": 2, "name": "Banana", "price": 0.69}' http://127.0.0.1:8000/items/2

To delete an item, you can use:

```bash
curl -X DELETE http://127.0.0.1:8000/items/3
```

### Generating documentation
One of the great features of FastAPI is that it automatically generates interactive documentation for your API using OpenAPI and Swagger UI. To access the documentation, visit http://127.0.0.1:8000/docs in your browser. You will see something like this:

![Swagger UI]

You can use the documentation to explore and test your API endpoints. You can also download the OpenAPI schema as a JSON file by clicking on the Download button at the top right corner.

Another option for documentation is ReDoc, which provides a more minimalist and responsive interface. To access ReDoc, visit http://127.0.0.1:8000/redoc in your browser. You will see something like this:

![ReDoc]

You can use ReDoc to view the details and examples of your API endpoints. You can also expand and collapse the sections by clicking on the headers.
### Dockeririzing the app
---------------- 

### Kubernetes
---------------- 

### Local Dev with Minikube
---------------- 

### Challenges & Closing
---------------- 

