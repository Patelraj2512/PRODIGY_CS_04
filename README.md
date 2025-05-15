# Keylogger Tool

## Overview
This is a simple keylogger application built in Python that can record keyboard inputs. The project was developed as Task 4 for Prodigy InfoTech internship and is intended for **educational purposes only**.

## Features
- **Keystroke Recording**: Captures all keyboard inputs until ESC key is pressed
- **Log Management**: Read, delete, and backup log files
- **Security**: Encrypt log files for added protection
- **User-friendly Interface**: Simple menu-driven console interface

## Installation

### Prerequisites
- Python 3.6 or higher
- Required Python packages

### Setup
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/keylogger-tool.git
   cd keylogger-tool
   ```

2. Install the required dependencies:
   ```
   pip install pynput cryptography
   ```

## Usage

Run the application:
```
python task4.py
```

### Menu Options

1. **Start Keylogger**
   - Begins recording keystrokes
   - Press ESC key to stop recording

2. **Read Log File**
   - Displays the contents of the keylog.txt file

3. **Delete Log File**
   - Removes the keylog.txt file

4. **Backup Log File**
   - Creates a backup copy named backup_keylog.txt

5. **Encrypt Log File**
   - Encrypts the log file using Fernet encryption
   - Provides a key for later decryption

6. **Exit**
   - Closes the application

## Example

```
========= Keylogger Tool =========
1. Start Keylogger
2. Read Log File
3. Delete Log File
4. Backup Log File
5. Encrypt Log File
6. Exit

Enter your choice (1-6): 1
🎯 Keylogger started... Press ESC to stop.
```

## Important Notice

### Legal and Ethical Considerations

This keylogger tool is developed strictly for **educational purposes** to understand the concepts of input monitoring and basic encryption. Please be aware of the following:

- **Consent**: Always ensure you have explicit permission before monitoring anyone's keystrokes
- **Privacy**: Unauthorized use of keyloggers may violate privacy laws
- **Legal Restrictions**: Using keyloggers without consent is illegal in many jurisdictions

### Responsible Use

The developer of this tool is not responsible for any misuse or damage caused by this program. Users are expected to comply with all applicable laws and regulations regarding computer monitoring software.

## License

This project is available under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Prodigy InfoTech for the project assignment
- [pynput](https://pypi.org/project/pynput/) library for keyboard monitoring
- [cryptography](https://pypi.org/project/cryptography/) library for encryption functionality