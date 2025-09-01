# Passwords-Bank

Passwords-Bank is a simple, secure desktop application for storing, generating, and managing your passwords. It provides an intuitive interface to save account credentials, generate strong passwords, and copy saved passwords to your clipboard.

---

## Table of Contents
- [Passwords-Bank](#passwords-bank)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [File Structure](#file-structure)
  - [Security Notes](#security-notes)
  - [Contributing](#contributing)
  - [License](#license)
  - [Screenshots](#screenshots)
---

## Features

- **Add New Account:** Save website, username/email, and password securely.
- **Password Generator:** Generate strong, random passwords.
- **Show Passwords:** View and copy your saved passwords.
- **Clipboard Copy:** Copy any password to your clipboard with one click.
- **Simple Navigation:** Easily switch between main menu, add account, and show passwords screens.

---

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd Passwords-Bank
   ```
2. **Install dependencies:**
   ```sh
   pip install customtkinter pyperclip
   ```
3. **Run the application:**
   ```sh
   python Home\ Page.py
   ```

---

## Usage

1. **Home Page:**
   - Choose to add a new account or view saved passwords.
2. **Add New Account:**
   - Enter the website, username/email, and password. You can generate a strong password automatically. Click "Save Password" to store your credentials.
3. **Show Passwords:**
   - View a list of saved accounts. Select an account and click "Copy Selected Password" to copy the password to your clipboard.

---

## File Structure

- `Home Page.py` — Main menu for navigation.
- `New Account.py` — Add new account credentials and generate passwords.
- `Show Passwords.py` — View and copy saved passwords.
- `passwords.json` — Stores your saved account data.
- `README.md` — Documentation.

---

## Security Notes
- Passwords are stored locally in a JSON file. For maximum security, consider encrypting this file or storing it in a secure location.
- Always use a strong master password for your device.
- Be cautious when copying passwords to the clipboard, as other applications may access clipboard data.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## License

This project is licensed under the MIT License.

---

## Screenshots

*Add screenshots or demo images here to showcase the application UI.*
