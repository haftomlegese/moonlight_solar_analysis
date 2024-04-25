# Moonlight Solar Analysis
This repository contains data analysis and visualization projects focusing on solar energy datasets. The repository includes notebooks for exploratory data analysis (EDA), a Streamlit dashboard application, datasets, unit tests, and configuration files for continuous integration.

## Repository Structure
```
.
├── notebook
│   ├── __init__.py
│   └── EDA.ipynb
├── app
│   ├── __init__.py
│   └── dashboard.py
├── data
│   ├── benin-malanville.csv
│   ├── sierraleone-bumbuna.csv
│   └── togo-dapaong_qc.csv
├── tests
│   ├── __init__.py
│   └── test_dashboard.py
├── requirements.txt
└── .github
    └── workflows
        └── unittests.yml
```

## Files Overview
* notebook/EDA.ipynb: Jupyter Notebook containing   exploratory data analysis for the three datasets (Benin, Sierra Leone, Togo).
* app/dashboard.py: Streamlit application file for visualizing solar energy data.
* data/:
    + benin-malanville.csv: Dataset for solar energy observations in Benin.
    + sierraleone-bumbuna.csv: Dataset for solar energy observations in Sierra Leone.
    + togo-dapaong_qc.csv: Dataset for solar energy observations in Togo.
* tests/test_dashboard.py: Unit tests for functions in app/dashboard.py.
* requirements.txt: List of required Python packages for running the project.
* .github/workflows/unittests.yml: GitHub Actions workflow file for running unit tests on push events.

## Steps to Run the Files
### 1. EDA Notebook (notebook/EDA.ipynb):
    * Ensure you have anaconda installed (pip install notebook).
    * Open anaconda
    * Launch Jupyter Notebook: jupyter notebook.
    * Access the notebook from the browser and execute cells to perform exploratory data analysis.
### 2. Streamlit Dashboard (app/dashboard.py):
    * Install required packages from requirements.txt: 
    "pip install -r requirements.txt."

    * Run the Streamlit application
    "streamlit run app/dashboard.py"
    * Open the provided URL in a web browser to interact with the solar energy dashboard.

### 3. Running Unit Tests:
    * Ensure you have Python and required packages installed (pip install -r requirements.txt).
    * Navigate to the project directory.
    * Run unit tests using the following command:
    "pytest"
    * Check the console output for test results.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Contributions are welcome!

## Issues and Feedback
If you encounter any issues or have suggestions for improvement, please open an issue on GitHub. Your feedback is valuable and helps in enhancing this project.