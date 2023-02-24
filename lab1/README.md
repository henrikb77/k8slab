
```
cd lab1
```

# Steg 1
```
kind create cluster --config cluster.yaml

docker build -t lab:1 .

kind load docker-image lab:1 # ekvivalent till att ladda upp till registry (Harbor, Dockerhub)
                             # detta är en specialare för lokalt kind-kluster
```

# Steg 2
```
kubectl get po
kubectl logs <poddens namn>
```

# Steg 3

Ändra rad 8 i resources.yaml så 1 --> 2:
```
replicas: 2
```

## Terminal 1
```
kubectl get po --watch
```

## Terminal 2
```
kubectl apply -f resources.yaml
```
