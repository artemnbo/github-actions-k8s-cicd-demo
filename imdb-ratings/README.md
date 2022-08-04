# Simple Python Flask Dockerized Application to get top 10 movies from IMDB using [IMDB-API](https://imdb-api.com) #

Build the image using the following command

```bash
$ docker build -t imdb-ratings:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -e API_KEY=YOUR_IMDB_API_KEY -d -p 5000:5000 imdb-ratings
```

The application will be accessible at [http://127.0.0.1:5000](http://127.0.0.1:5000)
