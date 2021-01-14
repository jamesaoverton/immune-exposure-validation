# Immune Exposure Validation

This repository contains scripts and data for building an ontology (OWL) file then validating immune exposure tables against that ontology using [ROBOT](http://robot.obolibrary.org). Note that this current requires a development version of ROBOT available here: [https://github.com/lmcmicu/robot/tree/add_validate_operation](https://github.com/lmcmicu/robot/tree/add_validate_operation)

# Prerequisites

* Python 3
* VALVE
* xlsx2csv
* COGS

# Installation

1. Make sure Python 3 is installed.
2. Clone the repository.
3. In order to use VALVE, the validation engine, there must be a `datatype`, `field`, and `rule` table. These tables are included to get you started. Please modify these as needed. There is also a `terminology` table that includes ontology terms that were used in immune exposure model described [here](https://academic.oup.com/database/article/doi/10.1093/database/baaa016/5818925). 

# Validation and Extraction
1. If you have an immune exposure table or any related tables (such as `terminology`, `datatype`, etc.) in an Excel Workbook, please rename this file as `immune_exposure.xlsx` and run `make validate` to run extraction and validation. 
2. Note that if there is a sheet in the Excel file with the same name as the tables included in the `tables` directory, the Excel sheet will replace the contents of the provided table in the `tables` directory.
