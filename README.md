# phbs-qps-2024

#project web: https://github.com/Lamperouge777/phbs-qps-2024

Homework 1: Getting started： fetch the US CPI data and reports the last 4 quarters of inflation in the US

US CPI Data Fetching and Analysis
Project Overview
This project aims to fetch the US Consumer Price Index (CPI) data from FRED (Federal Reserve Economic Data) using Python scripts and calculate the inflation rate for the last four quarters.

Directory Structure
project/
│

├── scripts/

│   └── fetch_cpi_data.py    # Script to fetch CPI data and calculate inflation rate
│

└── src/requirements.txt

└── data/result.png

└── notebooks/crawler.ipynb

# Other project source code
Dependencies
pandas
pandas-datareader
requests


You can install all dependencies using the following command:

pip install pandas pandas-datareader requests
Usage Instructions
1. Make sure you have installed all dependencies.

2. Save the fetch_cpi_data.py script to the scripts folder.

3. Open Visual Studio Code and navigate to the project directory.

4. Run the following command in the integrated terminal:


python scripts/fetch_cpi_data.py
Output
The script will output the inflation rate for the last four quarters in the US.

Notes
Please ensure that your Python environment is properly configured and can run Python scripts.
If there is a network issue, you may not be able to fetch data from FRED. Please check your network connection.
Contributors
If you have any questions or suggestions, please feel free to submit an issue or pull request.

---

This project is licensed under the MIT License. For more information, please refer to the LICENSE file.

