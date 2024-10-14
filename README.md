# HEIF to JPEG Converter

This is a web-based application built using Flask that allows users to upload HEIF/HEIC images and convert them to JPEG format. If you try to test this application on a windows machine then you will fail as pyheif library is only supported in Linux and Mac Os only. To over come this challenge we use Dockerized image.

1. **Clone the repository.**
2. **Update the code as per the feature.**
3. **Once you push your changes and it gets merged to main branch the automated github action scripts are triggered.**
4. **All the code gets built and tested in github and a new dockerized application image is created and tagged.**
5. **After the tagging is complete it gets pushed to dockerhub with the latest tag and also tag details are updated in the deployment.yaml file which is later on used for automated deployment in argocd using k8s.**
6. **Once all this process is complete automated builds are triggered and deployment is completed.** 

## Running the Application

### Prerequisites

- Python 3.10
- Github
- Docker
- Kubernetes
- ArgoCD

### Steps to Run manually:

1. **Clone the repository**
2. **docker build -t heif-converter.**
3. **docker run -p 5000:5000 -v ${PWD}\uploads:/app/uploads -v ${PWD}\converted:/app/converted heif-converter**


docker run -p 5000:5000 -v ${PWD}\uploads:/app/uploads -v ${PWD}\converted:/app/converted saumil156/image-converter:1.0
docker build -t saumil156/image-converter:1.1 .
docker push saumil156/image-converter:1.1


Git bash
docker run -p 5000:5000 -v "$(pwd)/uploads:/app/uploads" -v "$(pwd)/converted:/app/converted" heif_to_jpeg


Running Argo cd:

1. kubectl create namespace argocd
2. kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
3. kubectl port-forward svc/argocd-server -n argocd 8080:443
