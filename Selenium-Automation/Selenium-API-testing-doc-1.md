In order to provide effective and efficient software testing services, IT enterprises globally are implementing various automation solutions. At Evoke, we have been actively offering automation solutions for numerous customer engagements across multiple industry verticals. Our team is constantly developing new and innovative approaches for test automation utilizing Selenium framework, thereby helping enterprises to improve their service quality and reduce costs.

As part of this endeavor, we have come out with a Selenium framework that helps testing teams to automate the validations of URL based APIs and Microsoft Excel spreadsheets. The Selenium driven framework developed by Evoke automates submission of requests and validates the response using a web browser, thus reducing significant manual effort.

Selenium Based Automation Regression Suite
The below Selenium framework is a data driven solution consisting of:

Driver scripts developed in Java.
Test data provided in an Excel spreadsheet.
The Excel utility is developed in such a way that the URL based requests are dynamically created. While the driver code undertakes the following activities:

Reads the data from request column in an Excel spreadsheet.
Invokes the web browser and navigates to the URL based on the request.
Validates the response returned via browser body against the expected value in an Excel spreadsheet.
Updates the test case result in the spreadsheet.
Benefits of Selenium Framework
Preparing the test data and validating each scenario manually takes approximately 10 minutes.
To prepare the data and validate 350 scenarios takes approximately 7 man days per resource. However, with the implementation of the recommended selenium framework the time is reduced to 1.5 hours (approximately).
Selenium framework is easy to develop and the test cases can be maintained effortlessly, as all the test scenarios and test data are driven off the Excel spreadsheets.
This Selenium framework can be readily integrated with Continuous Integration (CI) build deployment process.
Manual Vs Automation Testing

Prerequisites
Below are some of the prerequisites to implement the Selenium framework:

NetBeans IDE
Microsoft Excel
JDK 1.8
Selenium-WebDriver-2.51.0 jar file
Poi-bin-3.13 jar file
javax.mail-1.3.3.01 jar file
Setting up the Environment
Before making use of the aforementioned Selenium framework, software testers need to set and configure the environment by downloading and installing the Java platform, Microsoft Excel and NetBeans IDE.

In the NetBeans IDE, create a new project with a Java application.

Click on the File menu and select ‘New Project’ in NetBeans IDE 8.1
Creating a new project in NetBeans IDE

Select ‘Java’ in categories and then select ‘Java Application’ in the ‘projects’ section and click on the ‘Next’ Button.
Choosing a project in NetBeans IDE

Provide a ‘Project Name’ and click on the ‘Finish Button’.
NetBeans IDE Finish Screen

Right click on the ‘Project Libraries’ folder and select ‘ADD JAR/Folder’.
Selecting the Project Libraries in NetBeans IDE

Select the jar files from your local machine and click on ‘Open’ button. The next step is to add the below mentioned jar files to the project.
Selenium-WebDriver-2.51.0
Poi-bin-3.13
Javax.mail-1.3.3.01
Adding JAR Folder

Provide the path or location of the Excel spreadsheet.
Location of the Excel spreadsheet in NetBeans IDE

Execution Process
Here’s the process to execute the Selenium framework.

Provide the API URL values in the Excel spreadsheet.
Create a new spreadsheet for execution of reports.
Include the sheet number in the ‘exeSheetNum’ variable.
Add the execution report sheet number into the ‘reportSheetNum’ variable.
Click on the ‘Run’ button on the NetBeans IDE.
The NetBeans IDE automatically launches the ‘Internet Explorer’ browser and passes the URL value into the browser. Subsequently, it obtains the response value and compares it with the expected value, thereby displaying the results (PASS/FAIL).
After successful execution of all the above steps, the execution reports are updated in the spreadsheet number mentioned in the Selenium framework.
Execution Reports in Microsoft Excel

Sample Test Scenario
Here’s a sample test scenario based on the above Selenium framework

Selenium Framework Sample Scenario

Conclusion
Selenium framework for URL based API testing, simplifies API validation by building test cases.  The same can be leveraged for a selenium driven automation engine to validate and update the test execution results.
