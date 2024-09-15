# PersonalScripts 🚀

Welcome to **PersonalScripts**, a collection of Python scripts designed to simplify day-to-day development tasks, boost productivity, and eliminate repetitive work. This repository is continually updated as I add new scripts for personal use.

## Table of Contents

- [Overview](#overview)
- [Scripts](#scripts)
  - [say_hello](#say_hello)
  - [move_items_to_parent_and_cleanup](#move_items_to_parent_and_cleanup)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository serves as a personal toolbox where I store Python scripts that automate everyday tasks. These scripts help reduce manual, repetitive actions, and optimize common development workflows.

## How to Use

To use any of the scripts in this repository, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/PersonalScripts.git
    ```
2. Navigate to the repository directory:
    ```
    cd PersonalProjects
    ```
3. Run the main.py file:
    ```
    python3 main.py
    ```
4. The script will present you with a list of available functions. Select the desired option, and based on your choice, the program will prompt you for any additional inputs required (such as a file path, folder name, etc.). Follow the instructions on the command line to execute the chosen function.

## Scripts

### 1. `say_hello`

- **Purpose:** A simple function that prints a greeting message to the console.
- **Usage:** Run this function to display a message saying "Hello 😎".
  
### 2. `move_items_to_parent_and_cleanup`

- **Purpose:** Moves items from subfolders to their parent folder and deletes the empty subfolders afterward.
- **Usage:** Provide the path to the root folder, and the script will move the contents from each subfolder into its parent folder.
- **Example**:
   - If your root folder contains subfolders like this:
     ```
     root_folder/
     ├── parent_folder1/
     │   ├── subfolder1/
     │   │   ├── file1.txt
     │   │   └── file2.txt
     │   ├── subfolder2/
     │   │   └── file3.txt
     ├── parent_folder2/
     │   ├── subfolder3/
     │   │   └── file4.txt
     │   ├── subfolder4/
     │   │   └── file5.txt
     ```
   - After running the script, the folder will be flattened like this:
     ```
     root_folder/
     ├── parent_folder1/
     │   ├── file1.txt
     │   ├── file2.txt
     │   ├── file3.txt
     ├── parent_folder2/
     │   ├── file4.txt
     │   ├── file5.txt
     ```

## Contributing
As this repository is for personal use, contributions are not expected. However, feel free to check it out and make suggestions if you find something interesting!
