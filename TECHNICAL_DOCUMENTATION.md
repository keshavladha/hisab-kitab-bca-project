# FinPulse Technical & System Architecture Documentation

---

## 1. System Architecture
FinPulse is built following a modular **Model-View-Controller (MVC)** client-server paradigm:

- **Client Layer (View)**: HTML5, CSS3 with HSL Design Tokens, Vanilla JS SPA router, Chart.js for data visualizations.
- **Server Layer (Controller)**: Express.js REST API router running on Node.js runtime.
- **Data Layer (Model)**: Relational schema using SQLite / in-memory JS state engine with SQL DDL export capabilities.

---

## 2. Key Modules & Folder Structure

```
fintrack_app/
├── server.js              # Express REST API Server & Data Handlers
├── package.json           # Application Dependencies & Scripts
├── public/
│   ├── index.html         # Single Page Application Markup & View Containers
│   ├── styles.css         # Design System, Glassmorphism & Theme Styling
│   └── app.js             # Client SPA Router, Chart Rendering, State Management
```

---

## 3. Core Technical Features

### 3.1 Reactive Data Binding & Single Page Routing
View switching occurs without full browser reloads using DOM container toggling (`#view-dashboard`, `#view-income`, `#view-expense`, `#view-transactions`, `#view-budget`, `#view-reports`, `#view-profile`, `#view-settings`).

### 3.2 Dynamic Chart.js Integration
Financial data is compiled into datasets rendered across five canvas elements:
1. Income vs Expense 6-Month Bar Chart
2. Expense Category Donut Chart
3. Net Savings Trend Line Chart
4. Income Sources Pie Chart
5. Category Budget vs Actual Bar Chart

### 3.3 Security & Input Sanitization
- Cross-Site Scripting (XSS) prevention via `escapeHtml()` string sanitization.
- CORS policy protection on Express router.
- Input validation on all REST POST endpoints.
