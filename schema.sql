-- =============================================================================
-- FinPulse - Smart Personal Finance & Expense Analytics Platform
-- Relational Database DDL Schema & Initial Seed Script (SQLite / PostgreSQL Compatible)
-- Author: BCA Project Engineering Team
-- Date: 2026-07-26
-- =============================================================================

PRAGMA foreign_keys = ON;

-- -----------------------------------------------------------------------------
-- Table 1: Users
-- Purpose: Stores authenticated user accounts, security hashes, and preferences
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'Member',
    currency VARCHAR(20) DEFAULT 'USD ($)',
    theme_preference VARCHAR(10) DEFAULT 'dark',
    notifications_enabled BOOLEAN DEFAULT 1,
    monthly_income_goal DECIMAL(12,2) DEFAULT 8500.00,
    monthly_expense_limit DECIMAL(12,2) DEFAULT 4200.00,
    avatar_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- Table 2: Categories
-- Purpose: Categories for organizing income and expense transactions
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category_name VARCHAR(50) NOT NULL,
    category_type VARCHAR(20) CHECK(category_type IN ('income', 'expense', 'both')),
    budget_limit DECIMAL(12,2) DEFAULT 0.00,
    color_hex VARCHAR(10) DEFAULT '#6366f1',
    icon_symbol VARCHAR(10) DEFAULT '📁',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- Table 3: Transactions
-- Purpose: Ledger of all financial transactions (Income & Expense entries)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category_id INTEGER,
    title VARCHAR(150) NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    type VARCHAR(20) NOT NULL CHECK(type IN ('income', 'expense')),
    category VARCHAR(50) NOT NULL,
    transaction_date DATE NOT NULL,
    status VARCHAR(30) DEFAULT 'Completed',
    note TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
);

-- -----------------------------------------------------------------------------
-- Table 4: Budgets
-- Purpose: Monthly category budget spending caps and warning thresholds
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS budgets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category VARCHAR(50) NOT NULL,
    monthly_limit DECIMAL(12,2) NOT NULL,
    warning_threshold DECIMAL(5,2) DEFAULT 80.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- Indices for Performance Optimization
-- -----------------------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_transactions_user_date ON transactions(user_id, transaction_date);
CREATE INDEX IF NOT EXISTS idx_transactions_type ON transactions(type);
CREATE INDEX IF NOT EXISTS idx_transactions_category ON transactions(category);

-- -----------------------------------------------------------------------------
-- Seed Initial User & Reference Data
-- -----------------------------------------------------------------------------
INSERT INTO users (id, full_name, email, password_hash, role, currency, theme_preference)
VALUES (1, 'Alex Morgan', 'alex.morgan@example.com', '$2a$10$e81Z...hashedPassword', 'Premium Member', 'USD ($)', 'dark');

INSERT INTO categories (user_id, category_name, category_type, budget_limit, color_hex, icon_symbol) VALUES
(1, 'Housing', 'expense', 2000.00, '#6366f1', '🏠'),
(1, 'Food & Groceries', 'expense', 500.00, '#10b981', '🛒'),
(1, 'Transportation', 'expense', 250.00, '#f59e0b', '⚡'),
(1, 'Entertainment', 'expense', 300.00, '#ec4899', '🎬'),
(1, 'Utilities', 'expense', 150.00, '#06b6d4', '💡'),
(1, 'Healthcare', 'expense', 300.00, '#8b5cf6', '🏥'),
(1, 'Shopping', 'expense', 400.00, '#ef4444', '🛍️'),
(1, 'Education', 'expense', 100.00, '#3b82f6', '📚');

INSERT INTO transactions (user_id, title, amount, type, category, transaction_date, note) VALUES
(1, 'TechCorp Salary', 6200.00, 'income', 'Salary', '2026-07-01', 'Monthly base salary compensation'),
(1, 'Freelance UI Design', 1450.00, 'income', 'Freelance', '2026-07-05', 'Client dashboard project payment'),
(1, 'Stock Dividends', 420.50, 'income', 'Investments', '2026-07-10', 'Quarterly index dividend payment'),
(1, 'Side Business Consulting', 800.00, 'income', 'Consulting', '2026-07-15', 'Cloud architecture review'),
(1, 'Luxury Apartment Rent', 1850.00, 'expense', 'Housing', '2026-07-02', 'Downtown flat monthly rent'),
(1, 'Whole Foods Market', 342.80, 'expense', 'Food & Groceries', '2026-07-04', 'Organic groceries'),
(1, 'Tesla Supercharging', 125.40, 'expense', 'Transportation', '2026-07-08', 'EV charging & highway toll'),
(1, 'Cloud Server Hosting', 89.99, 'expense', 'Utilities', '2026-07-11', 'AWS infrastructure hosting'),
(1, 'Gourmet Dining', 215.00, 'expense', 'Entertainment', '2026-07-14', 'Team celebration dinner'),
(1, 'Health Insurance', 260.00, 'expense', 'Healthcare', '2026-07-18', 'Monthly premium & gym pass'),
(1, 'Apple Studio Display', 499.00, 'expense', 'Shopping', '2026-07-20', 'Workstation monitor upgrade'),
(1, 'Udemy Tech Books', 45.00, 'expense', 'Education', '2026-07-22', 'System architecture learning');
