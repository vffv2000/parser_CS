
# Project 

The project involved parsing the website [https://careerspace.app/](https://careerspace.app/) to gather information about job vacancies. The libraries used for this task were requests, BeautifulSoup, and Selenium.

# Description


The requests library was used to send requests to the server and retrieve data, including the HTML code of the web page. BeautifulSoup was used to analyze the HTML code and extract relevant data such as job title, company, location, salary, description, etc. Selenium, an automation tool for web browsers, was used to access dynamic elements on the web page that may not be accessible using requests and BeautifulSoup alone.

The project was implemented using the Python programming language, with Google Chrome as the browser since Selenium supports it natively. The application automatically launches the browser, opens the web page, extracts job vacancy information using BeautifulSoup, and returns the results.

Overall, this project involved gathering information about job vacancies from a website and could be used for analyzing job market trends, generating reports, job searching, and other purposes that require systematic information about job vacancies in a specific field.




# Technologies Used

-   Python

> The main programming language used for the project.

-   requests

> Python library used for making HTTP requests to the server.

-   BeautifulSoup

> Python library used for parsing HTML and XML documents.

-   Selenium

> Automation tool used for interacting with web browsers.

-   Google Chrome

> Web browser used for the project, since it is natively supported by Selenium.

-   Git

> Version control system used for tracking changes in the code.

-   GitHub

> Web-based hosting service used for version control and collaborative software development.

# How to Run

-   Clone the repository
-   Create a virtual environment and activate it
-   Install the required packages using the command `pip install -r requirements.txt`
-   Run the bot using the command `python main.py`

# Contributing

If you want to contribute to the project, you can fork the repository, make your changes, and submit a pull request. Please make sure to follow the coding style used in the project and include tests for your changes.
