# Pwned Password Checker

This Python script utilizes the Pwned Passwords API to assess the security of passwords by determining if they've been compromised in data breaches. The script hashes passwords and queries the API to evaluate their exposure, advising users to change vulnerable passwords if necessary.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

Online security is paramount, and passwords play a vital role in safeguarding sensitive information. The "Pwned Password Checker" aims to enhance password security by checking if passwords have been exposed in previous data breaches.

## Features

- Uses the Pwned Passwords API to check the vulnerability of passwords.
- Hashes passwords locally before querying the API, ensuring privacy.
- Provides guidance on whether a password needs to be changed based on its exposure status.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Adinyk03/password_checker.git
    ```

2. Install the required dependencies:

    ```bash
    pip install requests
    ```

## Usage

1. Run the script:

    ```bash
    python pwned_password_checker.py <password1> <password2> ...
    ```

   Replace `<password1>`, `<password2>`, etc., with the passwords you want to check.

2. The script will output the vulnerability status of each password provided.

## License

This project is licensed under the [MIT License](LICENSE).

