# FastAPI Opinionated Starter

A structured and opinionated FastAPI framework that provides automatic controller discovery and decorator-based routing for building well-organized web applications.

## Features

- **Decorator-based Routing**: Use `@Controller`, `@Get`, `@Post`, `@Put`, `@Patch`, `@Delete` decorators to define routes
- **Automatic Controller Discovery**: Controllers in `app/domains` are automatically loaded
- **Clean Architecture**: Domain-based separation of concerns with support for class-based and functional-based approaches
- **Custom Logging**: Colored logging with timing information
- **FastAPI Integration**: Full compatibility with FastAPI features
- **Flexible Controller Patterns**: Supports both class-based and functional-based controller definitions

## Project Structure

```
fastapi-opinionated-starter/
├── app/
│   ├── core/                    # Core application components
│   ├── domains/                 # Domain-specific modules
│   │   ├── class-based/         # Class-based approach
│   │   │   ├── controllers/     # Controller classes with decorator-based routing
│   │   │   ├── services/        # Business logic services
│   │   │   └── queues/          # Background job queues
│   │   └── functional-based/    # Functional-based approach
│   │       ├── controllers/     # Functional controller endpoints
│   │       ├── services/        # Business logic services
│   │       └── queues/          # Background job queues
│   └── shared/                  # Shared utilities
├── main.py                     # Application entry point
└── pyproject.toml              # Project dependencies
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
poetry run fastapi dev main.py --host 0.0.0.0 --port 8003
```

Or if you have FastAPI installed globally:

```bash
fastapi dev main.py --host 0.0.0.0 --port 8003
```

## Usage

### Creating Class-Based Controllers

Create class-based controllers in the `app/domains` directory using the provided decorators:

```python
from fastapi_opinionated.decorators.routing import Controller, Get, Post, Put, Patch, Delete


@Controller("/users", group="USERS")
class UsersController:

    @Get("/")
    async def list(self):
        return {"message": "List class-based"}

    @Post("/create")
    async def create(self):
        return {"message": "UsersController created successfully"}

    @Put("/update")
    async def update(self):
        return {"message": "UsersController updated successfully"}

    @Patch("/partial_update")
    async def partial_update(self):
        return {"message": "UsersController updated successfully"}

    @Delete("/delete")
    async def delete(self):
        return {"message": "UsersController deleted successfully"}
```

### Creating Functional-Based Controllers

Or create functional controllers in the `app/domains` directory:

```python
from fastapi_opinionated.decorators.routing import Get, Post


@Get("/users", group="USERS")
async def list_users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

@Post("/users", group="USERS")
async def create_user(user: dict):
    return {"id": 3, **user}
```

### Available Decorators

#### Class-Based Controller Decorators:
- `@Controller(base_path, group=None)`: Defines a controller with a base path
- `@Get(path, group=None)`: Defines a GET route
- `@Post(path, group=None)`: Defines a POST route
- `@Put(path, group=None)`: Defines a PUT route
- `@Patch(path, group=None)`: Defines a PATCH route
- `@Delete(path, group=None)`: Defines a DELETE route

#### Functional-Based Decorators:
- `@Get(path, group=None)`: Defines a GET route
- `@Post(path, group=None)`: Defines a POST route
- `@Put(path, group=None)`: Defines a PUT route
- `@Patch(path, group=None)`: Defines a PATCH route
- `@Delete(path, group=None)`: Defines a DELETE route

The `group` parameter is optional and allows you to categorize your routes in the OpenAPI documentation.

### Lifespan Management

The application supports standard FastAPI lifespan management for startup and shutdown events:

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Startup code here
        print("Starting up the application...")
        yield
        # Shutdown code here
        print("Shutting down the application...")
    except Exception as e:
        print(f"Lifespan error: {e}")
```

## Configuration

The project uses the fastapi-opinionated-core library which provides:
- Automatic route registration
- Custom logging system
- Convention-based controller loading
- Support for both class-based and functional-based controllers

## Architecture

This project follows a domain-driven design with clear separation of concerns:

- **Controllers**: Handle HTTP requests and responses
- **Services**: Contain business logic
- **Queues**: Handle background jobs and tasks
- **Domains**: Group related functionality by business domain

### Creating New Domains

Create new domains by adding directories in `app/domains`:

```
app/domains/
├── user/
│   ├── controllers/
│   │   ├── users.py
│   │   └── profiles.py
│   ├── services/
│   │   ├── user_service.py
│   │   └── profile_service.py
│   └── queues/
│       └── user_tasks.py
└── auth/
    ├── controllers/
    │   └── auth.py
    ├── services/
    │   └── auth_service.py
    └── queues/
        └── auth_tasks.py
