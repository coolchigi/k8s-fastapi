<p align="center">
  <h1 align="center"><b> 👨‍💻 Kubernetes Application Built using the FastApi Library </b></h1>
💭 A very guide on how to deploy your applications on Kubernetes
</p>

<details open="open">
  <summary><h2 style="display: inline-block">Project Details</h2></summary>
  <ol>
    <li><a href="#tech-stack">Tech Stack</a>
    </li>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#setting-Up-the-FastAPI-Application">Setting Up the FastAPI Application</a></li>    
    <li><a href="#dockerizing-the-app">Dockerizing the app</a></li>
    <li><a href="#kubernetes-Local-Dev-With-Minikube">Kubernetes: Local Dev with Minikube</a></li>
    <li><a href="#challenges-closing">Challenges & Closing</a></li>
  </ol>
</details>


### Project Details
---------------- 
This is the K8s-FastApi application built using Kubernetes & the FastAPI library. This project aims to showcase how to deploy a FastApi application on a local Kubernetes cluster - Minikube

### Introduction  🤔
---------------- 
Why a FastApi application? The FastAPI library makes it easier to set up rest endpoints enabling the developer to focus on other aspects of the project. It's fast, lightweight, and very intuitive to use. As someone big on documentation, it automatically generates detailed API documentation based on the Python-type hints in your code. This not only serves as documentation but also helps developers understand the API's structure and use it effectively. Some notable mentions:
- FastAPI includes built-in support for OAuth and JWT (JSON Web Tokens), making it easier to implement authentication and authorization in your applications.
- Seamless integration with other services such as Docker, GraphQL, and other frontend frameworks

