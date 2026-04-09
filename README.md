# gamer-rater-api

## Testing

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
