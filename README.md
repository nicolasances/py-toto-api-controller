# ⚠️ DEPRECATED - Toto API Controller for Python

> **This project is deprecated and no longer maintained.**
> 
> Please visit the [Toto Microservice SDK Repository](https://github.com/nicolasances/toto-microservice-sdk) for the latest version of the Toto Microservice SDK, which supports both Node.js and Python.

---

This project aims at simplifying the creationg of python microservices using Flask, by creating some decorators to be added to routes (API endpoints) that take care of:
 - Basic validation of HTTP Headers
 - Authentication

This also provide simple logging utilities to uniform logs.

## Documentation
The documentation of the versions, including a general "How to" can be found here: 
 * [Version 2.0](./docs/v2.0.md)
 * [Version 1.1](./docs/v1.1.md)
 * [Version 1.0](./docs/v1.0.md)

## Building and Deploying to Pypi
Make sure you have the file `setup.py´ and that the dependencies are setup. <br>
To **build** the package, run: 
```
python setup.py sdist
```

To **upload** the package to PyPi, run:
```
twine upload dist/* 
```

Note that to **publish** packages to PyPi, you need to authenticate via token. <br>
The token needs to be stored in `$HOME/.pypirc` in this format: 
```
[pypi]
  username = __token__
  password = pypi-AgEIcHlwaS5vcmcCJDMwZDZlMjYzLWExZWUtNGI0ZC......
```
Note that the "username" value is the string `__token__`. The actual token only goes in the password field.

## Additional information
 * [Notes on starting and configuring a Python Virtual Environment](https://snails-shop-mta.craft.me/fo93w8gh34GEUH)
 * [How to build and deploy to Pypi]