```

Controllers, services, and queues in these domains will be automatically discovered and registered.

### Services

Business logic should be placed in service classes within the `services` directory:

```python
# app/domains/user/services/user_service.py
class UserService:
    @staticmethod
    async def get_all_users():
        # Business logic here
        return [{"id": 1, "name": "John"}, {"id": 2, "name": "Bob"}]

    @staticmethod
    async def create_user(data: dict):
        # Business logic here
        return {"id": 3, **data}
```

Then use the service in your controller:

```python
# app/domains/user/controllers/users.py
from fastapi_opinionated.decorators.routing import Controller, Get
from app.domains.user.services.user_service import UserService


@Controller("/users", group="USERS")
class UsersController:

    @Get("/")
    async def list(self):
        users = await UserService.get_all_users()
        return {"users": users}
```

### Queues [HOLD]

Background tasks can be defined in the `queues` directory:

```python
# app/domains/user/queues/user_tasks.py
import asyncio

async def send_welcome_email(user_id: int):
    # Background task logic here
    await asyncio.sleep(1)  # Simulate async work
    print(f"Welcome email sent to user {user_id}")
```

## Development

### Best Practices

1. **Domain Separation**: Group related functionality by domain (e.g., user, auth, product)
2. **Controller Responsibilities**: Controllers should handle HTTP concerns only, delegate business logic to services
3. **Service Layer**: Business logic should reside in service classes
4. **Consistent Naming**: Follow consistent naming conventions for routes and controller methods
5. **Error Handling**: Implement proper error handling in your services and controllers

### API Documentation

The application automatically generates OpenAPI documentation with Swagger UI and ReDoc. 
After starting the application, visit:
- Swagger UI: `http://localhost:8003/docs`
- ReDoc: `http://localhost:8003/redoc`

## Testing

To run tests:

```bash
# Install test dependencies
poetry install --with test

# Run tests
poetry run pytest
```

## CLI

The FastAPI Opinionated framework includes a command-line interface (CLI) tool for generating new components quickly and consistently.

### Installation

The CLI is automatically installed when you install the `fastapi-opinionated-core` package. It's available as a command-line tool:

```bash
fastapi-opinionated [OPTIONS] COMMAND [ARGS]...
```

### Available Commands

#### `new domain` - Create a new domain folder structure

```bash
fastapi-opinionated new domain NAME [OPTIONS]
```

**Options:**
- `--bootstrap` - Generate bootstrapped folders: controllers, services, queues

**Examples:**
```bash
# Create a basic domain
fastapi-opinionated new domain user

# Create a domain with all subfolders
fastapi-opinionated new domain user --bootstrap
```

**Generated Structure (with bootstrap):**
```
app/domains/{name}/
├── __init__.py
├── controllers/
│   └── __init__.py
├── services/
│   └── __init__.py
└── queues/
    └── __init__.py
```

#### `new controller` - Create a controller inside a domain

```bash
fastapi-opinionated new controller DOMAIN_NAME [OPTIONS]
```

**Options:**
- `--controller-name TEXT` - Specify controller filename (default: "controller")
- `--crud` - Generate CRUD endpoints (list, create, update, delete)

**Examples:**
```bash
# Create a basic controller for the user domain
fastapi-opinionated new controller user

# Create a named controller
fastapi-opinionated new controller user get_user

# Create a controller with CRUD endpoints
fastapi-opinionated new controller user --crud
```

**Generated Controller (with CRUD):**
```python
from fastapi_opinionated.decorators.routing import Controller, Get, Post, Put, Patch, Delete


@Controller("/{domain_name}", group="{DOMAIN_NAME}")
class {DomainName}Controller:

    @Get("/")
    async def list(self):
        return {"message": "List {domain_name}"}

    @Post("/create")
    async def create(self):
        return {"message": "{DomainName}Controller created successfully"}

    @Put("/update")
    async def update(self):
        return {"message": "{DomainName}Controller updated successfully"}
        
    @Patch("/partial_update")
    async def partial_update(self):
        return {"message": "{DomainName}Controller updated successfully"}

    @Delete("/delete")
    async def delete(self):
        return {"message": "{DomainName}Controller deleted successfully"}
```

