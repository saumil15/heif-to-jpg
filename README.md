# HEIF to JPEG Converter

This is a web-based application built using Flask that allows users to upload HEIF/HEIC images and convert them to JPEG format.

## Running the Application

### Prerequisites

- Docker
- Python 3.10

### Steps to Run:

1. **Clone the repository**
2. **docker build -t heif-converter.**
3. **docker run -p 5000:5000 -v ${PWD}\uploads:/app/uploads -v ${PWD}\converted:/app/converted heif-converter**

This project will only run on linux or mac as pyheif module doesn't work on windows. if you wish to run on windows use docker image

docker run -p 5000:5000 -v ${PWD}\uploads:/app/uploads -v ${PWD}\converted:/app/converted saumil156/image-converter:1.0

docker build -t saumil156/image-converter:1.1 .
docker push saumil156/image-converter:1.1


git bash
docker run -p 5000:5000 -v "$(pwd)/uploads:/app/uploads" -v "$(pwd)/converted:/app/converted" heif_to_jpeg


Running Argo cd:

1. kubectl create namespace argocd
2. kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
3. kubectl port-forward svc/argocd-server -n argocd 8080:443


Creating new image after changes

You need to create a new tag and push the image into docker hub repo 
then use the new tag for your next sync