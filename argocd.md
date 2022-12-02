где храниться стейт релизов


# Requiremetns


## Minikube

## Helmfile

https://github.com/helmfile/helmfile
https://github.com/helmfile/helmfile/releases/download/v0.148.1/helmfile_0.148.1_linux_amd64.tar.gz
helm plugin install https://github.com/databus23/helm-diff

#https://github.com/lucj/argocd-helmfile-plugin

## argocd cli
VERSION=v2.5.3
curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/download/v2.5.3/argocd-linux-amd64
sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd
rm argocd-linux-amd64


## Flask
export ARGO_ENV='123'
echo $ARGO_ENV
podman build -t docker.io/flomko/flask-test:0.0.1 .

# Set up
```
minikube start
minikube addons enable ingress
helmfile apply
kubectl port-forward -n argocd svc/argocd-server 8080:80
```

### Tear up
kubectl delete crd applications.argoproj.io applicationsets.argoproj.io appprojects.argoproj.io datadogagents.datadoghq.com
kubectl delete crd applications.argoproj.io applicationsets.argoproj.io appprojects.argoproj.io datadogagents.datadoghq.com
kubectl delete ClusterRoleBinding argocd-server argocd-application-controller


Git Ops continious delivery tool
- argo workflow
- argo CI
- argo events
- argo cd

https://github.com/argoproj/argocd-example-apps



kubectl - who deploy what, what is it, when etc

argocd --server 127.0.0.1:8080 --insecure version

kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

argocd login 127.0.0.1:8080 --username admin --password saBhvGSXFCylTfvU --insecure


argocd app create trivy-operator --repo https://github.com/aquasecurity/trivy-operator.git --path deploy/helm --revision HEAD --dest-server https://kubernetes.default.svc --dest-namespace trivy-operator --server 127.0.0.1:8080 --insecure 

https://github.com/aquasecurity/trivy-operator.git