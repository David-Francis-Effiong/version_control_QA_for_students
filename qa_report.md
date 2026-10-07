# QA Report

## Unit Tests Written
We created a suite of unit tests for the basic calculator functionality using the `pytest` framework. 
The tests cover:
- Addition: Tested with positive and mixed signed numbers.
- Subtraction: Tested normal subtraction and zero-subtraction scenarios.
- Multiplication: Tested positive and negative combinations.
- Division: Tested valid division and division by zero to ensure a `ValueError` is correctly raised.

## Linting and Code Style
We used `flake8` to perform static code analysis and ensure consistent style formatting across all Python files. 
- Early linting checks revealed missing spaces around operators and extra blank lines. These were corrected to adhere to PEP-8 standards.
- After cleanup, the linter reported zero stylistic errors and code complexity was well below the threshold of 10.

## Code Reviews
Code reviews were conducted via pull requests before merging branches to the main code base. 
Feedback highlighted the importance of informative docstrings, which were added to every function in `calculator.py`. 
By conducting code reviews, team members were able to spot logic edge cases (like dividing by zero) before they were deployed.
