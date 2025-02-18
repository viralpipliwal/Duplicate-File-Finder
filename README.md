# Duplicate File Finder

## Overview

`Duplicate File Finder` is a Python program that helps users find and manage duplicate files within a specified directory and its subdirectories. The program uses a SHA-256 hash algorithm to identify duplicate files based on their content, ensuring that files with identical data are detected even if they have different names.

This project includes both a core script for finding duplicate files (`duplicate_file_finder.py`) and a graphical user interface (GUI) for easier interaction with the program (`duplicate_file_finder_ui.py`). 

### Key Features:
- Scans folders and subfolders for duplicate files based on their content (using SHA-256 hashing).
- Saves the list of duplicate files and their paths into a CSV file for easy reference.
- Provides a simple GUI built using `Tkinter` for user-friendly folder selection and scanning.

## Requirements

- Python 3.x
- `Tkinter` (for GUI)
- `hashlib` (for generating SHA-256 hashes)
- `os` (for file and directory operations)

## Installation

### 1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/duplicate-file-finder.git
