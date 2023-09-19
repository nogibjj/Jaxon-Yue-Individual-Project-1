# IDS 706 Individual Project 1
[![OnInstall](https://github.com/nogibjj/Jaxon-Yue-Individual-Project-1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Jaxon-Yue-Individual-Project-1/actions/workflows/install.yml)
[![Format](https://github.com/nogibjj/Jaxon-Yue-Individual-Project-1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Jaxon-Yue-Individual-Project-1/actions/workflows/format.yml)
[![Lint](https://github.com/nogibjj/Jaxon-Yue-Individual-Project-1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Jaxon-Yue-Individual-Project-1/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/Jaxon-Yue-Individual-Project-1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Jaxon-Yue-Individual-Project-1/actions/workflows/test.yml)

### Video Walkthrough

### Overview
* This repository includes the components for Individual Project 1 - Continuous Integration using GitHub Actions of Python Data Science Project.

### Goal
* This project aims at implementing Continuous Integration (CI) using Github Actions for typical Data Science Exploratory Data Analysis projects.
* The EDA process includes getting essential statistics such as **mean**, **median**, and **standard deviation**, as well as data visualizations of a **histogram** and on the **growth of the average annual wages**.
* This repo also contains respective **tests** to check whether the statistics calculated in the EDA process **match with the real data points**.

### Project Structure:
- **`Jupyter Notebook (Project/notebook.ipynb)`**
    - Includes cells that perform descriptive statistics using Pandas
    - Tested using the nbval plugin for pytest
- **`Python Script (Project/script.py)`**
    - Includes same scripts that perform descriptive statistics using Pandas
- **`lib.py file (Project/lib.py)`**
    - Includes the shared code between the script and notebook
- **`Makefile`**
    - Includes and executes the following commands: **'Install'**, **'Format'**, **'Lint'**, **'Test''**
- **`Test Scripts`**
    - **`Project/test_script.py`**
        - Includes tests for the Python script
    - **`Project/test_lib.py`**
        - Includes tests for the library
- **`Requirements.txt`**
    - Includes the required packages
- **`GitHub Actions`**
    - Performs all commands in **'Makefile'**

### Results
Using Github Actions, I have passed make format, make lint, and make test as shown below.
