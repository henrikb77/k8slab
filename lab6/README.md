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

## Deploy

### metrics-server
```
kubectl apply -f metrics-server.yaml
```

### test-app
```
docker build -t lab:6 .
kind load docker-image lab:6
```

# Stress

```
 while true; do curl localhost:30000/fib?nterms=20; done
 ```

# Monitor
```
while true; do kubectl top po; sleep 1; done
```