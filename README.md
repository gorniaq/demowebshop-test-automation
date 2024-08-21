# Demo Webshop Test Automation

This project contains automated tests for the Demo Webshop site using Python, Selenium, and Pytest.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)
- Chrome and/or Firefox browsers installed

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gorniaq/demowebshop-test-automation.git
   cd demowebshop-test-automation
   
2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt

3. Running Tests

   To run all tests:
      ```bash
      pytest
      ```
   To run tests and generate Allure reports:
      ```bash
      pytest --alluredir=allure-results
      allure serve allure-results
      ```
