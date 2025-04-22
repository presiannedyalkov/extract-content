# Readability Microservice

A microservice built with Flask to extract the main content from web pages using the `readability-lxml` library.

## Overview

This microservice provides a simple REST API to extract readable content from URLs. It is designed to be lightweight and easy to deploy in containerized environments.

## Features

- **Content Extraction**: Uses `readability-lxml` to extract the main content from web pages.
- **Multi-Architecture Support**: Built with Docker to support both `amd64` and `arm64` architectures.
- **REST API**: Exposes a single endpoint (`/extract`) to receive URLs and return extracted content.

## Getting Started

### Prerequisites

- Docker installed on your system.
- A Docker Hub account (optional).

### Building and Running

1. **Clone the Repository**:
```git clone https://github.com/YOUR_USERNAME/readability-microservice.git```

2. **Build the Docker Image**:
```docker buildx build --platform linux/amd64,linux/arm64 --push -t YOUR_DOCKER_USERNAME/readability-microservice:latest .```

3. **Run the Container**:
```docker run -p 8080:5000 YOUR_DOCKER_USERNAME/readability-microservice:latest```

### Using the API

1. **Send a POST Request** to `http://localhost:8080/extract` with a JSON payload containing the URL:
```curl -X POST -H "Content-Type: application/json" -d '{"url": "https://example.com"}' http://localhost:8080/extract```

## Deployment

This microservice can be deployed in any environment that supports Docker containers.

## License
MIT License