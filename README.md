# Immune Exposure Validation

This repository contains scripts and data for validating immune exposure tables using [VALVE](https://github.com/ontodev/valve).

# Prerequisites

* Python 3
* [valve.py](https://github.com/ontodev/valve.py/)
* [xlsx2csv](https://github.com/dilshod/xlsx2csv)

# Installation

1. Make sure Python 3 is installed.
2. Clone this repository.
3. In order to use VALVE, the validation engine, there must be `datatype`, `field`, and `rule` tables. These tables are included to get you started. Please modify these as needed. Refer to the [VALVE documentation](https://github.com/ontodev/valve/blob/main/README.md) for more information. There is also a `terminology` table that includes ontology terms that were used in immune exposure model described [here](https://academic.oup.com/database/article/doi/10.1093/database/baaa016/5818925).

# Validation and Extraction
1. If you have an immune exposure table or any related tables (such as `terminology`, `datatype`, etc.) in an Excel Workbook, please rename this file as `immune_exposure.xlsx` and run `make extract` to extract all sheets into `tables` directory. Note that if there is a sheet in the Excel file with the same name as the tables included in the `tables` directory, the Excel sheet will replace the contents of the provided table in the `tables` directory.
2. Run `make validate` to run validation. 