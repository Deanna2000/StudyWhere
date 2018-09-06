## Link to Ticket
Closes

## Description of Proposed Changes
-

## Steps to Test

Outline the steps to test

```
git fetch --all
git checkout
code .

```

1. navigate to the root
1. python manage.py makemigrations studywhereapp
1. python manage.py migrate
1. python manage.py runserver
1. login or register on view http://127.0.0.1:8000/

## Impacted Areas in Application

- browser views for user to add a new computer


## Definition of Done

1. The project must be fully documented. This includes the following:
    1. Complete README that documents the steps to install the code, how to install any dependencies, or system configuration needed.
    1. Every class must be documented with purpose, author, and methods.
    1. Every method must be documented with purpose and argument list - which itself must contain a short purpose for each argument.
1. The project must be able to run fully, and without errors, on each teammate's system.
1. Fulfills every requirement.
Every line of code has been peer reviewed.
1. For projects that require unit testing, core functionality must be identified and have at least one test for each.