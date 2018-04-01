Data Structure & Algorithms
Implementation queue class with follow methods:
- magic methods such as len and str to support user functionality and informative responses
- push which takes any value as an argument and adds that value to the top of the stack with an O(1) Time performance
- pop which takes no arguments and removes / returns the Node at the top of the stack
 - peek which takes no arguments and returns the Node at the top of the stack



Installation
Each project in the TOC is designed to be tested in an isolated virtual environment. This can be created as follows.

cd <project sub directory>
python3 -m venv ENV
. ENV/bin/activate Each project is also designed to support importing as a Python module.
Testing
Test fixtures can be found on 'conftest.py'
Test functions are in 'test_stack.py'