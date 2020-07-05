box: lightweight virtualenv orchestration
=========================================

This project helps provision virtualenvs and dependencies for your Python code.
It works like tox_ or nox_, but your requirements are declared in your script.

Credit to the nox_ project for much of the implementation.


Installation
------------

Use pip::

    pip install --user box


Usage
-----

Before you import any other third-party modules, include code like::

    import box

    box.requires("lxml", "requests >= 1.0")

This will create a temporary virtualenv, install packages, and call
``os.exec()`` to replace the current process. Each virtualenv is stored in
the system's temporary directory and re-used when requirements are met. No
cleanup mechanism is provided - sorry!

.. _tox: https://tox.readthedocs.io
.. _nox: https://nox.thea.codes
