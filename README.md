# simple-flask-request
simple test hit to other app service


```bash
# deploy to kube
kubectl apply -f deployment.yaml
kubectl expose deployment simple-flask-test --type NodePort

# test hit
curl http://ip_host:nodeport/test-hit
```
