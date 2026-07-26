# FinPulse REST API Specification & Endpoint Documentation

This document outlines the complete REST API specification for the **FinPulse Personal Finance & Expense Analytics Platform**.

---

## Base URL
`http://localhost:3001/api`

---

## 1. Authentication Endpoints

### 1.1 Get Current Authenticated User Profile
- **Endpoint**: `GET /auth/me`
- **Headers**: `Authorization: Bearer <jwt_token>`
- **Response (200 OK)**:
```json
{
  "success": true,
  "user": {
    "id": 1,
    "name": "Alex Morgan",
    "email": "alex.morgan@example.com",
    "role": "Premium Member",
    "currency": "USD ($)",
    "theme": "dark"
  }
}
```

### 1.2 User Login
- **Endpoint**: `POST /auth/login`
- **Request Body**:
```json
{
  "email": "alex.morgan@example.com",
  "password": "Password123!"
}
```
- **Response (200 OK)**:
```json
{
  "success": true,
  "token": "jwt_mock_token_finpulse_98765",
  "user": { "id": 1, "name": "Alex Morgan" }
}
```

---

## 2. Dashboard & Financial Analytics Endpoints

### 2.1 Get Dashboard Financial Summary
- **Endpoint**: `GET /dashboard/summary`
- **Response (200 OK)**:
```json
{
  "success": true,
  "summary": {
    "totalBalance": 29943.31,
    "totalIncome": 8870.50,
    "totalExpense": 3427.19,
    "netSavings": 5443.31,
    "savingsRate": 61.4,
    "transactionCount": 12
  },
  "recentTransactions": [ ... ],
  "categories": [ ... ]
}
```

---

## 3. Transaction Management Endpoints

### 3.1 List Transactions
- **Endpoint**: `GET /transactions`
- **Query Parameters**:
  - `type`: `income` | `expense` (optional)
  - `category`: Category name string (optional)
  - `search`: Search query string (optional)
- **Response (200 OK)**:
```json
{
  "success": true,
  "count": 12,
  "transactions": [
    {
      "id": 101,
      "title": "TechCorp Salary",
      "amount": 6200.00,
      "type": "income",
      "category": "Salary",
      "date": "2026-07-01",
      "status": "Completed"
    }
  ]
}
```

### 3.2 Add Transaction
- **Endpoint**: `POST /transactions`
- **Request Body**:
```json
{
  "title": "Whole Foods Groceries",
  "amount": 120.50,
  "type": "expense",
  "category": "Food & Groceries",
  "date": "2026-07-26",
  "note": "Weekly grocery shopping"
}
```
- **Response (200 OK)**:
```json
{
  "success": true,
  "transaction": { "id": 1722000000, "title": "Whole Foods Groceries", ... }
}
```

### 3.3 Delete Transaction
- **Endpoint**: `DELETE /transactions/:id`
- **Response (200 OK)**:
```json
{
  "success": true,
  "message": "Transaction deleted successfully"
}
```

---

## 4. Budget & Category Endpoints

### 4.1 Get Category Budgets
- **Endpoint**: `GET /budgets`
- **Response (200 OK)**:
```json
{
  "success": true,
  "categories": [
    { "name": "Housing", "budget": 2000, "spent": 1850, "color": "#6366f1" }
  ]
}
```

---

## 5. System & Reports Endpoints

### 5.1 Get Financial Reports
- **Endpoint**: `GET /reports`
- **Response (200 OK)**:
```json
{
  "success": true,
  "expenseByCategory": { "Housing": 1850, "Shopping": 499 },
  "incomeByCategory": { "Salary": 6200, "Freelance": 1450 },
  "monthlyAnalytics": [ ... ]
}
```