### Prerequisites  🛠️
---------------- 
Excited? Me too! But before we embark on this journey, let's make sure you've got the essentials:
- **Your Coding Toolbox:** Bring along your Python skills and a pinch of experience with other libraries.
- **Kubernetes Basics:** No need to be a pro; we're here to guide you through the Kubernetes landscape.
- **Docker Know-How:** A basic understanding of containers and images will do wonders.
- **Minikube Setup:** Don't worry; there's a simple minikube guide for installation here [Minikube Installation](https://minikube.sigs.k8s.io/docs/start/).

### Tech Stack
---------------- 
- Kubernetes
- Docker
- Python FastApi Library

### Setting Up the FastAPI Application  ⚡
---------------- 
We'll walk through the process of setting up a FastAPI application that manages a list of items. In this section, we will show you how to set up a simple FastAPI application that can perform CRUD (Create, Read, Update, Delete) operations on a JSON file. The JSON file would serve as our `mock` database. Ideally you would want to use a SQL or NO-SQL database for this purpose

#### App Prerequisites
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
[Get routes](./app/main.py#L27-L34)
These lines create two routes, one for the welcome message and the other one to return all the items in the JSON file

#### Post
[Post Route](./app/main.py#L37)
This endpoint creates a new item and adds it to the JSON file, generating a  unique id for the item if not provided or already exists

#### Delete
[Delete Route](./app/main.py#L69)
This endpoint deletes an existing item by its id, returning a success message if the item is found and deleted. Else, it returns an error message if the item is not found
### Put
[Put Route](./app/main.py#L58) 
This endpoint updates an existing item by its id returning a success message if the item is found and updated. Else It returns an error message if the item is not found

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
One of the great features of FastAPI is that it automatically generates interactive documentation for your API using OpenAPI and Swagger UI. To access the documentation, visit `http://127.0.0.1:8000/docs` in your browser. You will see something like this:

![Swagger UI]

You can use the documentation to explore and test your API endpoints. You can also download the OpenAPI schema as a JSON file by clicking on the Download button at the top right corner.

Another option for documentation is ReDoc, which provides a more minimalist and responsive interface. To access ReDoc, visit `http://127.0.0.1:8000/redoc` in your browser. You will see something like this:

![ReDoc]

You can use ReDoc to view the details and examples of your API endpoints. You can also expand and collapse the sections by clicking on the headers.

### Dockerizing the app
---------------- 
Dockerizing is the process of packaging, deploying, and running applications using Docker containers. Docker containers are isolated environments that contain everything your application needs to run, such as code, libraries, dependencies, and configuration. By using Docker, you can ensure that your application runs consistently across different platforms and environments.

In this section, we'll learn how to dockerize a FastAPI application from scratch, based on the official Python image. This is what you would want to do in most cases, for example:

- Using Kubernetes or similar tools.
- When running on a Raspberry Pi.
- Using a cloud service that would run a container image for you, etc.

Here are the steps to dockerize a FastAPI application:

Create a `requirements.txt` file that lists all the Python dependencies for your application. For example, if your application uses `FastAPI` and `Uvicorn`, your `requirements.txt` file would look like this:
```txt
fastapi
uvicorn
```
Next, create a Dockerfile that contains instructions for building a Docker image for your application. A Docker image is a snapshot of your application and its dependencies, which can be run as a Docker container. A basic Dockerfile for a FastAPI application may look something like this:

[Docker file](./Dockerfile#L1-L14)

In this Dockerfile:

- We use a lightweight Python 3.9 image as the base.
- We set the working directory inside the container to /code.
- We copy the requirements.txt file and install the other necessary dependencies inside the conatiner.
- Copy the rest of the app source code, expose the port 8000 that the app listens on & define the command to run the app using Uvicorn.

#### Build
Build using: ``docker build -t fastapi_app .``

This will create a Docker image named fastapi_app from the current directory. You can see the built image by running:
`docker images`

#### Run
Run a Docker container from the image using the following command:
`docker run -p 8000:8000 -d fastapi_app`

This will map the port 8000 of the container to the port 8000 of the host machine, and run the container in the background. You can see the running container by running:

`docker ps`

You can now test your application by visiting `http://localhost:8000` in your browser. You should see the FastAPI application in action.

### Kubernetes: Local Dev with Minikube
---------------- 
Kubernetes is an open-source platform for managing containerized applications across multiple nodes. It offers features such as service discovery, load balancing, scaling, rolling updates, and self-healing. However, setting up a Kubernetes cluster can be complex and resource-intensive, especially for local development and testing purposes.

Minikube is a tool that simplifies the process of running a single-node Kubernetes cluster on your local machine. It uses a virtual machine (VM) to run the Kubernetes components, and allows you to interact with the cluster using the kubectl command-line tool. Minikube is ideal for experimenting with Kubernetes features and deploying applications without the need for a cloud provider.

In this section, we will show you how to set up a local Kubernetes cluster using Minikube and deploy a sample application to it. We will assume that you have already dockerized your FastAPI application as described in the previous section.

#### Minikube Prerequisites

To follow this guide, you will need:

- A computer or server with at least 2 GB of RAM and 20 GB of disk space.
- A hypervisor such as VirtualBox, VMware, Hyper-V, or KVM installed on your machine.
- Docker installed on your machine.
- kubectl installed on your machine.
- Minikube installed on your machine.

#### Starting the cluster

To start the cluster, run the following command:

```
minikube start
```

This will create and start a VM with the Kubernetes components. It may take a few minutes to complete. You can check the status of the cluster by running:

```
minikube status
```

You should see something like this:

```
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```

This means that the cluster is ready to use. You can also access the Kubernetes dashboard by running:

```
minikube dashboard
```

This will open the dashboard in your browser, where you can view and manage your cluster resources.

#### Deploying the application

To deploy your application to the cluster, you need to create a Kubernetes manifest file that defines the desired state of your application. A manifest file is a YAML or JSON file that contains one or more Kubernetes objects, such as Pods, Services, Deployments, etc.

For this example, we will create a manifest file named `app.yaml` that contains two objects: a Deployment and a Service. A Deployment is a resource that manages the creation and update of Pods, which are the basic units of execution in Kubernetes. A Service is a resource that exposes a Pod or a group of Pods to the network.

Here is the content of the `app.yaml` file:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-app
spec:
  selector:
    matchLabels:
      app: fastapi-app
  replicas: 1
  template:
    metadata:
      labels:
        app: fastapi-app
    spec:
      containers:
      - name: fastapi-app
        image: fastapi_app # The name of the Docker image we built in the previous section
        ports:
        - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: fastapi-app
spec:
  selector:
    app: fastapi-app
  type: NodePort # Expose the service on a port of the node
  ports:
  - port: 8000
    targetPort: 8000
    nodePort: 30000 # The port of the node where the service is accessible
```

In this file, we define a Deployment that creates a Pod with one container running the `fastapi_app` image. We also expose the port 8000 of the container to the Pod. Then, we define a Service that selects the Pod with the label `app: fastapi-app` and exposes it on the port 30000 of the node.

To apply the manifest file to the cluster, run the following command:

```
kubectl apply -f app.yaml
```

This will create the Deployment and the Service in the cluster. You can verify that they are created by running:

```
kubectl get deployment fastapi-app
kubectl get service fastapi-app
```

You should see something like this:

```
NAME          READY   UP-TO-DATE   AVAILABLE   AGE
fastapi-app   1/1     1            1           2m
```

```
NAME          TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
fastapi-app   NodePort   10.101.142.12   <none>        8000:30000/TCP   2m
```

This means that the application is deployed and running in the cluster.

#### Accessing the application

To access the application, you need to find the IP address of the node where the Service is exposed. You can do that by running:

```
minikube ip
```

You should see something like this:

```
192.168.99.100
```

This is the IP address of the node. To access the application, you can use this IP address and the node port (30000) in your browser. For example:

```
http://192.168.99.100:30000
```

You should see the FastAPI application in action.

#### Stopping and deleting the cluster

To stop the cluster, run the following command:

```
minikube stop
```

This will stop the VM and the Kubernetes components. To delete the cluster, run the following command:

```
minikube delete
```

This will delete the VM and all the cluster resources.


### Challenges & Closing
---------------- 
Working on this project was a great learning experience for me. I faced some challenges along the way, such as:

- Setting up the Kubernetes cluster using Minikube and deploying the FastAPI application to it. I had to learn how to use kubectl, create manifest files, and troubleshoot some errors.
- Dockerizing the FastAPI application and building a Docker image from the Dockerfile. I had to learn how to write a Dockerfile, use Docker commands, and push the image to a registry.
- Writing a good README file that explains the project, its features, and how to use it. I had to learn how to use Markdown, structure the content, and add screenshots and GIFs.
- Despite these challenges, I was able to overcome them and complete the project successfully. I learned a lot of new skills and technologies that will help me in my future projects. I also enjoyed working on this project and I hope you find it useful and interesting.

If you have any feedback, questions, or suggestions, please feel free to contact me or open an issue on GitHub. I would love to hear from you and improve this project. Thank you for reading and happy coding! 😊

