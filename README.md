# Paiton Project

## Overview

Paiton is a file monitoring application that observes a specified folder for new files and organizes them into designated folders based on their prefixes and extensions. The application is designed to automate the process of file management, making it easier to keep track of files.

## Project Structure

``` plaintext
paiton
├── src
│   ├── Main.py          # Main logic for monitoring and moving files
│   ├── Config.py        # Configuration constants for folder paths and file types
│   └── setup.py         # Script for setting up configuration with folder picker
├── requirements.txt      # List of dependencies for the project
└── README.md             # Documentation for the project
```

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using the following command:

   ``` bash
   pip install -r requirements.txt
   ```

## Configuration

Before running the application, you need to set up the observable and destination folders. You can do this by running the `setup.py` script, which will prompt you to select the folders using a graphical folder picker dialog.

## Usage

To start monitoring the specified folder, run the `Main.py` script:

``` bash
python src/Main.py
```

The application will continuously check for new files in the observable folder and move them to the appropriate destination based on their prefixes and extensions.
