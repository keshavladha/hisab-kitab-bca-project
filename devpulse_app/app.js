document.addEventListener('DOMContentLoaded', () => {
  // Initialize Lucide icons
  if (window.lucide) {
    lucide.createIcons();
  }

  // Render Velocity Chart using Chart.js
  const ctx = document.getElementById('velocityChart').getContext('2d');
  const gradientPushes = ctx.createLinearGradient(0, 0, 0, 250);
  gradientPushes.addColorStop(0, 'rgba(59, 130, 246, 0.4)');
  gradientPushes.addColorStop(1, 'rgba(59, 130, 246, 0.0)');

  const gradientBuilds = ctx.createLinearGradient(0, 0, 0, 250);
  gradientBuilds.addColorStop(0, 'rgba(139, 92, 246, 0.4)');
  gradientBuilds.addColorStop(1, 'rgba(139, 92, 246, 0.0)');

  const velocityChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Jul 12', 'Jul 14', 'Jul 16', 'Jul 18', 'Jul 20', 'Jul 22', 'Jul 24', 'Jul 26'],
      datasets: [
        {
          label: 'Git Pushes',
          data: [42, 65, 54, 89, 72, 95, 110, 128],
          borderColor: '#3b82f6',
          backgroundColor: gradientPushes,
          fill: true,
          tension: 0.4,
          borderWidth: 3,
          pointRadius: 4,
          pointBackgroundColor: '#3b82f6'
        },
        {
          label: 'Successful Builds',
          data: [38, 58, 50, 82, 68, 90, 102, 122],
          borderColor: '#8b5cf6',
          backgroundColor: gradientBuilds,
          fill: true,
          tension: 0.4,
          borderWidth: 3,
          pointRadius: 4,
          pointBackgroundColor: '#8b5cf6'
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          labels: {
            color: '#9ca3af',
            font: { family: 'Inter', size: 12 }
          }
        }
      },
      scales: {
        x: {
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          ticks: { color: '#9ca3af' }
        },
        y: {
          grid: { color: 'rgba(255, 255, 255, 0.05)' },
          ticks: { color: '#9ca3af' }
        }
      }
    }
  });

  // Populate Real-Time Live Activity Feed
  const feedItems = [
    { type: 'commit', user: 'Alex Vance', text: 'pushed 3 commits to `main` in api-gateway', time: 'Just now' },
    { type: 'build', user: 'CI/CD Pipeline', text: 'Build #1,402 succeeded (took 1m 12s)', time: '2 mins ago' },
    { type: 'pr', user: 'Sarah Chen', text: 'opened Pull Request #48: Add Redis cache layer', time: '14 mins ago' },
    { type: 'commit', user: 'Sam Taylor', text: 'merged branch `feature/auth-jwt` into `main`', time: '35 mins ago' },
    { type: 'build', user: 'CI/CD Pipeline', text: 'Build #1,401 succeeded (took 58s)', time: '1 hour ago' }
  ];

  const feedContainer = document.getElementById('activity-feed');
  feedItems.forEach(item => {
    const el = document.createElement('div');
    el.className = 'feed-item';
    el.innerHTML = `
      <div class="feed-badge ${item.type}">
        <i data-lucide="${item.type === 'commit' ? 'git-commit' : item.type === 'pr' ? 'git-pull-request' : 'check-circle-2'}"></i>
      </div>
      <div>
        <div class="feed-text"><strong>${item.user}</strong> ${item.text}</div>
        <div class="feed-time">${item.time}</div>
      </div>
    `;
    feedContainer.appendChild(el);
  });

  if (window.lucide) {
    lucide.createIcons();
  }
});
