# File Monitoring Utility

This Python script is designed to monitor specified files within a directory and perform actions if those files are being overwritten. The `always_find()` method in the script continuously checks the specified files for any modifications. If a modification is detected, it creates a copy of the file mentioned in the `files_to_check` set and renames the copy with incremented names appended at the end of the original file name.

## Usage

### Prerequisites
- Python 3.x
- Required Python packages: `os`, `time` (built-in Python modules)

### Instructions

1. Clone or download the Python script to your local machine.

2. Ensure you have the correct file paths and file names set up in the script's driver code.

3. Run the script. If using a command-line interface, navigate to the directory containing the script and execute:

    ```
    python main.py
    ```

    Replace `main.py` with the name of the Python script file.

4. The script will continuously monitor the specified files in the specified directory. If any modifications are detected, it will create a copy of the file being modified and rename it with an incremented name at the end.

## Parameters

- `directory`: Path to the directory containing the files to be monitored.
- `min_`: Interval (in minutes) at which the script checks for modifications in the specified files.
- `files_to_check`: Tuple containing the names of the files to be monitored. If multiple files are specified, the script monitors all of them. If only one file is specified, the script monitors that file only.

## Example

```python
if __name__ == '__main__':
    # Example directory path
    path = r"C:\Users\Username\Documents\Example_Directory"
    
    # Example file names to monitor
    files_to_check = ("LeftIris.bmp", "RightIris.bmp")
    
    # Interval for checking modifications (in minutes)
    interval_minutes = 5
    
    # Call the always_find method
    always_find(path, interval_minutes, files_to_check)
