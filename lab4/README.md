# Steg 1

## Hämta metrics-server

```
curl -L -o metrics-server.yaml https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/high-availability-1.21+.yaml
```

## Lägg till argument till deployment
.spec.template.spec.containers[].args

```
- --kubelet-insecure-tls
```

## Ta bort anti-affinity för att kunna testa på lokalt kind-kluster
Ta bort .spec.template.spec.affinity.

## Steg 2

### Deploya metrics-server
```
kubectl apply -f metrics-server.yaml
```

### Deploya test-app
```
kubectl delete deploy lab-deployment
docker build -t lab:4 .
kind load docker-image lab:4
kubectl apply -f resources.yaml
```

# Terminal 1
```
while true; do kubectl top po; sleep 1; done
```

# Terminal 2
```
kubectl get po --watch
```

# Terminal 3

```
 while true; do curl localhost:30000/fib?nterms=20; done
 ```

