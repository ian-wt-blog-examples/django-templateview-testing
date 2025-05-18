# django-templateview-testing

Check out my article [How to Test a Django TemplateView](https://ianwaldron.com/blog/how-to-test-a-django-templateview/) for more information.

## Setup

Once you've cloned a local copy of the repo, first create a virtual environment.

```shell
python3 -m venv env
```

This operation might take a few seconds. Once installed, activate the virtual environment.

```shell
source env/bin/activate
```

Next, install the requirements (Django, etc.)

```shell
pip install -r requirements.txt
```

## Run Tests

```shell
python manage.py test --verbosity 2
```
