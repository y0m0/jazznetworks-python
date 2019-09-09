### Jazznetworks python test

1. Define a generator which generates the positive integers up to and including a supplied value
which are divisible by another supplied positive integer and use it to calculate the sum of all
positive integers less than 102030 which are divisible by 3.


2. Write a function which is passed an integer n, and returns a list of n lists such that:
```
f(0) returns []
f(1) returns [[1]]
f(2) returns [[1], [1,2]]
f(3) returns [[1], [1,2], [1,2,3]] etc. 
```

### How to
Clone the repo on your local machine, and verify that you have the correct
version of python installed.
The python version used for this project is 3.7.4.

In case it's not installed on your system it can be easily added with [pyenv](https://github.com/pyenv/pyenv)
```
pyenv install 3.7.4
```

The solutions to the two problems have been created on 2 separate files:
- ex1.py
- ex2.py

A set of test, created with pytest, can be run for each one of the two files.
To install the necessary dependencies, [pipenv](https://github.com/pypa/pipenv) can be unsed as follow:
```
pipenv install
```

To run the tests:
```
pipenv run pytest
```
