# Redis Distributed Cache with Consistent Hashing

A Flask application demonstrating distributed Redis caching using consistent hashing.

## Features

- Redis caching
- Multiple Redis nodes
- Consistent hash routing
- Cache expiration
- Docker Compose setup

## Technologies Used

- Python
- Flask
- Redis
- Docker

## Installation

```bash
docker compose up --build
```

## Endpoint

GET /cache/<key>

GET /health

## Purpose

Day 295 demonstrates distributed caching and consistent hashing.
