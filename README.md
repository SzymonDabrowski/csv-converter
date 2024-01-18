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

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-project.git
   ```

2. Navigate to project directory:
   ```
   cd your-project
   ```

3. Install dependencies (if any):
    ```
    pip install -r requirements.txt
    ```

### Usage

1. Run the script:
    ```
    python csv_wrapper.py input.csv output.csv
    ```

- Replace input.csv with the path to your input CSV file.
- Replace output.csv with the desired output file name.

### Contributing

If you'd like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: git checkout -b feature-name.
3. Make changes and commit: git commit -m 'Add new feature'.
4. Push to the branch: git push origin feature-name.
5. Submit a pull request.

### License

This project is licensed under the [MIT License](LICENSE.txt). See the [LICENSE.txt](LICENSE.txt) file for the full license text.
