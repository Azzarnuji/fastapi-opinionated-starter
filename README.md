# FastAPI Opinionated Starter

A structured and opinionated FastAPI framework that provides automatic controller discovery and decorator-based routing for building well-organized web applications.

## Features

- **Decorator-based Routing**: Use `@Controller`, `@Get`, `@Post` decorators to define routes
- **Automatic Controller Discovery**: Controllers in `app/domains` are automatically loaded
- **Clean Architecture**: Domain-based separation of concerns
- **Custom Logging**: Colored logging with timing information
- **FastAPI Integration**: Full compatibility with FastAPI features

## Project Structure

```
fastapi-opinionated-starter/
├── app/
│   ├── core/           # Core application components
│   ├── domains/        # Domain-specific controllers
│   │   ├── user/       # User domain
│   │   │   └── controller.py
│   │   └── auth/       # Authentication domain
│   └── shared/         # Shared utilities
├── main.py            # Application entry point
└── pyproject.toml     # Project dependencies
```

## Getting Started

### Prerequisites

- Python 3.12+
- Poetry (recommended for dependency management)

### Installation

1. Clone the repository
2. Install dependencies using Poetry:

```bash
poetry install
```

3. Run the application:

```bash
fastapi dev main.py --host 0.0.0.0 --port 8003
```

## Usage

### Creating Controllers

Create controllers in the `app/domains` directory using the provided decorators:

```python
from fastapi_opinionated.decorators.routing import Controller, Get, Post

@Controller("/users")
class UserController:

    @Get("/")
    async def list(self):
        return ["john", "budi"]

    @Post("/create")
    async def create(self):
        return {"ok": True}
```

### Available Decorators

- `@Controller(base_path)`: Defines a controller with a base path
- `@Get(path)`: Defines a GET route
- `@Post(path)`: Defines a POST route
- `@Http(method, path)`: Generic HTTP method decorator

### Lifespan Management

The application supports standard FastAPI lifespan management for startup and shutdown events:

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Startup code here
        yield
        # Shutdown code here
    except Exception as e:
        print(f"Lifespan error: {e}")
```

## Configuration

The project uses the fastapi-opinionated-core library which provides:
- Automatic route registration
- Custom logging system
- Convention-based controller loading

## Development

### Adding New Domains

Create new directories in `app/domains` and add controller files. They will be automatically discovered and registered.


## License

This project is licensed under the MIT License - see the LICENSE file for details.