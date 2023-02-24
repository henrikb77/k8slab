
# Steg 1
```
docker build -t lab:2 .
kind load docker-image lab:2
kubectl apply -f resources.yaml
```

```
kubectl get po
curl localhost:30000
```

# Steg 2

## Terminal 1
```
while true; do curl localhost:30000; sleep 1; done
```

## Terminal 2
```
docker build -t lab:2.1 -f Dockerfile21 .
kind load docker-image lab:2.1
kubectl apply -f resources21.yaml
```
