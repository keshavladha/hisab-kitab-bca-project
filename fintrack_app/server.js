const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3001;

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// In-memory Database with realistic, human Indian data for HisabKitab
let state = {
  user: {
    id: 1,
    name: "Keshav Ladha",
    email: "keshav.ladha@college.edu.in",
    role: "BCA Final Year Student",
    currency: "INR (₹)",
    avatar: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=256",
    joinedDate: "2024-01-15",
    theme: "dark",
    notifications: true,
    monthlyIncomeGoal: 68000,
    monthlyExpenseLimit: 30000
  },
  transactions: [
    { id: 101, title: "Developer Stipend / Salary", amount: 45000.00, type: "income", category: "Salary", date: "2026-07-01", status: "Completed", note: "Monthly internship stipend" },
    { id: 102, title: "Freelance Client Website", amount: 15000.00, type: "income", category: "Freelance", date: "2026-07-05", status: "Completed", note: "Landing page design project" },
    { id: 103, title: "College Project Help", amount: 5000.00, type: "income", category: "Consulting", date: "2026-07-10", status: "Completed", note: "Python script debugging for classmate" },
    { id: 104, title: "Monthly Allowance", amount: 3000.00, type: "income", category: "Allowance", date: "2026-07-15", status: "Completed", note: "Sent by family for miscellaneous expenses" },
    { id: 105, title: "PG Flat Rent & Electricity", amount: 12500.00, type: "expense", category: "Housing", date: "2026-07-02", status: "Completed", note: "Room rent & AC electricity bill" },
    { id: 106, title: "Zomato & Swiggy Orders", amount: 4200.00, type: "expense", category: "Food & Swiggy", date: "2026-07-04", status: "Completed", note: "Late night biryani & pizza craving" },
    { id: 107, title: "Chai, Samosa & Tapri Snacks", amount: 1450.00, type: "expense", category: "Chai & Social", date: "2026-07-08", status: "Completed", note: "Daily tea & evening snacks with friends" },
    { id: 108, title: "Metro Card & Bike Petrol", amount: 2100.00, type: "expense", category: "Travel & Petrol", date: "2026-07-11", status: "Completed", note: "College commute & petrol refill" },
    { id: 109, title: "Mobile & Wifi Fiber Bill", amount: 799.00, type: "expense", category: "Utilities & Wifi", date: "2026-07-14", status: "Completed", note: "Unlimited 5G wifi plan" },
    { id: 110, title: "Myntra Clothes & Sneakers", amount: 3500.00, type: "expense", category: "Shopping", date: "2026-07-18", status: "Completed", note: "Impulse shopping sale discount" },
    { id: 111, title: "Gym Membership & Protein", amount: 1800.00, type: "expense", category: "Healthcare", date: "2026-07-20", status: "Completed", note: "Monthly gym subscription" },
    { id: 112, title: "Udemy Course & Tech Books", amount: 650.00, type: "expense", category: "Books & Learning", date: "2026-07-22", status: "Completed", note: "React & Node.js course certification" }
  ],
  categories: [
    { name: "Housing", budget: 15000, spent: 12500, icon: "🏠", color: "#6366f1" },
    { name: "Food & Swiggy", budget: 5000, spent: 4200, icon: "🍕", color: "#10b981" },
    { name: "Chai & Social", budget: 1500, spent: 1450, icon: "☕", color: "#f59e0b" },
    { name: "Travel & Petrol", budget: 3000, spent: 2100, icon: "🛵", color: "#ec4899" },
    { name: "Utilities & Wifi", budget: 1000, spent: 799, icon: "💡", color: "#06b6d4" },
    { name: "Healthcare", budget: 2000, spent: 1800, icon: "🏋️", color: "#8b5cf6" },
    { name: "Shopping", budget: 3000, spent: 3500, icon: "🛍️", color: "#ef4444" },
    { name: "Books & Learning", budget: 1000, spent: 650, icon: "📚", color: "#3b82f6" }
  ],
  monthlyAnalytics: [
    { month: "Feb 2026", income: 55000, expense: 22000, savings: 33000 },
    { month: "Mar 2026", income: 58000, expense: 24500, savings: 33500 },
    { month: "Apr 2026", income: 60000, expense: 23000, savings: 37000 },
    { month: "May 2026", income: 62000, expense: 28000, savings: 34000 },
    { month: "Jun 2026", income: 65000, expense: 26000, savings: 39000 },
    { month: "Jul 2026", income: 68000, expense: 26999, savings: 41001 }
  ]
};

// API Endpoints
app.get('/api/auth/me', (req, res) => {
  res.json({ success: true, user: state.user });
});

