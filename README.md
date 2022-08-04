# Demo CI/CD deployment to k8s using Github Actions #

Demo includes fully automated deployment to development and production environments. Pipelines run unit test execution, code analysis, building and pushing of docker image, running image security scanning and executing deployment of imdb-ratings application to k8s cluster.

### Gigthub Actions prerequisite configuration:

Setup [Gigthub Actions Secrets](https://github.com/Azure/actions-workflow-samples/blob/master/assets/create-secrets-for-GitHub-workflows.md) with following content:
- API_KEY - [IMDB-API](https://imdb-api.com) key
- KUBECONFIG_SA_KEY - Dedicated service account deployment k8s kubeconfig file
- DOCKERHUB_USERNAME - DockerHub login username
- DOCKERHUB_TOKEN - DockerHub login token


### Helm and CI/CD

All helm configuration lives in a deploy directory at the root of project by default. We use helm unpackaged chart per service concept. So servce has own chart what lives in deploy/helm/charts folder. 
Chart contains only templates and default values. For environment configuration we use deploy/helm/environments folder what have environment specific values file what overrides default values from chart per specific environment.

All other CI/CD deployment configuration lives in .github/workflows folder per specific environment.

Charts:

-  `imdb-ratings` - contains k8s deployments (with volume mounts, secrets, init
containers), Services, Secrets, Service accounts, Role Bindings for imdb-ratings k8s application deployment


Github Actions Workflows:

- `imdb-ratings-dev` - triggers on push/merge to main branch. Deploys to development namespace in k8s cluster

- `imdb-ratings-prod` - triggers on release creation event. Deploys to production namespace in k8s cluster
