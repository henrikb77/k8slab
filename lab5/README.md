# Steg 1
```
brew install helm
brew install fluxcd/tap/flux
```

```

flux bootstrap github   --owner=$GITHUB_USER   --repository=gitops   --branch=main   --path=./clusters/my-cluster --personal
flux create secret git auth -u $GITHUB_USER -p $GITHUB_TOKEN --url=https://github.com/henrikb77/k8slab
```