app.post('/api/auth/login', (req, res) => {
  const { email, password } = req.body;
  if (email && password) {
    res.json({ success: true, token: "jwt_mock_token_hisabkitab_12345", user: state.user });
  } else {
    res.status(400).json({ success: false, message: "Email and password are required" });
  }
});

app.post('/api/auth/register', (req, res) => {
  const { name, email, password } = req.body;
  if (name && email && password) {
    state.user.name = name;
    state.user.email = email;
    res.json({ success: true, token: "jwt_mock_token_hisabkitab_12345", user: state.user });
  } else {
    res.status(400).json({ success: false, message: "All fields are required" });
  }
});

app.get('/api/dashboard/summary', (req, res) => {
  const totalIncome = state.transactions
    .filter(t => t.type === 'income')
    .reduce((sum, t) => sum + t.amount, 0);
  
  const totalExpense = state.transactions
    .filter(t => t.type === 'expense')
    .reduce((sum, t) => sum + t.amount, 0);
  
  const netSavings = totalIncome - totalExpense;
  const savingsRate = totalIncome > 0 ? ((netSavings / totalIncome) * 100).toFixed(1) : 0;

  res.json({
    success: true,
    summary: {
      totalBalance: netSavings + 150000, // Reserve savings
      totalIncome,
      totalExpense,
      netSavings,
      savingsRate,
      transactionCount: state.transactions.length
    },
    recentTransactions: state.transactions.slice(-5).reverse(),
    categories: state.categories,
    analytics: state.monthlyAnalytics
  });
});

app.get('/api/transactions', (req, res) => {
  const { type, category, search } = req.query;
  let result = [...state.transactions];

  if (type) {
    result = result.filter(t => t.type === type);
  }
  if (category && category !== 'All') {
    result = result.filter(t => t.category === category);
  }
  if (search) {
    const q = search.toLowerCase();
    result = result.filter(t => t.title.toLowerCase().includes(q) || t.note.toLowerCase().includes(q));
  }

  res.json({ success: true, count: result.length, transactions: result.reverse() });
});

app.post('/api/transactions', (req, res) => {
  const { title, amount, type, category, date, note } = req.body;
  if (!title || !amount || !type || !category) {
    return res.status(400).json({ success: false, message: "Missing required transaction fields" });
  }

  const newTx = {
    id: Date.now(),
    title,
    amount: parseFloat(amount),
    type,
    category,
    date: date || new Date().toISOString().split('T')[0],
    status: "Completed",
    note: note || ""
  };

  state.transactions.push(newTx);

  if (type === 'expense') {
    const catObj = state.categories.find(c => c.name === category);
    if (catObj) {
      catObj.spent += parseFloat(amount);
    }
  }

  res.json({ success: true, transaction: newTx });
});

app.delete('/api/transactions/:id', (req, res) => {
  const id = parseInt(req.params.id);
  state.transactions = state.transactions.filter(t => t.id !== id);
  res.json({ success: true, message: "Transaction deleted successfully" });
});

app.get('/api/budgets', (req, res) => {
  res.json({ success: true, categories: state.categories });
});

app.post('/api/budgets', (req, res) => {
  const { category, budget } = req.body;
  const catObj = state.categories.find(c => c.name === category);
  if (catObj) {
    catObj.budget = parseFloat(budget);
    res.json({ success: true, category: catObj });
  } else {
    res.status(404).json({ success: false, message: "Category not found" });
  }
});

app.get('/api/reports', (req, res) => {
  const expenseByCategory = {};
  state.transactions.filter(t => t.type === 'expense').forEach(t => {
    expenseByCategory[t.category] = (expenseByCategory[t.category] || 0) + t.amount;
  });

  const incomeByCategory = {};
  state.transactions.filter(t => t.type === 'income').forEach(t => {
    incomeByCategory[t.category] = (incomeByCategory[t.category] || 0) + t.amount;
  });

  res.json({
    success: true,
    expenseByCategory,
    incomeByCategory,
    monthlyAnalytics: state.monthlyAnalytics
  });
});

app.get('/api/user/profile', (req, res) => {
  res.json({ success: true, user: state.user });
});

app.put('/api/user/profile', (req, res) => {
  const { name, email, currency, theme, monthlyIncomeGoal, monthlyExpenseLimit } = req.body;
  if (name) state.user.name = name;
  if (email) state.user.email = email;
  if (currency) state.user.currency = currency;
  if (theme) state.user.theme = theme;
  if (monthlyIncomeGoal) state.user.monthlyIncomeGoal = parseFloat(monthlyIncomeGoal);
  if (monthlyExpenseLimit) state.user.monthlyExpenseLimit = parseFloat(monthlyExpenseLimit);

  res.json({ success: true, user: state.user });
});

app.listen(PORT, () => {
  console.log(`HisabKitab application server running at http://localhost:${PORT}`);
});

module.exports = app;
