# Defendly - Complete User Installation Guide

## For New Users: How to Install & Run Defendly

---

## 📋 Prerequisites

Before you start, make sure you have:
- ✅ **Java JDK 17 or later** ([Download here](https://adoptium.net/))
- ✅ **Git** (optional, for cloning)
- ✅ **Internet connection** (only for initial download)

---

## 🚀 Method 1: Run from Source (Recommended)

### Step 1: Download Defendly

**Option A: Using Git**
```powershell
git clone https://github.com/PriyanshuChoubey0/defendly_scan.git
cd defendly_scan
```

**Option B: Download ZIP**
1. Go to: https://github.com/PriyanshuChoubey0/defendly_scan
2. Click green "**Code**" button → "**Download ZIP**"
3. Extract the ZIP file
4. Open folder in terminal/command prompt

### Step 2: Verify Java Installation

Check if Java is installed:
```powershell
java -version
```

You should see something like:
```
openjdk version "17.0.x" or higher
```

If not installed, download from: https://adoptium.net/

### Step 3: Run Defendly

**Windows:**
```powershell
.\gradlew.bat run
```

**Linux/Mac:**
```bash
./gradlew run
```

**First run takes 1-2 minutes** (builds the application)  
**Subsequent runs take 10-20 seconds**

### Step 4: Start Using Defendly!

Defendly will launch with:
- ✅ Main window with "Defendly" branding
- ✅ Quick Start tab
- ✅ Spider, Scanner, and all tools ready
- ✅ All 20 core add-ons loaded

---

## 📦 Method 2: Pre-built Executable (Coming Soon)

If you want a **ready-to-run version** without building:

### Step 1: Download Release
1. Go to: https://github.com/PriyanshuChoubey0/defendly_scan/releases
2. Download: `Defendly_X.X.X_Crossplatform.zip`
3. Extract the ZIP file

### Step 2: Run
**Windows:**
```
Double-click: defendly.bat
```

**Linux/Mac:**
```bash
./defendly.sh
```

That's it! No build required! 🎉

---

## 🎯 Quick Comparison

| Method | Pros | Cons | Best For |
|--------|------|------|----------|
| **Run from Source** | ✅ Always latest<br>✅ Can modify code<br>✅ Available now | ⚠️ First build takes time | Developers, testers |
| **Pre-built ZIP** | ✅ Instant run<br>✅ No build needed | ⚠️ Larger download | End users, quick testing |

---

## 🖥️ Complete Example (Windows User)

```powershell
# 1. Open PowerShell or Command Prompt
# Press Windows Key + R, type "powershell", press Enter

# 2. Navigate to where you want Defendly
cd C:\Users\YourName\Desktop

# 3. Clone the repository
git clone https://github.com/PriyanshuChoubey0/defendly_scan.git

# 4. Enter the folder
cd defendly_scan

# 5. Run Defendly
.\gradlew.bat run

# 6. Wait for build (first time only)
# Defendly window will open automatically!
```

---

## 🖥️ Complete Example (Linux/Mac User)

```bash
# 1. Open Terminal

# 2. Navigate to where you want Defendly
cd ~/Desktop

# 3. Clone the repository
git clone https://github.com/PriyanshuChoubey0/defendly_scan.git

# 4. Enter the folder
cd defendly_scan

# 5. Run Defendly
./gradlew run

# 6. Wait for build (first time only)
# Defendly window will open automatically!
```

---

## ✅ What You'll See When Running

### Terminal Output:
```
Starting a Gradle Daemon...
> Task :zap:run
[ZAP-BootstrapGUI] INFO - Loading extensions...
[ZAP-BootstrapGUI] INFO - Defendly started successfully
```

### Defendly Window:
- Title bar shows: **"Defendly"**
- Quick Start tab with options to scan websites
- Tools menu with Spider, Active Scan, etc.
- Clean interface without ZAP branding

---

## 🔍 How to Use Defendly

### Quick Start Scan
1. Click **"Quick Start"** tab
2. Enter target URL (e.g., `http://example.com`)
3. Click **"Attack"** button
4. Watch Defendly scan for vulnerabilities!

### Manual Testing
1. Set browser proxy to `localhost:8080`
2. Browse your target application normally
3. Defendly intercepts and analyzes all traffic
4. View findings in **"Alerts"** tab

---

## 🛠️ Troubleshooting

### Problem: "Java not found"
**Solution:** Install Java JDK 17+
```powershell
# Check Java version
java -version

# If not installed, download from:
https://adoptium.net/
```

### Problem: Build takes too long
**Solution:** This is normal for first run (downloads dependencies)
- First run: 1-3 minutes
- Subsequent runs: 10-20 seconds

### Problem: "Permission denied" (Linux/Mac)
**Solution:** Make gradlew executable
```bash
chmod +x gradlew
./gradlew run
```

### Problem: Port 8080 already in use
**Solution:** Another application is using the port
- Close other applications
- Or change Defendly port in Tools > Options > Local Proxies

---

## 📱 System Requirements

| Component | Requirement |
|-----------|-------------|
| **OS** | Windows 10+, Linux, macOS |
| **Java** | JDK 17 or later |
| **RAM** | 2 GB minimum, 4 GB recommended |
| **Disk Space** | 500 MB for source, 200 MB for pre-built |
| **Internet** | Only for initial download |

---

## 🎓 Next Steps

After launching Defendly:

1. **Learn the Basics**
   - Explore the Quick Start tab
   - Read built-in help (Help > User Guide)

2. **Configure Your Browser**
   - Set proxy to `localhost:8080`
   - Install Defendly root certificate

3. **Run Your First Scan**
   - Start with Quick Start automated scan
   - Try manual exploration mode

4. **View Results**
   - Check Alerts tab for findings
   - Generate reports (Report > Generate Report)

---

## 🆘 Getting Help

- **Documentation:** Built-in Help menu
- **Issues:** https://github.com/PriyanshuChoubey0/defendly_scan/issues
- **Original ZAP Docs:** https://www.zaproxy.org/docs/ (features are identical)

---

## ⚡ Super Quick TL;DR

```powershell
# Three commands to get started:
git clone https://github.com/PriyanshuChoubey0/defendly_scan.git
cd defendly_scan
.\gradlew.bat run

# That's it! 🎉
```
