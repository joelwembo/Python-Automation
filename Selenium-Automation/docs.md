# Selenium overview
Is Selenium for you? See an overview of the different project components.
Selenium is not just one tool or API but it composes many tools.

WebDriver
If you are beginning with desktop website or mobile website test automation, then you are going to be using WebDriver APIs. WebDriver uses browser automation APIs provided by browser vendors to control browser and run tests. This is as if a real user is operating the browser. Since WebDriver does not require its API to be compiled with application code, it is not intrusive. Hence, you are testing the same application which you push live.

IDE
IDE (Integrated Development Environment) is the tool you use to develop your Selenium test cases. It’s an easy-to-use Chrome and Firefox extension and is generally the most efficient way to develop test cases. It records the users’ actions in the browser for you, using existing Selenium commands, with parameters defined by the context of that element. This is not only a time-saver but also an excellent way of learning Selenium script syntax.

# Grid
Selenium Grid allows you to run test cases in different machines across different platforms. The control of triggering the test cases is on the local end, and when the test cases are triggered, they are automatically executed by the remote end.

After the development of the WebDriver tests, you may face the need of running your tests on multiple browser and operating system combinations. This is where Grid comes into the picture.

Selenium components
A deeper look at Selenium
Selenium is an umbrella project for a range of tools and libraries that enable and support the automation of web browsers.

Selenium components
Building a test suite using WebDriver will require you to understand and effectively use a number of different components. As with everything in software, different people use different terms for the same idea. Below is a breakdown of how terms are used in this description.

Terminology
API: Application Programming Interface. This is the set of “commands” you use to manipulate WebDriver.
Library: A code module which contains the APIs and the code necessary to implement them. Libraries are specific to each language binding, eg .jar files for Java, .dll files for .NET, etc.
Driver: Responsible for controlling the actual browser. Most drivers are created by the browser vendors themselves. Drivers are generally executable modules that run on the system with the browser itself, not on the system executing the test suite. (Although those may be the same system.) NOTE: Some people refer to the drivers as proxies.
Framework: An additional library used as a support for WebDriver suites. These frameworks may be test frameworks such as JUnit or NUnit. They may also be frameworks supporting natural language features such as Cucumber or Robotium. Frameworks may also be written and used for things such as manipulating or configuring the system under test, data creation, test oracles, etc.
The Parts and Pieces
At its minimum, WebDriver talks to a browser through a driver. Communication is two way: WebDriver passes commands to the browser through the driver, and receives information back via the same route.

Basic Communication
The driver is specific to the browser, such as ChromeDriver for Google’s Chrome/Chromium, GeckoDriver for Mozilla’s Firefox, etc. The driver runs on the same system as the browser. This may, or may not be, the same system where the tests themselves are executing.

This simple example above is direct communication. Communication to the browser may also be remote communication through Selenium Server or RemoteWebDriver. RemoteWebDriver runs on the same system as the driver and the browser.

# Remote Communication
Remote communication can also take place using Selenium Server or Selenium Grid, both of which in turn talk to the driver on the host system

Remote Communication with Grid
Where Frameworks fit in
WebDriver has one job and one job only: communicate with the browser via any of the methods above. WebDriver does not know a thing about testing: it does not know how to compare things, assert pass or fail, and it certainly does not know a thing about reporting or Given/When/Then grammar.

This is where various frameworks come in to play. At a minimum you will need a test framework that matches the language bindings, e.g. NUnit for .NET, JUnit for Java, RSpec for Ruby, etc.

The test framework is responsible for running and executing your WebDriver and related steps in your tests. As such, you can think of it looking akin to the following image.

Test Framework
Natural language frameworks/tools such as Cucumber may exist as part of that Test Framework box in the figure above, or they may wrap the Test Framework entirely in their own implementation.
