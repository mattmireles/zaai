# ZAAI: Zerg Autonomous AI Manifest Suite

A comprehensive benchmark system for evaluating AI coding capabilities across diverse software development domains.

## 🚀 Quickstart

### What is ZAAI?
ZAAI is an autonomous AI benchmark suite that tests AI coding capabilities across real-world software development scenarios. Instead of simple coding puzzles, ZAAI presents comprehensive challenges like "build a Flask web app," "integrate with Jira API," or "create a 2D game" - then validates the AI's implementation against realistic requirements.

### What Can It Test?
- **Core Programming**: Hello World, API integrations, game development, file processing
- **Enterprise Integration**: Jira, Confluence, Salesforce, Zendesk, ServiceNow connectors  
- **Cloud Development**: Web applications, cloud deployments, database integration
- **Environment Handling**: Multi-language source files, various file formats

### Quick Demo
```bash
# 1. Clone the repository
git clone <your-repo-url>
cd zaai

# 2. Examine a simple benchmark
cat domains/core/core.yaml | grep -A 20 "name: \"hello\""

# 3. Look at expected implementation patterns
cat domains/core/foobar.py  # Example workspace file

# 4. Check what the AI would need to create
grep -n "from main import" domains/core/core.yaml
```

### How It Works
1. **Manifest Definition**: Each benchmark is defined in YAML with specs, tests, and configs
2. **AI Implementation**: AI creates required files (main.py, connector.py, etc.) 
3. **Automated Testing**: Python test functions validate the implementation
4. **Pass/Fail Results**: Comprehensive validation with detailed error reporting

### Example Benchmark Flow
```yaml
# From domains/core/core.yaml
- name: "hello"
  description: "Create a program that prints 'Hello World'"
  tests:
    - function_to_run: |
        def test_hello_world(zerg_state=None):
          from main import hello_world  # AI must create this
          result = hello_world()
          assert result == "Hello World"
          return True
```

The AI must create `main.py` with a `hello_world()` function that returns exactly `"Hello World"`.

### Key Files to Understand
- `suite.yaml` - Main configuration, constants, common settings
- `domains/core/core.yaml` - Basic programming benchmarks
- `domains/connector/connector.yaml` - Enterprise service integrations
- `domains/cloud/cloud.yaml` - Web applications and cloud services
- `domains/test/test.yaml` - Environment and file format validation

### For AI Developers
If you're an AI system, pay attention to:
- **Import Patterns**: Tests expect specific module names (`main.py`, `connector.py`)
- **Function Signatures**: Test functions show exactly what interfaces to implement
- **Configuration Access**: Use `zerg_state.get("param_name").get("value")` for config values
- **Error Handling**: Implement proper timeouts and retry logic using system constants

### For Human Developers  
- Each benchmark is self-contained with requirements, tests, and validation
- Benchmarks inherit common configuration from `suite.yaml`
- Environment variables handle sensitive data (API keys, credentials)
- All numeric values are defined as named constants for maintainability

## System Architecture

ZAAI is built on a domain-driven architecture that organizes benchmarks by functional area and complexity. The system uses YAML manifest files to define benchmarks, test criteria, and execution parameters.

### Core Components

```
zaai/
├── suite.yaml                    # Main orchestration and common configuration
├── domains/                      # Domain-specific benchmark definitions
│   ├── core/
│   │   ├── core.yaml             # Core programming benchmarks
│   │   └── foobar.py             # Workspace reference classes
│   ├── connector/
│   │   └── connector.yaml        # Enterprise service integration benchmarks  
│   ├── cloud/
│   │   └── cloud.yaml            # Cloud application and deployment benchmarks
│   └── test/
│       ├── test.yaml             # Environment and file format testing
│       └── environment_test/     # Sample files for format validation
```

### Configuration Inheritance Model

The system follows a hierarchical configuration pattern:

1. **suite.yaml** - Defines system-wide defaults, constants, and common configurations
2. **Domain YAML files** - Inherit common settings and define domain-specific benchmarks
3. **Individual benchmarks** - Can override domain and system defaults as needed

### Benchmark Domains

#### Core Domain (`domains/core/`)
Fundamental programming capabilities and basic system integration:
- **Basic Output**: Console applications, simple I/O operations
- **API Integration**: REST API consumption, HTTP client libraries  
- **Game Development**: Interactive applications, graphics programming
- **Email/SMS Services**: Third-party service integration patterns
- **Multi-file Projects**: Code organization, module management

#### Connector Domain (`domains/connector/`)
Enterprise SaaS platform integration and business tool connectivity:
- **Task Management**: Jira, Asana, Trello integration
- **Documentation**: Confluence knowledge management
- **Customer Support**: Zendesk ticket system integration
- **Version Control**: GitHub repository and issue management  
- **CRM**: Salesforce customer relationship management
- **ITSM**: ServiceNow IT service management workflows

