# Defendly

[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://www.apache.org/licenses/LICENSE-2.0.html)

## About Defendly

Defendly is a security testing tool for web applications, forked from OWASP ZAP (Zed Attack Proxy). This is a white-labeled, independent version customized for enterprise security testing.

It can help you automatically find security vulnerabilities in your web applications while you are developing and testing your applications. It's also a great tool for experienced pentesters to use for manual security testing.

## Building Defendly

To build Defendly from source:

```bash
# Clone the repository
git clone https://github.com/PriyanshuChoubey0/defendly_scan.git
cd defendly_scan

# Build the distribution
./gradlew distCrossplatform

# The built artifacts will be in:
# zap/build/distributions/
```

## Running Defendly

After building, you can run Defendly from the distribution:

```bash
cd zap/build/distributions/
# Extract the ZIP file
# Run the appropriate script for your platform
```

Or run directly from source for development:

```bash
./gradlew run
```

## License

Defendly is licensed under the Apache License, Version 2.0. See LICENSE for details.

This project is a fork of OWASP ZAP (Zed Attack Proxy), originally developed by the ZAP Development Team and Checkmarx.

## Attribution

This software is derived from OWASP ZAP (https://www.zaproxy.org/), which is Copyright 2010-2024 The ZAP Development Team and licensed under the Apache License, Version 2.0.
