# House Price Prediction Endpoint

[![Endpoint](https://github.com/anirbanpranto/house-price-endpoint/actions/workflows/python-app.yml/badge.svg)](https://github.com/anirbanpranto/house-price-endpoint/actions/workflows/python-app.yml)
[![Docker Image CI](https://github.com/anirbanpranto/house-price-endpoint/actions/workflows/docker-image.yml/badge.svg)](https://github.com/anirbanpranto/house-price-endpoint/actions/workflows/docker-image.yml)

## How to run

### Build the docker image

```bash
export DOCKER_BUILDKIT=1
docker build --tag house_price_endpoint:latest  -f Dockerfile .
```

### Run the docker image

You can either run it in detached mode,

```bash
docker run -d -p 8000:80 house_price_endpoint:latest
```

or without detached mode,

```
docker run -p 8000:80 house_price_endpoint:latest
```

The app should be running at `http://localhost:8000/`

## Endpoints

The app contains a single endpoint,

```bash
/predict
```

### Make a request to the endpoint

```bash
curl -X POST http://localhost:8000/predict \
-H 'Content-Type: application/json' \
-d '{
    "features":
        {
            "avg_area_income":79545.45857431678,
            "avg_area_house_age":5.682861321615587,
            "avg_area_number_of_rooms":7.009188142792237,
            "avg_area_number_of_bedrooms":4.09,
            "area_population":23086.800502686456,
            "address":"208 Michael Ferry Apt. 674 Laurabury, NE 37010-5101"
        },
        "provider": "payment-api"
    }'
```

The output should be similar to,

```bash
{
  "features": {
    "avg_area_income": 79545.45857431678,
    "avg_area_house_age": 5.682861321615587,
    "avg_area_number_of_rooms": 7.009188142792237,
    "avg_area_number_of_bedrooms": 4.09,
    "area_population": 23086.800502686456,
    "address": "208 Michael Ferry Apt. 674 Laurabury, NE 37010-5101"
  },
  "provider": "payment-api",
  "output": 1244892.8
}
```

## Testing

If you wish to run tests -

```bash
pip install -r requirements.txt
pytest
```

## Performance

The endpoint can serve on average 85 requests/second. If the number of concurrent users are more than 90, the response time deteroriates, as shown by the locust test below.

![Locust](https://github.com/anirbanpranto/house-price-endpoint/blob/master/total_requests_per_second_1694273708.png)
