# prometheus-custom-instrumentation
sample application for scraping custom metrics from sample app

## Usage

1. build docker
`docker build -t prometheus-sample-app`

2. push to docker or private repo

3. deploy to k8s
`kubectl apply -f app.yml`

4. validate the app by using busybox

5. edit prometheus server configmap, add the static_config to the scrape_configs
`k edit cm -n prometheus prometheus-for-amp-server`

```
    scrape_configs:
    - job_name: 'myapp'
      static_configs:
      - targets: ['myapp.default:80']      
```     
