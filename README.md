# FinPulse - Smart Personal Finance & Expense Analytics Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-v24.14-green.svg)](https://nodejs.org/)
[![Express](https://img.shields.io/badge/Express-v4.19-blue.svg)](https://expressjs.com/)

**FinPulse** is a full-stack personal finance and expense analytics web application designed for real-time transaction tracking, budget management, visual financial reporting, and personal financial management.

---

## 🌟 Key Features

- **Dashboard Overview**: Metrics for Total Reserve Balance, Monthly Income, Monthly Expenses, and Net Savings Rate.
- **Income Management**: Track income sources (Salary, Freelance, Dividends, Consulting).
- **Expense Management**: Log expenses with automatic category tagging and spending cap analysis.
- **Transaction History**: Filterable, searchable ledger table with CSV export.
- **Budget Planner**: Configure category monthly limits with progress indicators.
- **Visual Reports**: Interactive Bar, Pie, and Line charts powered by Chart.js.
- **User Profile & Settings**: Custom avatar, currency preferences ($ / ₹ / € / £), and Dark Mode.

---

## 📁 Repository Structure

```
scratch/
├── fintrack_app/            # Full-Stack Web Application Codebase
│   ├── server.js            # Express API Server
│   ├── package.json         # Node Dependencies
│   └── public/              # HTML5/CSS3/JS Frontend
├── assets/images/           # Captured Live Application Screenshots
├── schema.sql               # Database DDL Schema File
├── .env.example             # Environment Variables Example
├── API_DOCUMENTATION.md     # REST API Specifications
├── INSTALLATION.md          # Setup & Deployment Guide
├── USER_MANUAL.md           # End-User Operating Manual
├── TECHNICAL_DOCUMENTATION.md # Architecture & Design System
├── Project_Report.docx      # ~35 Page BCA Project Report (Word Format)
└── Project_Report.pdf       # Printable PDF Project Report
```

---

## 🚀 Quick Start

1. Start the application:
```bash
cd fintrack_app
npm install
npm start
```
2. Open `http://localhost:3001` in your browser.
