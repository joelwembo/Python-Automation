1.2. Installing Python bindings for Selenium
Use pip to install the selenium package. Python 3 has pip available in the standard library. Using pip, you can install selenium like this:

pip install selenium
You may consider using virtualenv to create isolated Python environments. Python 3 has venv which is almost the same as virtualenv.

You can also download Python bindings for Selenium from the PyPI page for selenium package. and install manually.

1.3. Instructions for Windows users
Install Python 3 using the MSI available in python.org download page.

Start a command prompt using the cmd.exe program and run the pip command as given below to install selenium.

C:\Python39\Scripts\pip.exe install selenium
Now you can run your test scripts using Python. For example, if you have created a Selenium based script and saved it inside C:\my_selenium_script.py, you can run it like this:

C:\Python39\python.exe C:\my_selenium_script.py
