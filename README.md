# Domain Status Checker

This tool is designed to check the registration status of specified domains. It processes a list of domains provided by the user, checking each for its registration status. Developed for educational purposes, this tool can be used for domain research.

## Features

- Indicates whether the domains are available or not.

## Installation

To run this script, install the required Python libraries using the following command:

```bash
pip install requests
```

## Usage

Fill in the domains list with your domains and run the script. Example usage:

```python
domains = ['domain1.com', 'domain2.com', 'domain3.com']

for domain in domains:
    is_available = check_domain(domain)
    if is_available:
        print(f"{domain}: Available")
```

## Notes
This script is intended for educational and research purposes only.
Domain queries are performed via the API of the specified service provider.

## WARNING
Use this tool within legal and ethical boundaries.
The developer does not accept any responsibility for misuse of this tool.
