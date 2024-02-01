# Project Name

## Overview

This project is designed to process CSV files from a bank and perform various operations on the data to extract useful information. It leverages Python and includes modules for reading CSV files, defining bank structures, and processing data based on certain rules.

## Features

- **CSV File Processing:** The project processes a CSV file containing bank data.
- **Bank Module:** The `bank` module defines a structure for handling bank-related operations.
- **Data Processing:** The project includes functionality to remove column names, filter and sort data, and handle ambiguous data.
- **Category Management:** Categories are managed and compared, and priority exceptions are checked.
- **Export Functionality:** Processed data can be exported to a new CSV file.

## Getting Started

### Prerequisites

- Python installed (version 3.9.13)

### Installation

Clone the repository and go to project directory.

Install dependencies:
```
pip install -r requirements.txt
```

### Usage

1. Run the script:
    ```
    python bank_csv_converter.py input.csv output.csv
    ```

- input.csv - replace with the path to your input CSV file.
- (optional) output.csv - replace with the desired output file name.

### Contributing

If you'd like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: git checkout -b feature-name.
3. Make changes and commit: git commit -m 'Add new feature'.
4. Push to the branch: git push origin feature-name.
5. Submit a pull request.

### License

This project is licensed under the [MIT License](LICENSE.txt). See the [LICENSE.txt](LICENSE.txt) file for the full license text.
