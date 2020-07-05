xox: lightweight virtualenv orchestration
=========================================

This project helps provision virtualenvs and dependencies for your Python code.
It works like tox_ or nox_, but your requirements are declared in your script.

Credit to the nox_ project for much of the implementation.


Installation
------------

Use pip::

    pip install --user xox


Usage
-----

Before you import any other third-party modules, call ``xox.activate()``::

    import xox

    xox.activate("lxml", "requests>=1.0")

    import lxml
    import requests

This will create a virtualenv, install packages, and call ``os.exec()`` to
replace the current process. The virtualenv will be re-used in subsequent runs.

You could also pass ``python='pythonX.Y'`` to specify a Python version, or
``silent=False`` to show output from ``pip``.

... And that's it! No custom executables or config files needed, just an extra
header in your script.


Notes
-----

Any code before your ``activate()`` call will be run twice: once without and
once within the virtualenv. Any code after your ``activate()`` call will run
only within the virtualenv.

Each virtualenv is stored in a subdirectory of system's temporary directory
named ``'xox-virtualenvs'``. No cleanup mechanism is provided - sorry!


.. _tox: https://tox.readthedocs.io
.. _nox: https://nox.thea.codes
