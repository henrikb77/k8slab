# Steg 0

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

## Steg 1

### Deploy metrics-server
```
kubectl apply -f metrics-server.yaml
kubectl wait pods -n kube-system -l k8s-app=metrics-server --for condition=Ready
```

### Deploy test-app
```
docker build -t lab:4 .
kind load docker-image lab:4
kubectl apply -f resources.yaml
```

# Steg 2

| Terminal 1 | Terminal 2 | Terminal 3 |
|------------|------------|------------|
| `watch kubectl top po`| `watch kubectl get po`| `while true; do curl localhost:30000/fib?nterms=20; done`|

# Finally:
```
kubectl delete -f resources.yaml
```