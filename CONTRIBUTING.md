# Contributing to ML Evaluation Metrics

First off, thank you for considering contributing to ML Evaluation Metrics! It's people like you who make this project a valuable resource for the machine learning community.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [How Can I Contribute?](#how-can-i-contribute)
4. [Style Guidelines](#style-guidelines)
5. [Development Process](#development-process)
6. [Documentation Guidelines](#documentation-guidelines)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

### Prerequisites

- Python 3.8+
- NumPy
- Pandas
- Scikit-learn
- PyTest (for running tests)

### Setting Up Development Environment

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/ml-evaluation-metrics.git
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

## How Can I Contribute?

### Reporting Bugs

- Check if the bug has already been reported in [Issues](issues)
- If not, create a new issue using the bug report template
- Include as much detail as possible:
  - Python version
  - Package versions
  - Error messages
  - Minimal reproducible example

### Suggesting Enhancements

- First, check if the enhancement has been suggested before
- Create a new issue using the feature request template
- Provide clear rationale and possible implementation details

### Adding New Metrics

1. **Research Phase**
   - Thoroughly research the metric
   - Document mathematical foundations
   - Identify use cases and limitations

2. **Implementation Requirements**
   - Create a new file in appropriate category folder
   - Include docstrings with LaTeX math formulas
   - Add type hints
   - Write comprehensive tests
   - Provide usage examples

3. **Documentation**
   - Mathematical explanation
   - Implementation details
   - Use cases
   - Visual examples (if applicable)

### Pull Request Process

1. Create a branch with a descriptive name:
   ```bash
   git checkout -b feature/add-new-metric
   # or
   git checkout -b fix/metric-calculation
   ```

2. Make your changes:
   - Write clean, documented code
   - Add tests
   - Update documentation

3. Test your changes:
   ```bash
   pytest tests/
   ```

4. Commit your changes:
   ```bash
   git add .
   git commit -m "feat: add new metric [metric name]"
   ```

5. Push to your fork and create a Pull Request

## Style Guidelines

### Python Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints
- Maximum line length: 88 characters
- Use docstring format:
  ```python
  def metric_function(y_true: np.ndarray, y_pred: np.ndarray) -> float:
      """
      Calculate metric value.

      Parameters
      ----------
      y_true : np.ndarray
          Ground truth values
      y_pred : np.ndarray
          Predicted values

      Returns
      -------
      float
          Metric value

      Examples
      --------
      >>> metric_function(np.array([1, 0]), np.array([1, 1]))
      0.5
      """
  ```

### Test Guidelines

- Write tests using pytest
- Cover edge cases
- Include both unit and integration tests
- Maintain test coverage above 90%

## Development Process

1. **Design Phase**
   - Research the metric
   - Document mathematical foundation
   - Plan implementation approach

2. **Implementation Phase**
   - Write core functionality
   - Add error handling
   - Optimize performance

3. **Testing Phase**
   - Write comprehensive tests
   - Verify edge cases
   - Check performance benchmarks

4. **Documentation Phase**
   - Update documentation
   - Add examples
   - Create visualizations

## Documentation Guidelines

### Metric Documentation Structure

1. **Theoretical Background**
   ```markdown
   ## Metric Name

   ### Mathematical Definition
   $$metric = formula$$

   ### Properties
   - Property 1
   - Property 2

   ### Use Cases
   - Use case 1
   - Use case 2
   ```

2. **Implementation Details**
   ```markdown
   ### Implementation Notes
   - Key considerations
   - Optimizations
   - Limitations

   ### Examples
   ```python
   example_code()
   ```
   ```

3. **Visual Examples**
   - Include relevant plots
   - Show comparisons
   - Demonstrate edge cases

---

## Questions or Need Help?

Feel free to:
- Open an issue
- Contact project maintainers
- Join our community discussions

## License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.
