# Contributing to Mermaid-py

Thank you for your interest in contributing to Mermaid-py! We welcome contributions from the community. This document provides guidelines and information to help you get started.

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to abide by its terms.

## Development Setup

### Prerequisites

- Python 3.9 or higher
- [uv](https://github.com/astral-sh/uv) for dependency management

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ouhammmourachid/mermaid-py.git
   cd mermaid-py
   ```

2. Install dependencies:
   ```bash
   make install
   ```

3. Install pre-commit hooks:
   ```bash
   make install/pre-commit
   ```

## Development Workflow

### Running Tests

Run the test suite:
```bash
make test
```

Run tests with coverage:
```bash
make coverage
```

### Code Quality

This project uses several tools to maintain code quality:

- **Ruff**: For linting and formatting
- **MyPy**: For static type checking
- **Pre-commit**: To run checks before commits

Run all linting and formatting checks:
```bash
make lint
```

### Local Development Server

For testing with local diagrams, you can run the mermaid.ink server locally:

Start the server:
```bash
make mermaid.ink/up
```

Stop the server:
```bash
make mermaid.ink/down
```

Set the `MERMAID_INK_SERVER` environment variable to use the local server.

## Making Changes

1. Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes, ensuring tests pass and code quality checks succeed.

3. Update documentation if necessary.

4. Commit your changes:
   ```bash
   git commit -m "Description of your changes"
   ```

5. Push your branch and create a pull request.

## Pull Request Guidelines

- Ensure your PR has a clear title and description
- Reference any related issues
- Keep PRs focused on a single feature or fix
- Ensure all tests pass
- Update documentation if needed
- Follow the existing code style

## Project Structure

- `mermaid/`: Main package code
- `tests/`: Test files
- `docs/`: Documentation
- `pyproject.toml`: Project configuration
- `Makefile`: Common development tasks

## Questions?

If you have questions about contributing, feel free to open an issue or discussion on GitHub.</content>
<parameter name="filePath">/workspaces/mermaid-py/CONTRIBUTING.md