#### Cloud Domain (`domains/cloud/`)
Modern web application development and cloud platform deployment:
- **Web Applications**: Flask, FastAPI, Django full-stack development
- **Cloud Services**: AWS, GCP, Azure service integration
- **Containerization**: Docker, Kubernetes deployment patterns
- **Database Integration**: SQL and NoSQL data persistence

#### Test Domain (`domains/test/`)
System capability validation and file format compatibility:
- **File Format Support**: PDF, images, vector graphics, source code
- **Environment Integration**: Workspace file mapping and access
- **Media Processing**: Image, document, and text file handling

## Execution Model

### Benchmark Definition Structure
Each benchmark is defined with four key components:

```yaml
- name: "benchmark_id"
  category: "Functional Category"  
  description: "Natural language requirement description"
  
  specs:                          # Success criteria and requirements
    - description: "What must be accomplished"
      preconditions: "Required setup or context"
      postconditions: "Expected outcomes and validation criteria"
      
  tests:                          # Automated validation functions
    - description: "Test scenario description"  
      function_to_run: !python/function |
        def test_function(zerg_state=None):
          # Validation logic with assertions
          return True
          
  references:                     # External resources and workspace files
    - description: "Resource description"
      file_path: "path/to/resource"
      workspace_path: "mapped/path"
      
  configs:                        # Benchmark-specific parameters
    - name: "parameter_name"
      description: "Parameter purpose and usage"  
      value: "parameter_value"
```

### Test Function Execution Pattern

Test functions follow a standardized pattern for AI validation:

1. **Import Pattern**: Functions import from expected modules (`main.py`, `connector.py`, etc.)
2. **State Access**: Configuration accessed via `zerg_state.get("param").get("value")`
3. **Assertion-Based Validation**: Success determined by assertion completion
4. **Error Handling**: Graceful handling of API failures and network issues

### Environment Variable Integration

Sensitive configuration (API keys, credentials) uses the `!env/var` directive:

```yaml
configs:
  - name: "api_token"
    description: "Service API authentication token"
    value: !env/var  # Loaded from environment at runtime
```

## AI Implementation Expectations

### Module Creation Patterns
AI implementations must create modules with expected interfaces:

- **Core Domain**: `main.py` with required functions, `game.py` with Game class
- **Connector Domain**: `connector.py` with service-specific connector classes  
- **Cloud Domain**: `app.py` with application factory patterns

### Workspace File Integration
Some benchmarks provide workspace files (like `foobar.py`) that AI code must import and use:

```python
# AI must create this pattern:
from workspace.foobar import Foo, Bar, Baz

def create_foo_bar_baz():
    return Foo(), Bar(), Baz()
```

### Error Handling Requirements
All network operations must implement:
- Timeout handling using `constants.DEFAULT_REQUEST_TIMEOUT_SECONDS`
- Retry logic up to `constants.DEFAULT_MAX_RETRIES` attempts  
- Graceful degradation for API rate limits and service unavailability

## System Constants

The system defines named constants to eliminate magic numbers:

```yaml
constants:
  DEFAULT_REQUEST_TIMEOUT_SECONDS: 60      # API call timeouts
  DEFAULT_MAX_RETRIES: 3                   # Retry attempt limits
  GAME_AUTO_EXIT_TIMEOUT_SECONDS: 10       # Test execution limits
  DEFAULT_API_RESULT_LIMIT: 10             # Result set pagination
  ALTERNATIVE_APPROACHES_TO_CONSIDER: 3    # Error recovery guidance
```

## Development Workflow

### Adding New Benchmarks

1. **Domain Selection**: Choose appropriate domain or create new domain directory
2. **Benchmark Definition**: Add benchmark entry to domain YAML file
3. **Test Function Creation**: Define validation logic with proper assertions  
4. **Configuration Setup**: Add necessary parameters and environment variables
5. **Documentation**: Include comprehensive descriptions and cross-references

### Testing Strategy

The system includes multiple validation layers:

- **Syntax Validation**: Code must parse and compile without errors
- **Functional Testing**: Core functionality must work as specified
- **Integration Testing**: External service connections must succeed  
- **Error Handling**: Failure modes must be handled gracefully
- **Security Validation**: No credentials exposed in code or logs

## Architecture Benefits

### Maintainability
- **Centralized Configuration**: Common settings managed in single location
- **Clear Separation**: Domain boundaries provide logical organization
- **Named Constants**: All numeric values have semantic meaning
- **Cross-Reference Documentation**: File relationships explicitly documented

### Scalability  
- **Domain Extension**: New capability areas easily added
- **Benchmark Growth**: Individual domains can expand independently
- **Configuration Inheritance**: New benchmarks inherit robust defaults
- **Parallel Execution**: Domain structure supports concurrent testing

### AI-First Design
- **Explicit Documentation**: All relationships and expectations clearly stated
- **Structured Data**: YAML provides machine-readable configuration
- **Predictable Patterns**: Consistent interfaces across all domains
- **Context Preservation**: zerg_state maintains execution context

This architecture enables comprehensive evaluation of AI coding capabilities across the full spectrum of modern software development while maintaining clarity and extensibility for future expansion.