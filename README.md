# microservice-in-python
https://www.youtube.com/watch?v=SdTzwYmsgoU
https://github.com/kunchalavikram1427/microservices-in-python

Creating Python Virtual Environments
    python3 -m venv tutorial-env
    source tutorial-env/bin/activate
Installing Python VS Code Extension
Sample Flask Application
    pip install Flask
    https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application
Jinja templating for Dynamic Web Pages
Using Pip to Freeze Python Dependencies
Building the docker image using Dockerfile
Writing Docker Compose file
    minikube ip  -> 192.168.49.2 on port ??
    curl -f http://192.168.49.2:81/details
Writing Kubernetes Manifest files for the application
Creating Helm Chart
    helm template webapp
    helm install web webapp
    helm uninstall web
