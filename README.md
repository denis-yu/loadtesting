# load_testing.
Load testing project developed with Locust and based on Python.

## Setup the virtual environment.
In the project folder run the following commands.

```
$virtualenv venv1.0
$source venv1.0/bin/activate
$pip install -r requirements.txt
```

## Running the loading tests.
Follow the example below.
```
$source venv1.0/bin/activate
$locust -f <path/file_name.py> -u 5 - r 3 -t 15s --headless

To run the test, use the command like:
locust -f src/tests/user_scenario_1.py --web-host="127.0.0.1"
