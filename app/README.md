First commit into the main because it is more simple and there is nothing in the app so far.
I know it might be forbided in a real environment, but I do it like this this time.

Later I will use branches and PR-s.

The app uses port 8000


# #################################################################
# Application Requirements

Create a small service in **Go** or **Python** with the following endpoints.

## Required Endpoints

### `GET /health`

**Response:**

```json
{
    "status": "ok"
}
```

### `GET /version`

**Response:**

```json
{
    "version": "1.0.0"
}
```

### `GET /env`

**Response:**

```json
{
    "environment": "<value from ENVIRONMENT variable>"
}
```

### `POST /config`

**Request:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

**Response:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

### `GET /config/{name}`

**Example:**

```bash
GET /config/database_url
```

**Response:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

### `DELETE /config/{name}`

**Response:**

```json
{
    "deleted": true
}
```

## Implementation Notes

Use any framework you prefer.
