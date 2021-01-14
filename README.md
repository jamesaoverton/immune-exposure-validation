# Immune Exposure Validation

This repository contains scripts and data for building an ontology (OWL) file then validating immune exposure tables against that ontology using [ROBOT](http://robot.obolibrary.org). Note that this current requires a development version of ROBOT available here: [https://github.com/lmcmicu/robot/tree/add_validate_operation](https://github.com/lmcmicu/robot/tree/add_validate_operation)

# Prerequisites

* Python 3
* VALVE
* xlsx2csv
* COGS

# Installation

1. Make sure Python 3 is installed.
2. Clone the repository and enter `pip install -r requirements` on the terminal in the cloned repository.
3. Download or place your immune exposure table as a TSV or CSV file in the immune-exposure-validation directory. [TODO: Add details on how xlsx2csv and/or COGS might be used]
4. In order to use VALVE, the validation engine, there must be a `datatype`, `field`, and `rule` table. These tables are included to get you started. Please modify these as needed.
