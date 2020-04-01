# demo web app #
My friend Austin has a lot of great ideas that could make him a billionaire. Unfortunately, he's usually a few decades late. This is a web app which includes CRUD operations for keeping a list of "$B Ideas" with front end in [React](reactjs.org), backend API built with Python [Flask](https://www.fullstackpython.com/flask.html) and [MongoDB](www.mongodb.com). This is an exercise for me to learn some new technologies and show the value of deploying them on Kubernetes.

## Prerequisites ##
* MongoDB instance configured ([MongoDB Atlas](mongodb.com/cloud/atlas) is an easy way to get started!) with connection string
* docker and docker-compose installed (for dev envirnment)
* Kubernetes cluster configured with a `web-app` namespace
* Tool for sending HTTP requests (i.e. [Postman](https://www.getpostman.com/) or [Curl](https://curl.haxx.se/))
 
## Setup a development instance ##
**Clone git repo**
```bash
$ git clone https://github.com/dja3/web-app.git
```

**Create MongoDB Database and collection**
You need to have a database named `idea` and a collecion named `oneBIdeas` configured in your MongoDB instance. Will hopefully get this initialization added to the application later.

**Add Mongo connection string**
Add your own MongoDB connection string to a file named `connection` under `for_devs/dev_mongo_config/` directory. File should look something like this:
```bash
mongodb+srv://<username>:<password>@cluster0.gcp.mongodb.net/test?retryWrites=true&w=majority
```

**Deploy with  Docker-Compose**
To start the API server and the UI containers locally, from the root of the repo run:
```bash
$ docker-compose up
Starting webapp_api_1
Starting webapp_ui_1
Attaching to webapp_api_1, webapp_ui_1
api_1  |  * Serving Flask app "app.web" (lazy loading)
api_1  |  * Environment: production
api_1  |    WARNING: This is a development server. Do not use it in a production deployment.
api_1  |    Use a production WSGI server instead.
api_1  |  * Debug mode: off
api_1  |  * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
ui_1   | 
ui_1   | > web-app@0.1.0 start /web-app
ui_1   | > react-scripts start
ui_1   | 
ui_1   | ℹ ｢wds｣: Project is running at http://172.18.0.3/
ui_1   | ℹ ｢wds｣: webpack output is served from 
ui_1   | ℹ ｢wds｣: Content not from webpack is ser ved from /web-app/public
ui_1   | ℹ ｢wds｣: 404s will fallback to /
ui_1   | Starting the development server...
ui_1   | 
ui_1   | Compiled with warnings.
ui_1   | 
ui_1   | ./src/App.js
ui_1   |   Line 5:7:  'API_BASE_URL' is assigned a value but never used       no-unused-vars
ui_1   |   Line 6:7:  'API_BASE_URL_PORT' is assigned a value but never used  no-unused-vars
ui_1   | 
ui_1   | Search for the keywords to learn more about each warning.
ui_1   | To ignore, add // eslint-disable-next-line to the line before.
ui_1   | 
```
P
The backend API is available on `http://localhost:80` and the UI is available on `http://localhost:3000`.

**Deploy on Kubernetes**
In the root of the repository are two `yaml` configs, `web_app_api.yaml` and `web_app_ui.yaml`. 

`web_app_api.yaml` 

This creates the following three Kubernetes objects for the backend API: [Service](https://kubernetes.io/docs/concepts/services-networking/service/), [Secret](https://kubernetes.io/docs/concepts/configuration/secret/) and [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

*Service* - The backend API service is a `ClusterIP` ServiceType so it the service is only reachable from with the Kubernetes cluster to be accessed by the UI. It is connected to the backend API deployment through the `tier: web-app-api` Selector.

*Secret* - The secret is used to pass your MongoDB connection string (containing credentials) into the pod rather than hard-coding a connection.

*Deployment* - The deployment for the backend API defines the number of replicas as well as the pod configuration.

`web_app_ui.yaml`

This creates the following two Kubernetes objects for the frontend UI: [Service](https://kubernetes.io/docs/concepts/services-networking/service/) and [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

*Service* - The backend API service is a `LoadBalancer` ServiceType to expose it outside the Kubernetes cluster. It is connected to the frontent UI deployment through the `tier: web-app-ui` Selector. You can also use `NodePort` ServiceType to expose outside if a `LoadBalancer` isn't configured. All public cloud provider's Kuberenetes services have `LoadBalancer` configured and it's an easy way to get a stable Public IP address assigned.

*Deployment* - The deployment for the frontend defines the number of replicas as well as the pod configuration. The frontend UI makes calls to the backend API via the backend service.
