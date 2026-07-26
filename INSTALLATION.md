# FinPulse Installation & Setup Guide

This guide provides step-by-step instructions for installing, configuring, and deploying the **FinPulse Personal Finance & Expense Analytics Platform**.

---

## 1. System Requirements

- **Operating System**: Windows 10/11, macOS 12+, or Ubuntu 20.04+
- **Node.js**: Version 18.0.0 or higher (v24.x recommended)
- **Package Manager**: npm 9+ or yarn 1.22+
- **Python**: 3.10+ (for documentation generation & automated tests)
- **Web Browser**: Google Chrome, Microsoft Edge, or Mozilla Firefox

---

## 2. Installation Steps

### Step 1: Clone / Navigate to Project Directory
```bash
cd C:\Users\kesha.000\.gemini\antigravity-ide\scratch\fintrack_app
```

### Step 2: Install Node.js Dependencies
```bash
npm install
```

### Step 3: Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp ../.env.example .env
```

### Step 4: Launch Application Server
```bash
npm start
```
*Output:*
`FinPulse application server running at http://localhost:3001`

---

## 3. Verifying Installation

Open your web browser and navigate to:
`http://localhost:3001`

You will immediately see the live interactive FinPulse dashboard initialized with pre-loaded sample income, expense, transaction, budget, and report data.
