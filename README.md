# Typograph Service

Th script runs Flask server and builds the form based on template. The form is a typograph service which prepares a text to publish for web.


# How to Install

Before you start install packages via from **requirements.txt**.

```bash

$ pip install -r requirements.txt
```

and switch on/off debug mode in your .env file.

```
DEBUG=boolean

```

# Quickstart

1. Run **server.py**.

```bash

$ python server.py

 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with windowsapi reloader
 * Debugger is active!
 * Debugger PIN: 245-222-022
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

2. Goto [http://127.0.0.1:5000/typograph](http://127.0.0.1:5000/typograph) and check out it with your text


# Project Goals

The code is written for educational purposes on [DEVMAN.org](https://devman.org) course for web-developers.
