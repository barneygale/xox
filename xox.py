import hashlib
import os
import shutil
import sys
import tempfile

import pkg_resources

import nox.command
import nox.virtualenv


def activate(*packages, python=None, silent=True):
    """
    Ensure we run in a virtualenv with the given packages installed.

    This function may call `exec()` to replace the current process. It should
    be called before you import any required packages.

    :param packages: List of packages to pass to `pip install`
    :param python: Python version to pass to `virtualenv -p`
    :param silent: Whether to suppress output from `pip`
    """

    packages = [_requirement('xox')] + list(packages)
    tempdir = os.path.join(tempfile.gettempdir(), 'xox-virtualenv')
    venv = nox.virtualenv.VirtualEnv(
        location=os.path.join(tempdir, _sha1(python, *packages)),
        interpreter=python,
        reuse_existing=True)

    if tempdir in os.environ['PATH']:
        assert venv.bin in os.environ['PATH'], 'virtualenv already activated'
        return

    try:
        if venv.create():
            nox.command.run(
                args=['python', '-m', 'pip', 'install'] + list(packages),
                path=venv.bin,
                env=venv.env,
                silent=silent)
    except:
        if os.path.exists(venv.location):
            shutil.rmtree(venv.location)
        raise

    os.environ.update(venv.env)
    os.execvp('python', ['python'] + sys.argv)


def _requirement(package):
    """
    Returns a pip requirement for the given package.
    """

    return str(pkg_resources.require(package)[0].as_requirement())


def _sha1(*args):
    """
    Returns a sha1 hex digest of the given arguments
    """

    h = hashlib.sha1()
    for arg in args:
        if arg:
            h.update(arg.encode('utf8'))
    return h.hexdigest()
