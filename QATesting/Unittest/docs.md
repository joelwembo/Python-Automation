PYTHON TESTING  UNITTEST
Overview
unittest is the standard Python unit testing framework. Inspired by JUnit, it is included with the standard CPython distribution. unittest provides a base class named TestCase, which provides methods for assertions and setup/cleanup routines. All test case classes must inherit from TestCase. Each method in a TestCase subclass whose name starts with “test” will be run as a test case. Tests can be grouped and loaded using the TestSuite class and load methods, which together can build custom test runners. unittest can also generate XML reports (like JUnit) using unittest-xml-reporting.

unittest is supported in both Python 2 and 3. However, use the unittest2 backport for versions earlier than Python 2.7.

Installation
Basic unittest does not need any special installation because it comes with Python. However, additional modules may be installed with pip if you need them:

> pip install unittest2
> pip install unittest-xml-reporting