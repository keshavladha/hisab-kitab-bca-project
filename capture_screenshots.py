import os
import time
from playwright.sync_api import sync_playwright

def capture():
    output_dir = r"C:\Users\kesha.000\.gemini\antigravity-ide\scratch\assets\images"
    os.makedirs(output_dir, exist_ok=True)

    print("Launching Playwright to capture live application screenshots...")

    with sync_playwright() as p:
        browser = p.chromium.launch(channel='msedge', headless=True)
        
        # Desktop Context
        context = browser.new_context(viewport={'width': 1440, 'height': 900})
        page = context.new_page()

        # 1. Landing Page
        page.goto('http://localhost:3001')
        page.evaluate("document.querySelector('.nav-item[data-view=\"landing\"]')?.click() || document.getElementById('nav-landing')?.click()")
        page.wait_for_timeout(1000)
        page.screenshot(path=os.path.join(output_dir, "fig_5_1_landing.png"))
        print("Captured Landing Page")

        # 2. Dashboard View
        page.evaluate("document.getElementById('nav-dashboard').click()")
        page.wait_for_timeout(1500)
        page.screenshot(path=os.path.join(output_dir, "fig_5_4_dashboard.png"))
        print("Captured Dashboard View")

        # 3. Login Modal
        page.evaluate("document.getElementById('btn-show-login').click(); document.getElementById('tab-login').click()")
        page.wait_for_timeout(800)
        page.screenshot(path=os.path.join(output_dir, "fig_5_2_login.png"))
        print("Captured Login Modal")

        # 4. Register Modal
        page.evaluate("document.getElementById('tab-register').click()")
        page.wait_for_timeout(800)
        page.screenshot(path=os.path.join(output_dir, "fig_5_3_register.png"))
        print("Captured Register Modal")

        # Close Modal
        page.evaluate("document.getElementById('close-auth-modal').click()")
        page.wait_for_timeout(500)

        # 5. Income Management Page
        page.evaluate("document.getElementById('nav-income').click()")
        page.wait_for_timeout(1000)
        page.screenshot(path=os.path.join(output_dir, "fig_5_5_income.png"))
        print("Captured Income Page")

        # 6. Expense Management Page
        page.evaluate("document.getElementById('nav-expense').click()")
        page.wait_for_timeout(1000)
        page.screenshot(path=os.path.join(output_dir, "fig_5_6_expense.png"))
        print("Captured Expense Page")

        # 7. Transaction History Page
        page.evaluate("document.getElementById('nav-transactions').click()")
        page.wait_for_timeout(1000)
        page.screenshot(path=os.path.join(output_dir, "fig_5_7_transactions.png"))
        print("Captured Transactions Page")

        # 8. Budget Planner Page
        page.evaluate("document.getElementById('nav-budget').click()")
        page.wait_for_timeout(1000)
        page.screenshot(path=os.path.join(output_dir, "fig_5_8_budget.png"))
        print("Captured Budget Planner Page")

        # 9. Reports & Charts Analytics Page
        page.evaluate("document.getElementById('nav-reports').click()")
        page.wait_for_timeout(2000) # Allow Chart.js animation
        page.screenshot(path=os.path.join(output_dir, "fig_5_9_reports.png"))
        print("Captured Reports & Charts Analytics Page")

        # 10. User Profile Page
        page.evaluate("document.getElementById('nav-profile').click()")
        page.wait_for_timeout(1000)
        page.screenshot(path=os.path.join(output_dir, "fig_5_10_profile.png"))
        print("Captured User Profile Page")

        # 11. Settings & Dark Mode Page
        page.evaluate("document.getElementById('nav-settings').click()")
        page.wait_for_timeout(1000)
        page.screenshot(path=os.path.join(output_dir, "fig_5_11_settings.png"))
        print("Captured Settings Page")

        # 12. Dark Mode UI Overview
        page.evaluate("document.getElementById('nav-dashboard').click()")
        page.wait_for_timeout(1000)
        page.screenshot(path=os.path.join(output_dir, "fig_5_12_darkmode.png"))
        print("Captured Dark Mode UI Overview")

        context.close()

        # 13. Mobile Viewport Context (375x812)
        mobile_context = browser.new_context(viewport={'width': 375, 'height': 812}, is_mobile=True)
        mobile_page = mobile_context.new_page()
        mobile_page.goto('http://localhost:3001')
        mobile_page.wait_for_timeout(1500)
        mobile_page.screenshot(path=os.path.join(output_dir, "fig_5_13_mobile.png"))
        print("Captured Mobile Responsive Viewport")
        mobile_context.close()

        browser.close()

    print("All live application screenshots successfully captured!")

if __name__ == '__main__':
    capture()
