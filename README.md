# Version Control, CI, and QA Project

## Overview
This project is designed to give high school students hands-on experience with version control (Git), Continuous Integration (CI), and Quality Assurance (QA). 

## Project Features
- A simple Python calculator (`calculator.py`).
- Unit tests using `pytest` to ensure correctness (`test_calculator.py`).
- Automated testing and linting via GitHub Actions (`.github/workflows/ci.yml`).

## Instructions
1. **Version Control**: Clone this repository, create a new branch for your features, stage and commit changes, and push them to GitHub.
2. **Continuous Integration**: When you push your code, GitHub Actions automatically runs the tests to ensure nothing breaks.
3. **Quality Assurance**: Make sure your code passes both the tests (via `pytest`) and the linter (via `flake8`).

## Running Locally
To run tests locally:
```bash
pip install -r requirements.txt
pytest
flake8
```
