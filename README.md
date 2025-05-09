# Consumer Complaints: Insight Application for Erika Jacobs

## Summary
This project reads a consumer complaints csv file and provides the financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.

## Environment
This project was developed using Python 3.8.2 and Ubuntu 20.04 (via Windows WSL). A version of Python 3.8 and a Linux environment will be required.

To ensure the version of your Python3 installation is compatible, please execute the following command on the Linux environment command line prior to execution:

```/usr/bin/python3 --version```

## Directions
After downloading a copy of this repository, place a "complaints.csv" file in the input folder within the main repository directory. Once this is complete, the code can be run.

The file "complaints.csv" can contain any columns in any order. However, the complaints.csv file *must* include the following columns in order to run successfully:
* Date received
* Product
* Company

The output of the code execution will be placed in the output folder within the main repository directory shortly after the code is run. The output will also be a csv file, featuring the following fields (In this order from left to right):
* Product
* Year
* Number of Complaints
* Number of Companies
* Largest Percentage of Complaints From Single Company

## How To Run
From the main repository directory on the Linux Command Line, type and execute the following code:

```sh run.sh```

## Test Suite Folder
The test suite folder features files that were used to validate the source code. The test suite includes the following tests:
* Test 1: Overall General Test - Provided By Insight
* Test 2: Tests company case sensitivity
* Test 3: Tests product case sensitivity
* Test 4: Tests product code for commas
* Test 5: Tests combinations of years and products out of order
* Test 6: Tests number of compaints
* Test 7: Tests number of companies receiving a complaint
* Test 8: Tests highest percentage of compaints directed at a single company

The csv for each test is located in the "input" folder of that test's directory as its own "complaints.csv" file. Each respective test can be placed into the input folder in the main directory of this repository to run the code. The csv output of each test is located in the output of that test's directory.

Example: Test 2 has an input file located at /insight_testsuite/test_2/input/complaints.csv, and has an output file located at /insight_testsuite/test_2/output/report.csv

## Source code
The source code is located in the src directory of the repository. 
