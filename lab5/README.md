# Steg 0
```
brew install helm
brew install fluxcd/tap/flux
```

# Steg 1

| Terminal 1 | Terminal 2 | Terminal 3 |
|------------|------------|------------|
| `watch kubectl get po -n foo`| `kubectl create ns foo`||
||`flux bootstrap github   --owner=$GITHUB_USER   --repository=gitops   --branch=main   --path=./clusters/my-cluster --personal`||
||`flux create secret git auth -u $GITHUB_USER -p $GITHUB_TOKEN --url=https://github.com/henrikb77/k8slab`||
||`kubectl apply -f sourcerepo.yaml`||
|||`while true; do curl localhost:30000/;sleep 1; done`|

# Steg 2
Byt imageVersion i gitops - gör en release!