### CLI Integration

The CLI-generated components integrate seamlessly with the FastAPI Opinionated Starter:

1. **Automatic Discovery**: Components created with the CLI are automatically discovered and registered
2. **Consistent Architecture**: Generated code follows the same architectural patterns as the rest of the project
3. **No Manual Configuration**: New domains and controllers are instantly available in your application without additional setup

**Example Integration Test:**
```bash
# Create a new domain with bootstrapped folders
fastapi-opinionated new domain product --bootstrap

# Create a controller with CRUD operations
fastapi-opinionated new controller product --crud

# Run the application - new routes will be automatically available
poetry run fastapi dev main.py --host 0.0.0.0 --port 8003
```

When you run the application, you'll see log messages confirming that the new controller was discovered and its routes registered automatically.

### CLI Benefits

- **Speed**: Quickly scaffold new domains and controllers with proper structure
- **Consistency**: Ensures all components follow the same architectural patterns
- **Conventions**: Automatically applies proper naming and decorator conventions  
- **Zero Configuration**: New components are automatically discovered and registered without manual configuration

## Deployment

For production deployment, use Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8003
```

## Architecture Flow Diagram

Here's an end-to-end flow diagram showing how the FastAPI Opinionated framework works:

```mermaid
graph TB
    subgraph "Development Phase"
        Dev[Developer]
        CLI[fastapi-opinionated CLI]
        GenDomain[Generate Domain Structure<br/>--bootstrap]
        GenController[Generate Controller<br/>--crud]
        AddCode[Add custom business logic]
        
        Dev --> CLI
        CLI --> GenDomain
        CLI --> GenController
        GenDomain --> AddCode
        GenController --> AddCode
    end
    
    subgraph "Project Structure"
        AppDir[app/]
        DomainsDir[domains/]
        ClassBased[class-based/]
        FuncBased[functional-based/]
        DomainDir[domain-name/]
        CtrlDir[controllers/]
        ServDir[services/]
        QueueDir[queues/]
        
        AppDir --> DomainsDir
        DomainsDir --> ClassBased
        DomainsDir --> FuncBased
        DomainsDir --> DomainDir
        ClassBased --> CtrlDir
        ClassBased --> ServDir
        ClassBased --> QueueDir
    end
    
    subgraph "Controller Examples"
        ClassCtrl[Class-based Controller<br/>@Controller, @Get, @Post...]
        FuncCtrl[Functional Controller<br/>@Get, @Post decorators]
        
        CtrlDir --> ClassCtrl
        CtrlDir --> FuncCtrl
    end
    
    subgraph "Application Startup"
        Main[main.py App.create()]
        Discovery[Auto-discovery engine]
        ImportMod[Import modules from app/domains/]
        FindDecor[Find decorated functions/classes]
        RegRoutes[Register routes with FastAPI]
        
        Main --> Discovery
        Discovery --> ImportMod
        ImportMod --> FindDecor
        FindDecor --> RegRoutes
    end
    
    subgraph "Runtime Request Flow"
        HTTPReq[HTTP Request]
        FastAPIRouter[FastAPI Router]
        RouteMatch[Match to controller method]
        Execute[Execute method]
        Response[Return Response]
        
        HTTPReq --> FastAPIRouter
        FastAPIRouter --> RouteMatch
        RouteMatch --> Execute
        Execute --> Response
    end
    
    subgraph "Service Integration"
        Service[Service Layer]
        BusinessLogic[Business Logic]
        Service --> BusinessLogic
        Execute --> Service
    end
    
    subgraph "Queue Processing"
        Queue[Queue System]
        BGTask[Background Tasks]
        Queue --> BGTask
    end
    
    Dev -.-> GenDomain
    GenDomain -.-> DomainDir
    GenController -.-> ClassCtrl
    GenController -.-> FuncCtrl
    AddCode -.-> ClassCtrl
    AddCode -.-> FuncCtrl
    DomainDir -.-> CtrlDir
    Main -.-> Discovery
    ImportMod -.-> ClassCtrl
    ImportMod -.-> FuncCtrl
    FindDecor -.-> RegRoutes
    RegRoutes -.-> FastAPIRouter
    RouteMatch -.-> ClassCtrl
    RouteMatch -.-> FuncCtrl
    Execute -.-> Service
    Execute -.-> Queue
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.