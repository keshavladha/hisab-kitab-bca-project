document.addEventListener('DOMContentLoaded', () => {
  // App State
  let appState = {
    user: null,
    transactions: [],
    categories: [],
    analytics: [],
    summary: {},
    currentView: 'dashboard',
    theme: 'dark'
  };

  // Chart Instances
  let chartTrend = null;
  let chartDonut = null;
  let chartSavings = null;
  let chartIncomePie = null;
  let chartCategoryBar = null;

  // Initialize App
  init();

  async function init() {
    setupEventListeners();
    await fetchDashboardData();
    setupCharts();
    renderAllViews();
  }

  // Setup Event Listeners
  function setupEventListeners() {
    // Navigation items
    document.querySelectorAll('.nav-item').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const view = btn.dataset.view;
        if (view) {
          switchView(view);
        } else if (btn.id === 'nav-landing') {
          switchView('landing');
        }
      });
    });

    // Mobile sidebar toggle
    document.getElementById('mobile-toggle').addEventListener('click', () => {
      document.getElementById('sidebar').classList.toggle('open');
    });

    // Theme Toggle Buttons
    document.getElementById('theme-toggle').addEventListener('click', toggleTheme);
    document.getElementById('settings-theme-btn')?.addEventListener('click', toggleTheme);

    // Quick Add Button & Modals
    document.getElementById('btn-quick-add').addEventListener('click', () => openTxModal());
    document.getElementById('btn-add-income-modal')?.addEventListener('click', () => openTxModal('income'));
    document.getElementById('btn-add-expense-modal')?.addEventListener('click', () => openTxModal('expense'));
    document.getElementById('close-tx-modal').addEventListener('click', closeTxModal);
    document.getElementById('cancel-tx-modal').addEventListener('click', closeTxModal);

    // Auth Modals
    document.getElementById('btn-show-login').addEventListener('click', () => openAuthModal('login'));
    document.getElementById('close-auth-modal').addEventListener('click', closeAuthModal);
    document.getElementById('tab-login').addEventListener('click', () => setAuthTab('login'));
    document.getElementById('tab-register').addEventListener('click', () => setAuthTab('register'));
    document.getElementById('landing-cta-register').addEventListener('click', () => openAuthModal('register'));
    document.getElementById('landing-cta-dashboard').addEventListener('click', () => switchView('dashboard'));

    // Transaction Search & Filters
    document.getElementById('tx-search')?.addEventListener('input', renderFullTxTable);
    document.getElementById('tx-type-filter')?.addEventListener('change', renderFullTxTable);
    document.getElementById('tx-category-filter')?.addEventListener('change', renderFullTxTable);

    // Forms
    document.getElementById('tx-form').addEventListener('submit', handleAddTransaction);
    document.getElementById('auth-form').addEventListener('submit', handleAuthSubmit);
    document.getElementById('profile-form').addEventListener('submit', handleProfileUpdate);

    // Export buttons
    document.getElementById('btn-export-csv')?.addEventListener('click', exportCSV);
    document.getElementById('btn-export-json')?.addEventListener('click', exportJSON);
    document.getElementById('dash-view-all-tx')?.addEventListener('click', () => switchView('transactions'));
  }

  // Fetch Dashboard Summary Data
  async function fetchDashboardData() {
    try {
      const res = await fetch('/api/dashboard/summary');
      const data = await res.json();
      if (data.success) {
        appState.summary = data.summary;
        appState.categories = data.categories;
        appState.analytics = data.analytics;
        await fetchAllTransactions();
      }
    } catch (err) {
      console.error("Failed to fetch dashboard data", err);
    }
  }

  async function fetchAllTransactions() {
    try {
      const res = await fetch('/api/transactions');
      const data = await res.json();
      if (data.success) {
        appState.transactions = data.transactions;
      }
    } catch (err) {
      console.error("Failed to fetch transactions", err);
    }
  }

  // Switch View
  function switchView(viewName) {
    appState.currentView = viewName;
    
    // Hide all view sections
    document.querySelectorAll('.view-section').forEach(sec => sec.classList.add('hidden'));

    // Deactivate all nav items
    document.querySelectorAll('.nav-item').forEach(btn => btn.classList.remove('active'));

    const targetView = document.getElementById(`view-${viewName}`);
    if (targetView) {
      targetView.classList.remove('hidden');
    }

    const activeNav = document.getElementById(`nav-${viewName}`);
    if (activeNav) {
      activeNav.classList.add('active');
    }

    // Update Header Title
    const titles = {
      dashboard: "Dashboard Overview - HisabKitab",
      income: "Income & Stipends Manager",
      expense: "Expenses & Swiggy Habits",
      transactions: "Full Transaction Ledger",
      budget: "Monthly Budget Planner & Caps",
      reports: "Charts & Visual Reports",
      profile: "Student Profile (Keshav Ladha)",
      settings: "Preferences & Theme",
      landing: "Welcome to HisabKitab"
    };

    document.getElementById('page-title').textContent = titles[viewName] || "Dashboard";

    // Close mobile menu if open
    document.getElementById('sidebar').classList.remove('open');

    // Re-render specific view items
    if (viewName === 'income') renderIncomeTable();
    if (viewName === 'expense') renderExpenseTable();
    if (viewName === 'transactions') renderFullTxTable();
    if (viewName === 'budget') renderBudgetCards();
    if (viewName === 'reports') updateReportCharts();
  }

  // Toggle Dark / Light Theme
  function toggleTheme() {
    const htmlEl = document.documentElement;
    const isDark = htmlEl.getAttribute('data-theme') === 'dark';
    const newTheme = isDark ? 'light' : 'dark';
    
    htmlEl.setAttribute('data-theme', newTheme);
    appState.theme = newTheme;

    document.getElementById('theme-icon').textContent = newTheme === 'dark' ? '🌙' : '☀️';
    document.getElementById('theme-text').textContent = newTheme === 'dark' ? 'Dark Mode' : 'Light Mode';

    // Re-render charts for theme contrast
    setupCharts();
  }

  // Render All Views
  function renderAllViews() {
    renderSummaryStats();
    renderRecentTxTable();
    renderIncomeTable();
    renderExpenseTable();
    renderFullTxTable();
    renderBudgetCards();
  }

  function renderSummaryStats() {
    const s = appState.summary;
    if (s.totalBalance !== undefined) {
      document.getElementById('stat-total-balance').textContent = `₹${s.totalBalance.toLocaleString('en-IN', {minimumFractionDigits: 2})}`;
      document.getElementById('stat-total-income').textContent = `₹${s.totalIncome.toLocaleString('en-IN', {minimumFractionDigits: 2})}`;
      document.getElementById('stat-total-expense').textContent = `₹${s.totalExpense.toLocaleString('en-IN', {minimumFractionDigits: 2})}`;
      document.getElementById('stat-net-savings').textContent = `₹${s.netSavings.toLocaleString('en-IN', {minimumFractionDigits: 2})}`;
    }
  }

  function renderRecentTxTable() {
    const tbody = document.getElementById('dash-tx-body');
    if (!tbody) return;
    tbody.innerHTML = '';

    const recent = appState.transactions.slice(0, 5);
    recent.forEach(tx => {
      const tr = document.createElement('tr');
      const isIncome = tx.type === 'income';
      tr.innerHTML = `
        <td><strong>${escapeHtml(tx.title)}</strong><br><small style="color:var(--text-muted)">${escapeHtml(tx.note || '')}</small></td>
        <td><span class="badge badge-accent">${escapeHtml(tx.category)}</span></td>
        <td>${tx.date}</td>
        <td><span class="badge ${isIncome ? 'badge-success' : 'badge-danger'}">${tx.type.toUpperCase()}</span></td>
        <td class="${isIncome ? 'amount-income' : 'amount-expense'}">${isIncome ? '+' : '-'}₹${tx.amount.toFixed(2)}</td>
        <td><span class="badge badge-success">${tx.status || 'Completed'}</span></td>
      `;
      tbody.appendChild(tr);
    });
  }

  function renderIncomeTable() {
    const tbody = document.getElementById('income-table-body');
    if (!tbody) return;
    tbody.innerHTML = '';

    const incomeList = appState.transactions.filter(t => t.type === 'income');
    incomeList.forEach(tx => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td><strong>${escapeHtml(tx.title)}</strong></td>
        <td><span class="badge badge-accent">${escapeHtml(tx.category)}</span></td>
        <td>${tx.date}</td>
        <td>${escapeHtml(tx.note || '-')}</td>
        <td class="amount-income">+$${tx.amount.toFixed(2)}</td>
        <td><button class="btn btn-sm btn-outline" onclick="deleteTx(${tx.id})">Delete</button></td>
      `;
      tbody.appendChild(tr);
    });
  }

  function renderExpenseTable() {
    const tbody = document.getElementById('expense-table-body');
    if (!tbody) return;
    tbody.innerHTML = '';

    const expenseList = appState.transactions.filter(t => t.type === 'expense');
    expenseList.forEach(tx => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td><strong>${escapeHtml(tx.title)}</strong></td>
        <td><span class="badge badge-warning">${escapeHtml(tx.category)}</span></td>
        <td>${tx.date}</td>
        <td>${escapeHtml(tx.note || '-')}</td>
        <td class="amount-expense">-$${tx.amount.toFixed(2)}</td>
        <td><button class="btn btn-sm btn-outline" onclick="deleteTx(${tx.id})">Delete</button></td>
      `;
      tbody.appendChild(tr);
    });
  }

  function renderFullTxTable() {
    const tbody = document.getElementById('full-tx-table-body');
    if (!tbody) return;
    tbody.innerHTML = '';

    const searchVal = document.getElementById('tx-search')?.value.toLowerCase() || '';
    const typeVal = document.getElementById('tx-type-filter')?.value || 'All';
    const catVal = document.getElementById('tx-category-filter')?.value || 'All';

    let filtered = appState.transactions.filter(t => {
      const matchSearch = t.title.toLowerCase().includes(searchVal) || (t.note && t.note.toLowerCase().includes(searchVal));
      const matchType = typeVal === 'All' || t.type === typeVal;
      const matchCat = catVal === 'All' || t.category === catVal;
      return matchSearch && matchType && matchCat;
    });

    filtered.forEach(tx => {
      const tr = document.createElement('tr');
      const isIncome = tx.type === 'income';
      tr.innerHTML = `
        <td>#${tx.id}</td>
        <td><strong>${escapeHtml(tx.title)}</strong><br><small style="color:var(--text-muted)">${escapeHtml(tx.note || '')}</small></td>
        <td><span class="badge badge-accent">${escapeHtml(tx.category)}</span></td>
        <td>${tx.date}</td>
        <td><span class="badge ${isIncome ? 'badge-success' : 'badge-danger'}">${tx.type.toUpperCase()}</span></td>
        <td><span class="badge badge-success">${tx.status || 'Completed'}</span></td>
        <td class="${isIncome ? 'amount-income' : 'amount-expense'}">${isIncome ? '+' : '-'}$${tx.amount.toFixed(2)}</td>
        <td><button class="btn btn-sm btn-outline" onclick="deleteTx(${tx.id})">Delete</button></td>
      `;
      tbody.appendChild(tr);
    });
  }

  function renderBudgetCards() {
    const container = document.getElementById('budget-cards-container');
    if (!container) return;
    container.innerHTML = '';

    appState.categories.forEach(cat => {
      const pct = Math.min(100, Math.round((cat.spent / cat.budget) * 100));
      const isOver = cat.spent > cat.budget;
      const isWarning = pct >= 80 && !isOver;

      let statusBadge = `<span class="badge badge-success">On Track</span>`;
      let barColor = cat.color || '#6366f1';

      if (isOver) {
        statusBadge = `<span class="badge badge-danger">Over Budget (${pct}%)</span>`;
        barColor = '#ef4444';
      } else if (isWarning) {
        statusBadge = `<span class="badge badge-warning">Near Cap (${pct}%)</span>`;
        barColor = '#f59e0b';
      }

      const div = document.createElement('div');
      div.className = 'budget-card';
      div.innerHTML = `
        <div class="budget-card-header">
          <span class="budget-category-title">${cat.icon || '📁'} ${escapeHtml(cat.name)}</span>
          ${statusBadge}
        </div>
        <div class="budget-amounts">
          <span>Spent: <strong>$${cat.spent.toFixed(2)}</strong></span>
          <span>Limit: <strong>$${cat.budget.toFixed(2)}</strong></span>
        </div>
        <div class="progress-bar-bg">
          <div class="progress-bar-fill" style="width: ${pct}%; background-color: ${barColor};"></div>
        </div>
      `;
      container.appendChild(div);
    });
  }

  // Setup & Render Chart.js
  function setupCharts() {
    const isDark = appState.theme === 'dark';
    const textColor = isDark ? '#9ca3af' : '#4b5563';
    const gridColor = isDark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.08)';

    // Chart 1: Dashboard Trend
    const ctxTrend = document.getElementById('chart-income-expense-trend')?.getContext('2d');
    if (ctxTrend) {
      if (chartTrend) chartTrend.destroy();
      chartTrend = new Chart(ctxTrend, {
        type: 'bar',
        data: {
          labels: appState.analytics.map(a => a.month),
          datasets: [
            {
              label: 'Monthly Income ($)',
              data: appState.analytics.map(a => a.income),
              backgroundColor: '#10b981',
              borderRadius: 6
            },
            {
              label: 'Monthly Expenses ($)',
              data: appState.analytics.map(a => a.expense),
              backgroundColor: '#ef4444',
              borderRadius: 6
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { labels: { color: textColor } } },
          scales: {
            x: { ticks: { color: textColor }, grid: { color: gridColor } },
            y: { ticks: { color: textColor }, grid: { color: gridColor } }
          }
        }
      });
    }

    // Chart 2: Expense Donut
    const ctxDonut = document.getElementById('chart-expense-donut')?.getContext('2d');
    if (ctxDonut) {
      if (chartDonut) chartDonut.destroy();
      chartDonut = new Chart(ctxDonut, {
        type: 'doughnut',
        data: {
          labels: appState.categories.map(c => c.name),
          datasets: [{
            data: appState.categories.map(c => c.spent),
            backgroundColor: appState.categories.map(c => c.color)
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { position: 'bottom', labels: { color: textColor, boxWidth: 12 } } }
        }
      });
    }
  }

  function updateReportCharts() {
    const isDark = appState.theme === 'dark';
    const textColor = isDark ? '#9ca3af' : '#4b5563';
    const gridColor = isDark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.08)';

    // Chart 3: Savings Trend (Line Chart)
    const ctxSavings = document.getElementById('report-savings-chart')?.getContext('2d');
    if (ctxSavings) {
      if (chartSavings) chartSavings.destroy();
      chartSavings = new Chart(ctxSavings, {
        type: 'line',
        data: {
          labels: appState.analytics.map(a => a.month),
          datasets: [{
            label: 'Net Monthly Savings ($)',
            data: appState.analytics.map(a => a.savings),
            borderColor: '#06b6d4',
            backgroundColor: 'rgba(6, 182, 212, 0.15)',
            fill: true,
            tension: 0.4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { labels: { color: textColor } } },
          scales: {
            x: { ticks: { color: textColor }, grid: { color: gridColor } },
            y: { ticks: { color: textColor }, grid: { color: gridColor } }
          }
        }
      });
    }

    // Chart 4: Income Sources Pie
    const ctxIncomePie = document.getElementById('report-income-pie-chart')?.getContext('2d');
    if (ctxIncomePie) {
      if (chartIncomePie) chartIncomePie.destroy();
      const incomeTx = appState.transactions.filter(t => t.type === 'income');
      const catTotals = {};
      incomeTx.forEach(t => { catTotals[t.category] = (catTotals[t.category] || 0) + t.amount; });

      chartIncomePie = new Chart(ctxIncomePie, {
        type: 'pie',
        data: {
          labels: Object.keys(catTotals),
          datasets: [{
            data: Object.values(catTotals),
            backgroundColor: ['#10b981', '#3b82f6', '#8b5cf6', '#f59e0b']
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { position: 'bottom', labels: { color: textColor } } }
        }
      });
    }

    // Chart 5: Category Bar Chart
    const ctxBar = document.getElementById('report-category-bar-chart')?.getContext('2d');
    if (ctxBar) {
      if (chartCategoryBar) chartCategoryBar.destroy();
      chartCategoryBar = new Chart(ctxBar, {
        type: 'bar',
        data: {
          labels: appState.categories.map(c => c.name),
          datasets: [
            {
              label: 'Allocated Budget ($)',
              data: appState.categories.map(c => c.budget),
              backgroundColor: 'rgba(99, 102, 241, 0.5)',
              borderColor: '#6366f1',
              borderWidth: 1
            },
            {
              label: 'Actual Spent ($)',
              data: appState.categories.map(c => c.spent),
              backgroundColor: 'rgba(239, 68, 68, 0.8)',
              borderRadius: 4
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { labels: { color: textColor } } },
          scales: {
            x: { ticks: { color: textColor }, grid: { color: gridColor } },
            y: { ticks: { color: textColor }, grid: { color: gridColor } }
          }
        }
      });
    }
  }

  // Modals & Handlers
  function openTxModal(prefillType = 'expense') {
    document.getElementById('tx-input-type').value = prefillType;
    document.getElementById('tx-input-date').value = new Date().toISOString().split('T')[0];
    document.getElementById('tx-modal').classList.remove('hidden');
  }

  function closeTxModal() {
    document.getElementById('tx-modal').classList.add('hidden');
  }

  async function handleAddTransaction(e) {
    e.preventDefault();
    const title = document.getElementById('tx-input-title').value;
    const amount = document.getElementById('tx-input-amount').value;
    const type = document.getElementById('tx-input-type').value;
    const category = document.getElementById('tx-input-category').value;
    const date = document.getElementById('tx-input-date').value;
    const note = document.getElementById('tx-input-note').value;

    try {
      const res = await fetch('/api/transactions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, amount, type, category, date, note })
      });
      const data = await res.json();
      if (data.success) {
        closeTxModal();
        await fetchDashboardData();
        renderAllViews();
        setupCharts();
      }
    } catch (err) {
      console.error("Error adding transaction", err);
    }
  }

  window.deleteTx = async function(id) {
    if (confirm("Are you sure you want to delete this transaction record?")) {
      try {
        const res = await fetch(`/api/transactions/${id}`, { method: 'DELETE' });
        const data = await res.json();
        if (data.success) {
          await fetchDashboardData();
          renderAllViews();
          setupCharts();
        }
      } catch (err) {
        console.error("Error deleting transaction", err);
      }
    }
  };

  function openAuthModal(mode = 'login') {
    setAuthTab(mode);
    document.getElementById('auth-modal').classList.remove('hidden');
  }

  function closeAuthModal() {
    document.getElementById('auth-modal').classList.add('hidden');
  }

  function setAuthTab(tab) {
    if (tab === 'login') {
      document.getElementById('tab-login').classList.add('active');
      document.getElementById('tab-register').classList.remove('active');
      document.getElementById('group-name').style.display = 'none';
      document.getElementById('auth-submit-btn').textContent = 'Sign In to FinPulse';
      document.getElementById('auth-modal-title').textContent = 'User Sign In';
    } else {
      document.getElementById('tab-register').classList.add('active');
      document.getElementById('tab-login').classList.remove('active');
      document.getElementById('group-name').style.display = 'flex';
      document.getElementById('auth-submit-btn').textContent = 'Create New Account';
      document.getElementById('auth-modal-title').textContent = 'Register New Account';
    }
  }

  async function handleAuthSubmit(e) {
    e.preventDefault();
    closeAuthModal();
    switchView('dashboard');
  }

  async function handleProfileUpdate(e) {
    e.preventDefault();
    const name = document.getElementById('prof-name').value;
    const email = document.getElementById('prof-email').value;
    const currency = document.getElementById('prof-currency').value;
    
    document.getElementById('sidebar-user-name').textContent = name;
    document.getElementById('profile-name-display').textContent = name;
    alert("Profile updated successfully!");
  }

  function exportCSV() {
    let csv = "ID,Title,Category,Date,Type,Status,Amount,Note\n";
    appState.transactions.forEach(t => {
      csv += `${t.id},"${t.title}","${t.category}",${t.date},${t.type},${t.status || 'Completed'},${t.amount},"${t.note || ''}"\n`;
    });
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `FinPulse_Transactions_${new Date().toISOString().split('T')[0]}.csv`;
    a.click();
  }

  function exportJSON() {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(appState, null, 2));
    const a = document.createElement('a');
    a.href = dataStr;
    a.download = `FinPulse_Backup_${new Date().toISOString().split('T')[0]}.json`;
    a.click();
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/[&<>"']/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' })[m]);
  }
});
