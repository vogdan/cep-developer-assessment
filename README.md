cep-developer-assessment
========================

This assessment contains three exercises that will help CEP evaluate a candidate's skills in software development that are relevant to CEP's work. Besides efficiency, CEP also looks for clarity in code submissions.

The assessment has three exercises that test a candidate's ability to work with CSV files, manipulate CSV data, and write JSON output files using existing Python packages.

It is recommended that the candidate has familiarity with the following software packages: `numpy`, `scipy`, and `pandas`. These packages will simplify the work required in the assessment.

# Instructions
For each exercise folder, there are three subfolders within:

* `input`: This folder contains all input files to be read by your program
* `output`: This folder contains "model" output files that your program ought to produce. For example, in exercise 1, there are two files in the `output` folder: `mean.csv` and `stats.csv`. Your program is expected to create these two files in the exact format and layout.
* `submissions`: This is where you can save your program in the format `your_name.py`

# Exercise 1
In spring 2014, CEP helped 9 foundation clients administered a survey to their grantees. At the end of the survey, CEP analysts cleaned and sent the data to you in a CSV format. The file is called `xl.csv` and saved in the `exercise1/input` folder. This file contains all survey responses, with each column representing a survey question and each row a set of responses from a grantee.

In this file, the column `fdntext` provides the client code for a given survey respondent, i.e., helps identify whose foundation the grantee respondent is 
