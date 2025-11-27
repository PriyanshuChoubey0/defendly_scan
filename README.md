# Defendly - Security Testing Tool

[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://www.apache.org/licenses/LICENSE-2.0.html)

**Defendly** is a powerful security testing tool for web applications. It's a white-labeled fork of OWASP ZAP (Zed Attack Proxy) with custom branding and disabled auto-updates for enterprise use.

---

## 🚀 Quick Start (Clone and Run)

### Prerequisites
- **Java JDK 17 or later** (JDK 21 recommended)
- **Git**

### Step 1: Clone the Repository
```bash
git clone https://github.com/PriyanshuChoubey0/defendly_scan.git
cd defendly_scan
```

### Step 2: Build Defendly
```bash
# On Windows:
.\gradlew.bat distCrossplatform

# On Linux/Mac:
./gradlew distCrossplatform
```

**Build time:** ~2-5 minutes (first build downloads dependencies)

### Step 3: Run Defendly

After the build completes:

1. Navigate to: `zap/build/distributions/`
2. Extract the ZIP file: `Defendly_X.X.X_Crossplatform.zip`
3. Run the launcher:
   - **Windows:** `defendly.bat`
   - **Linux/Mac:** `./defendly.sh`

**Or run directly from source:**
```bash
.\gradlew.bat run
```

---

## ✨ What You Get

- ✅ **Fully functional web app security scanner**
- ✅ **Rebranded as "Defendly"** - no ZAP references in UI
- ✅ **No auto-updates** - complete control over versions
- ✅ **No external connections** - works offline
- ✅ **100% feature parity** - all original ZAP features work identically

---

## 📋 Features

All the powerful features of OWASP ZAP:
- **Intercepting Proxy** - Intercept and modify HTTP/HTTPS traffic
- **Active Scanning** - Automated vulnerability detection
- **Passive Scanning** - Background analysis while browsing
- **Spider/Crawler** - Automatic site mapping
- **Fuzzing** - Test input validation
- **API Testing** - REST, SOAP, GraphQL support
- **Extensive Add-ons** - Manual installation supported

---

## 🔧 Development

### Project Structure
```
defendly_scan/
├── zap/                          # Main application code
│   ├── src/main/
│   │   ├── java/                 # Java source
│   │   ├── resources/            # Assets & configs
│   │   └── dist/                 # Distribution files
│   └── build/
│       └── distributions/        # Built packages
├── buildSrc/                     # Build scripts
└── gradle/                       # Gradle wrapper
```

### Build Commands
```bash
# Clean build
.\gradlew.bat clean

# Build distribution
.\gradlew.bat distCrossplatform

# Run from source
.\gradlew.bat run

# Run tests
.\gradlew.bat test
```

---

## 📖 Documentation

- See [BUILDING.md](BUILDING.md) for detailed build instructions
- Configuration is stored in: `~/.ZAP/config.xml`
- Logs are in: `~/.ZAP/zap.log`

---

## 🎯 Use Cases

- Penetration testing
- Security regression testing
- CI/CD integration
- Developer security training
- API security testing

---

## 🔒 Security Note

**Only use Defendly against applications you have permission to test.**

Unauthorized scanning may be illegal in your jurisdiction.

---

## 📜 License

Licensed under the Apache License, Version 2.0.

This project is a fork of [OWASP ZAP](https://www.zaproxy.org/), Copyright 2010-2024 The ZAP Development Team.

---

## 🙏 Attribution

Defendly is based on the excellent work of:
- **OWASP ZAP** - The original Zed Attack Proxy
- **ZAP Development Team** & **Checkmarx**

For the original project, visit: https://www.zaproxy.org/

---

## 📞 Support

This is a white-labeled fork for internal use. For support:
- Check logs in `~/.ZAP/zap.log`
- Review configuration in `~/.ZAP/config.xml`
- Consult original ZAP documentation (features are identical)

---

**Ready to scan? Clone, build, and run! 🎉**
