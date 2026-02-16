# 1. Consume data from an API using command line tools (curl)

## 1 : Check curl installation

### Command
```bash
curl --version
```

### Output (excerpt)
```text
curl 8.5.0 (x86_64-pc-linux-gnu) libcurl/8.5.0 OpenSSL/3.0.13 ...
Protocols: ... http https ...
Features: ... HTTP2 ... SSL ...
```

### Interpretation
- curl is installed and available on the system.
- HTTP and HTTPS protocols are supported.
- SSL/TLS support is enabled via OpenSSL.
- HTTP/2 support is enabled.

---

## 2 : Fetching data from an API (GET request)

### Command
```bash
curl https://jsonplaceholder.typicode.com/posts
```

### Output (excerpt)
```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\n..."
  },
  ...
]
```

### Interpretation
- The API returns a JSON array of posts.
- Each post contains: `userId`, `id`, `title`, `body`.

---

## 3 : Fetch only response headers

### Command
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

### Output
```text
HTTP/2 200
date: Mon, 16 Feb 2026 12:40:40 GMT
content-type: application/json; charset=utf-8
cache-control: max-age=43200
etag: W/"6b80-Ybsq/K6GwwqrYkAsFxqDXGC7DoM"
server: cloudflare
x-powered-by: Express
...
```

### Interpretation
- Status code `200` confirms the request succeeded.
- `content-type: application/json` confirms the server returns JSON.
- Cache-related headers (`cache-control`, `etag`, `age`) show the response may be cached.
- Server is behind Cloudflare (`server: cloudflare`).

---

## 4 : Send data to the API (POST request)

### Command
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

### Output
```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

### Interpretation
- A new resource is simulated as created by JSONPlaceholder.
- The response includes the submitted fields and a generated `id` (101).
- JSONPlaceholder does not persist data, but simulates the behavior of a real API.