## Build
```sh
gcloud builds submit --tag gcr.io/hello-streamlit/hello_streamlit --project=hello-streamlit
```

## Deploy

```sh
gcloud run deploy --image gcr.io/hello-streamlit/hello_streamlit --platform managed --project=hello-streamlit --allow-unauthenticated
```