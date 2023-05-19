# Playwright Python Example

[Tech](#tech) |
[Installation](#installation) |
[Running Tests](#running) |
[Test Reports](#reports) |
[Troubleshooting](#troubleshooting)

<a name="tech"/></a>

## Tech Stack

[Python](python.org) - Interpreted high-level general-purpose programming language <br/>
[Pytest](https://docs.pytest.org/en/latest/) - Python testing framework <br/>
[Playwright](https://playwright.dev/) - Library to automate Chromium, Firefox and WebKit with a single API <br/>

<a name="installation"/></a>
## What is Playwright?

Inside this project, create a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html)
using the [venv](https://docs.python.org/3/library/venv.html) module
to manage dependency packages locally:

```bash
$ python3 -m venv venv
```

Creating a new virtual environment for each Python project is a recommended practice.
This command will create a subdirectory named `venv` that holds all virtual environment files, including dependency
packages.

After creating a virtual environment, you must "activate" it.
On macOS or Linux, use the following command:

```bash
$ source venv/bin/activate
```

The equivalent command for a Windows command line is:

```
> venv\Scripts\activate.bat
```

You can tell if a virtual environment is active if its name appears in the prompt.

Let's add some Python packages to our new virtual environment:

```bash
pip3 install -r requirements.txt
```

Notice that pip fetches dependencies of dependencies.
It is customary for Python projects to store this list of dependencies in a file named `requirements.txt`.

After the Python packages are installed, we need to install the browsers for Playwright.
The `playwright install` command installs the latest versions of the three browsers that Playwright supports:
Chromium, Firefox, and WebKit:

```bash
$ playwright install
```

By default, pytest with the Playwright plugin will run headless Chromium.


<a name="running"/></a>
## Running Tests
### Running Tests Locally
To run the tests locally, run the following command:

```bash
$ python3 -m pytest
```

pytest should discover, run, and pass the single test case under the `tests` directory.
I would recommend running the tests with the `--slowmo` option to slow down the test execution at least 1000ms.

### Running Tests with different browsers
To run the tests with different browsers, run the following command:

```bash
$ python3 -m pytest --browser firefox 
```

### Running Tests in Docker
To run the tests in Docker, run the following command:

```bash
$ docker build -t automation-image .
$ docker run -it automation-image bash
$ python3 -m pytest
```

[//]: # (TODO: combine allure results from multiple json files)
<a name="reports"/></a>
## Test Reports
### Allure Reports in local
[Allure](https://docs.qameta.io/allure-report/#_pytest) test reports are generated in the `reports/allure-results` directory.
To view the test report, run the following command:

```bash
$ allure serve reports/allure-results/
```

### Allure Reports in Docker
To view the test report in Docker, run the following command:

```bash
$ docker run -p 5050:5050 -e CHECK_RESULTS_EVERY_SECONDS=3 -e KEEP_HISTORY=1 \
                 -v ${PWD}/reports/allure-results:/app/allure-results \
                 -v ${PWD}/reports/allure-reports:/app/default-reports \
                 frankescobar/allure-docker-service

```
Visit for reports: http://localhost:5050/allure-docker-service/latest-report