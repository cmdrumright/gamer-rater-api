# gamer-rater-api

## Testing Auth

### Register

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
    "username": "cory@drumright.com",
    "password": "drumright",
    "first_name": "Cory",
    "last_name": "Drumright"
}' \
  'http://localhost:8000/register' | jq
```

### Login

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
    "username": "cory@drumright.com",
    "password": "drumright"
}' \
  'http://localhost:8000/login' | jq
```

## Testing Games

### Get All

```bash
curl --header "Authorization: Token aec5bb2d4dfef8d67879dfd1c608d2096e3736ba" \
'http://localhost:8000/games' | jq
```

### Get One

```bash
curl --header "Authorization: Token aec5bb2d4dfef8d67879dfd1c608d2096e3736ba" \
'http://localhost:8000/games/1' | jq
```

### Create

```bash
curl --header "Content-Type: application/json" \
  --header "Authorization: Token aec5bb2d4dfef8d67879dfd1c608d2096e3736ba" \
  --request POST \
  --data '{
    "title": "Monopoly",
    "description": "A board game teaching the pitfalls of capitalism",
    "release_year": 1970,
    "player_count": 8,
    "completion_hours": 10,
    "recommended_age": 13,
    "categories": [1, 2]
}' \
  'http://localhost:8000/games' | jq
```

### Update

```bash
curl --header "Content-Type: application/json" \
  --header "Authorization: Token aec5bb2d4dfef8d67879dfd1c608d2096e3736ba" \
  --request PUT \
  --data '{
    "title": "Monopoly",
    "description": "A board game teaching the pitfalls of capitalism",
    "release_year": 1970,
    "player_count": 8,
    "completion_hours": 10,
    "recommended_age": 13,
    "categories": [1, 3]
}' \
  'http://localhost:8000/games/7' | jq
```

### Delete

```bash
curl --header "Authorization: Token aec5bb2d4dfef8d67879dfd1c608d2096e3736ba" \
--request "DELETE" \
'http://localhost:8000/games/8' | jq

```
