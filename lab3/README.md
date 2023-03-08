
# Steg 1
```
docker build -t lab:3 .
kind load docker-image lab:3
kubectl apply -f resources.yaml
```

```
kubectl get po
curl localhost:30000
```

# Steg 2

| Terminal 1 | Terminal 2 | Terminal 3 |
|------------|------------|------------|
| `while true; do curl  -m 2 localhost:30000; sleep 1; done` | `watch kubectl get po` | `curl localhost:30000/crash`|


# Steg 3

| Terminal 1 | Terminal 2 | Terminal 3 |
|------------|------------|------------|
| `while true; do curl  -m 2 localhost:30000; sleep 1; done`| `watch kubectl get po`| `curl localhost:30000/hang` |

# Finally:
```
kubectl delete deploy lab-deployment
```