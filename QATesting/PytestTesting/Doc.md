PYTTEST
pytest: helps you write better programs
The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

An example of a simple test:

# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
To execute it:

$ pytest
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-6.x.y, py-1.x.y, pluggy-0.x.y
cachedir: $PYTHON_PREFIX/.pytest_cache
rootdir: $REGENDOC_TMPDIR
collected 1 item

test_sample.py F                                                     [100%]

================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_answer():
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

test_sample.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_sample.py::test_answer - assert 4 == 5
============================ 1 failed in 0.12s =============================
Due to pytest’s detailed assertion introspection, only plain assert statements are used. See Getting Started for more examples.

Features
Detailed info on failing assert statements (no need to remember self.assert* names)

Auto-discovery of test modules and functions

Modular fixtures for managing small or parametrized long-lived test resources

Can run unittest (including trial) and nose test suites out of the box

Python 3.6+ and PyPy 3

Rich plugin architecture, with over 315+ external plugins and thriving community

Run multiple tests
pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories. More generally, it follows standard test discovery rules.

Assert that a certain exception is raised¶
Use the raises helper to assert that some code raises an exception:

# content of test_sysexit.py
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
Execute the test function with “quiet” reporting mode:

$ pytest -q test_sysexit.py
.                                                                    [100%]
1 passed in 0.12s

