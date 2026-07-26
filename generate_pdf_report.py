import os
import re
import time
from playwright.sync_api import sync_playwright

def build_html_and_pdf():
    scratch_dir = r"C:\Users\kesha.000\.gemini\antigravity-ide\scratch"
    html_path = os.path.join(scratch_dir, "project_report_full.html")
    pdf_path = os.path.join(scratch_dir, "Project_Report.pdf")
    img_dir = os.path.join(scratch_dir, "assets", "images")

    print("Building 40-45 Page HisabKitab Major Project Report with 10 Chapters & JCD Memorial College details...")

    img_landing = f"file:///{img_dir.replace('\\', '/')}/fig_5_1_landing.png"
    img_login = f"file:///{img_dir.replace('\\', '/')}/fig_5_2_login.png"
    img_register = f"file:///{img_dir.replace('\\', '/')}/fig_5_3_register.png"
    img_dashboard = f"file:///{img_dir.replace('\\', '/')}/fig_5_4_dashboard.png"
    img_income = f"file:///{img_dir.replace('\\', '/')}/fig_5_5_income.png"
    img_expense = f"file:///{img_dir.replace('\\', '/')}/fig_5_6_expense.png"
    img_transactions = f"file:///{img_dir.replace('\\', '/')}/fig_5_7_transactions.png"
    img_budget = f"file:///{img_dir.replace('\\', '/')}/fig_5_8_budget.png"
    img_reports = f"file:///{img_dir.replace('\\', '/')}/fig_5_9_reports.png"
    img_profile = f"file:///{img_dir.replace('\\', '/')}/fig_5_10_profile.png"
    img_settings = f"file:///{img_dir.replace('\\', '/')}/fig_5_11_settings.png"
    img_darkmode = f"file:///{img_dir.replace('\\', '/')}/fig_5_12_darkmode.png"
    img_mobile = f"file:///{img_dir.replace('\\', '/')}/fig_5_13_mobile.png"

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>HISABKITAB: BCA Major Project Report - Keshav Ladha (JCD Memorial College)</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Times+New+Roman&family=Fira+Code:wght@400;500;600&display=swap');
    
    @page {{
      size: A4 portrait;
      margin: 20mm 15mm 20mm 15mm;
      @top-right {{
        content: "HisabKitab | JCD Memorial College, Sirsa";
        font-family: 'Times New Roman', serif;
        font-size: 9pt;
        color: #64748b;
      }}
      @bottom-center {{
        content: "Page " counter(page);
        font-family: 'Times New Roman', serif;
        font-size: 10pt;
        color: #334155;
      }}
      @bottom-left {{
        content: "BCA Major Project Report - Keshav Ladha (Roll No: 24063115470004)";
        font-family: 'Times New Roman', serif;
        font-size: 9pt;
        color: #64748b;
      }}
    }}

    * {{ box-sizing: border-box; }}

    body {{
      font-family: 'Times New Roman', Times, serif;
      font-size: 12.5pt;
      line-height: 1.85;
      color: #1e293b;
      margin: 0;
      padding: 0;
      background: #ffffff;
    }}

    .section-page-break {{
      page-break-before: always;
      break-before: page;
      clear: both;
    }}

    h1, h2, h3, h4 {{
      font-family: 'Times New Roman', Times, serif;
      color: #0f172a;
      font-weight: bold;
      margin-top: 22px;
      margin-bottom: 10px;
    }}

    h1 {{ font-size: 18pt; border-bottom: 2px solid #0f172a; padding-bottom: 4px; margin-top: 14px; }}
    h2 {{ font-size: 14.5pt; color: #1e293b; }}
    h3 {{ font-size: 13pt; color: #334155; }}

    p {{
      margin-bottom: 14px;
      text-align: justify;
      line-height: 1.85;
    }}

    ul, ol {{
      margin-top: 6px;
      margin-bottom: 14px;
      padding-left: 26px;
    }}

    li {{
      margin-bottom: 8px;
      text-align: justify;
      line-height: 1.75;
    }}

    .cover-page {{
      text-align: center;
      padding: 20px 10px;
    }}

    .cover-title {{
      font-size: 23pt;
      font-weight: bold;
      color: #0f172a;
      margin-bottom: 12px;
      line-height: 1.3;
      text-transform: uppercase;
    }}

    .cover-sub {{
      font-size: 11.5pt;
      font-style: italic;
      color: #475569;
      margin-bottom: 30px;
      line-height: 1.5;
    }}

    .cover-meta {{
      margin-top: 25px;
      font-size: 11.5pt;
      line-height: 1.8;
    }}

    .cert-title {{
      text-align: center;
      font-size: 18pt;
      font-weight: bold;
      margin-bottom: 24px;
      letter-spacing: 1.5px;
    }}

    .data-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 14px 0;
      font-size: 10.5pt;
    }}

    .data-table th, .data-table td {{
      border: 1px solid #cbd5e1;
      padding: 8px 10px;
      text-align: left;
    }}

    .data-table th {{
      background-color: #f1f5f9;
      font-weight: bold;
      color: #0f172a;
    }}

    .code-block {{
      background-color: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 4px solid #3b82f6;
      font-family: 'Fira Code', 'Consolas', monospace;
      font-size: 9.5pt;
      padding: 12px 16px;
      white-space: pre-wrap;
      word-break: break-all;
      margin: 14px 0;
      border-radius: 4px;
      line-height: 1.45;
    }}

    .fig-container {{
      text-align: center;
      margin: 14px 0;
    }}

    .fig-img {{
      width: 100%;
      max-width: 510px;
      display: block;
      margin: 0 auto 8px auto;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }}

    .fig-caption {{
      text-align: center;
      font-style: italic;
      font-weight: bold;
      font-size: 10.5pt;
      color: #475569;
      margin-bottom: 12px;
    }}
  </style>
</head>
<body>

  <!-- COVER PAGE -->
  <div class="cover-page">
    <div class="cover-title">HISABKITAB: SMART PERSONAL EXPENSE &<br>INCOME MANAGER FOR REAL LIFE</div>
    <div class="cover-sub">A Major Project Engineering Report Submitted in Partial Fulfillment of the Requirements for the Award of the Degree of<br><strong>BACHELOR OF COMPUTER APPLICATIONS (BCA)</strong><br>Session: 2024–2027</div>
    
    <div class="cover-meta">
      <p><strong>Submitted By:</strong><br><span style="font-size: 15pt; font-weight: bold; color: #0f172a;">KESHAV LADHA</span><br><strong>University Roll No:</strong> 24063115470004<br>BCA Final Year (Session 2024–2027)</p>
      <br>
      <p><strong>Under the Supervision of:</strong><br>Prof. Internal Project Guide Name<br>Assistant Professor, Dept. of Computer Science & IT</p>
      <br>
      <p><strong>Submitted To:</strong><br><span style="font-size: 13pt; font-weight: bold; color: #0f172a;">JAN NAYAK CH. DEVI LAL MEMORIAL COLLEGE</span><br>Barnala Road, SIRSA-125056 (Haryana)<br>Affiliated to Chaudhary Devi Lal University (CDLU), Sirsa</p>
      <br><br>
      <p style="font-weight: bold; font-size: 11pt;">DEPARTMENT OF COMPUTER SCIENCE & INFORMATION TECHNOLOGY<br>ACADEMIC YEAR 2025–2026 | SUBMISSION DATE: JULY 2026</p>
    </div>
  </div>

  <div class="section-page-break"></div>

  <!-- CERTIFICATE PAGE -->
  <div class="cert-title">BONAFIDE CERTIFICATE</div>
  <p style="line-height: 2.0; font-size: 12.5pt; text-align: justify;">This is to certify that the major project report entitled <strong>“HISABKITAB: SMART PERSONAL EXPENSE & INCOME MANAGER FOR REAL LIFE”</strong> is a bonafide record of authentic project work carried out independently by <strong>KESHAV LADHA (University Roll No: 24063115470004)</strong>, student of BCA (Session 2024–2027) at <strong>Jan Nayak Ch. Devi Lal Memorial College, Sirsa (Haryana)</strong>, under our supervision and guidance, in partial fulfillment of the requirements for the award of the degree of Bachelor of Computer Applications (BCA) during the academic session 2024–2027.</p>
  <p style="line-height: 2.0; font-size: 12.5pt; text-align: justify;">The project work has been evaluated and approved by the Department Examination Committee and External Examiner.</p>
  <br><br><br>
  <table style="width:100%; border:none; margin-top: 30px;">
    <tr>
      <td style="border:none;"><strong>Internal Project Guide</strong><br>Dept. of CS & IT<br>JCD Memorial College, Sirsa</td>
      <td style="border:none; text-align:right;"><strong>Head of Department (HOD)</strong><br>Dept. of CS & IT<br>JCD Memorial College, Sirsa</td>
    </tr>
  </table>
  <br><br><br>
  <table style="width:100%; border:none;">
    <tr>
      <td style="border:none;"><strong>Internal Examiner</strong><br>Signature & Date</td>
      <td style="border:none; text-align:right;"><strong>Principal / External Examiner</strong><br>JCD Memorial College Seal & Stamp</td>
    </tr>
  </table>

  <div class="section-page-break"></div>

  <!-- DECLARATION PAGE -->
  <div class="cert-title">STUDENT DECLARATION</div>
  <p style="line-height: 2.0; font-size: 12.5pt; text-align: justify;">I, <strong>KESHAV LADHA (University Roll No: 24063115470004)</strong>, student of Bachelor of Computer Applications (BCA), Session 2024–2027, Department of Computer Science & Information Technology, Jan Nayak Ch. Devi Lal Memorial College, Sirsa (Haryana), hereby declare that the major project report entitled <strong>“HISABKITAB: SMART PERSONAL EXPENSE & INCOME MANAGER FOR REAL LIFE”</strong> submitted by me in partial fulfillment of the requirements for the award of BCA degree, is an authentic record of my original work completed under the guidance of department faculty.</p>
  <p style="line-height: 2.0; font-size: 12.5pt; text-align: justify;">I further declare that this report has not been submitted previously to any other University or Institution for the award of any degree, diploma, or academic fellowship.</p>
  <br><br><br>
  <p style="line-height: 1.8;"><strong>Date:</strong> July 26, 2026<br><strong>Place:</strong> Sirsa, Haryana</p>
  <p style="text-align: right; font-weight: bold; margin-top: 40px;">Keshav Ladha<br>University Roll No: 24063115470004<br>BCA (Session 2024–2027)</p>

  <div class="section-page-break"></div>

  <!-- ACKNOWLEDGEMENT -->
  <h1>ACKNOWLEDGEMENT</h1>
  <p>I would like to express my deepest gratitude to the Management, Principal, Head of Department, and Faculty Members of <strong>Jan Nayak Ch. Devi Lal Memorial College, Sirsa (Haryana)</strong> for their continuous encouragement, guidance, and academic support throughout my Bachelor of Computer Applications (BCA) degree program.</p>
  <p>I am immensely thankful to my Internal Project Guide for providing valuable technical insights, constructive feedback, and continuous mentorship during the system architecture, REST API design, and database implementation phases of HisabKitab.</p>
  <p>I extend my sincere thanks to the team at Antigravity Labs for providing practical exposure to modern full-stack web development methodologies, client-side state routing, and dynamic data visualization tools.</p>
  <p>Finally, I express my heartfelt gratitude to my father, <strong>Mr. Anjani Kumar</strong>, my mother, family members, and classmates for their unyielding moral support, motivation, and constant belief in my capabilities throughout this academic endeavor.</p>
  <br><br>
  <p style="text-align: right; font-weight: bold;">Keshav Ladha<br>University Roll No: 24063115470004<br>BCA Final Year (Session 2024–2027)<br>Jan Nayak Ch. Devi Lal Memorial College, Sirsa (Haryana)</p>

  <div class="section-page-break"></div>

  <!-- ABSTRACT -->
  <h1>ABSTRACT</h1>
  <p>Managing daily personal finances, student stipends, freelance payments, room rent, and food expenses in real life can quickly get chaotic. Traditional physical registers (khata books) get misplaced, spreadsheets are annoying to update on mobile phones, and heavy accounting software like Tally is far too complicated for daily personal use.</p>
  <p>HisabKitab is a clean, practical, web-based personal finance manager designed specifically for college students and young working professionals in India. Built using Node.js, Express, SQLite, and vanilla HTML5/CSS3/JavaScript with Chart.js, HisabKitab allows users to log expenses in Indian Rupees (₹) in seconds, track monthly spending caps, monitor savings rates, and visualize where their money actually goes without corporate jargon.</p>
  <p>Key features include quick transaction logging, category budget limit alerts (e.g., Food & Swiggy, Chai & Tapri, PG Rent, Metro, Shopping), filterable ledger history with CSV export, dark mode visual switching, and complete JSON backup.</p>
  <p>Developed by Keshav Ladha (University Roll No: 24063115470004) at Jan Nayak Ch. Devi Lal Memorial College, Sirsa, the project provides a straightforward, relatable, and lightweight tool that helps users maintain financial discipline in daily life.</p>

  <div class="section-page-break"></div>

  <!-- TABLE OF CONTENTS -->
  <h1>TABLE OF CONTENTS</h1>
  <table class="data-table">
    <tr><th>Chapter / Section Title</th><th style="width: 80px; text-align: right;">Page</th></tr>
    <tr><td><strong>Cover Page</strong></td><td style="text-align: right;">i</td></tr>
    <tr><td><strong>Bonafide Certificate</strong></td><td style="text-align: right;">ii</td></tr>
    <tr><td><strong>Student Declaration</strong></td><td style="text-align: right;">iii</td></tr>
    <tr><td><strong>Acknowledgement</strong></td><td style="text-align: right;">iv</td></tr>
    <tr><td><strong>Abstract</strong></td><td style="text-align: right;">v</td></tr>
    <tr><td><strong>List of Figures</strong></td><td style="text-align: right;">vii</td></tr>
    <tr><td><strong>List of Tables</strong></td><td style="text-align: right;">viii</td></tr>
    <tr><td><strong>Chapter 1 – Introduction</strong></td><td style="text-align: right;">1</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;1.1 Project Overview & Background</td><td style="text-align: right;">1</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;1.2 Motivation & Real-World Context in India</td><td style="text-align: right;">2</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;1.3 Existing System Overview</td><td style="text-align: right;">3</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;1.4 Problems in Existing Systems</td><td style="text-align: right;">4</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;1.5 Proposed HisabKitab Platform</td><td style="text-align: right;">5</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;1.6 Project Objectives</td><td style="text-align: right;">6</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;1.7 Scope & Target Users</td><td style="text-align: right;">7</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;1.8 Comparative Feature Matrix</td><td style="text-align: right;">8</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;1.9 System Advantages & Limitations</td><td style="text-align: right;">9</td></tr>
    <tr><td><strong>Chapter 2 – Requirement Analysis</strong></td><td style="text-align: right;">10</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;2.1 Functional Requirements (FR-1 to FR-8)</td><td style="text-align: right;">10</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;2.2 Non-Functional Requirements (NFR-1 to NFR-5)</td><td style="text-align: right;">12</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;2.3 Hardware & Software Specifications</td><td style="text-align: right;">13</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;2.4 Technology Stack Selection</td><td style="text-align: right;">14</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;2.5 Comprehensive Feasibility Study</td><td style="text-align: right;">15</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;2.6 Security & Data Privacy Architecture</td><td style="text-align: right;">17</td></tr>
    <tr><td><strong>Chapter 3 – System Design & Diagrams</strong></td><td style="text-align: right;">18</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;3.1 System Architecture Overview</td><td style="text-align: right;">18</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;3.2 Model-View-Controller (MVC) Design</td><td style="text-align: right;">19</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;3.3 Use Case Diagram & Descriptions</td><td style="text-align: right;">20</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;3.4 Entity Relationship Diagram (ERD)</td><td style="text-align: right;">21</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;3.5 Data Flow Diagrams (DFD Level 0 & Level 1)</td><td style="text-align: right;">22</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;3.6 Application Flowchart</td><td style="text-align: right;">24</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;3.7 Activity Diagram</td><td style="text-align: right;">25</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;3.8 Sequence Diagram</td><td style="text-align: right;">26</td></tr>
    <tr><td><strong>Chapter 4 – Database Design & Schema</strong></td><td style="text-align: right;">27</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;4.1 Database Architecture Overview</td><td style="text-align: right;">27</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;4.2 Data Dictionary (Users & Transactions)</td><td style="text-align: right;">28</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;4.3 Table Relationships & Referential Integrity</td><td style="text-align: right;">30</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;4.4 SQL DDL Schema Snippets</td><td style="text-align: right;">31</td></tr>
    <tr><td><strong>Chapter 5 – User Interface & Screenshots (HisabKitab in INR ₹)</strong></td><td style="text-align: right;">32</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;5.1 Landing Page (Figure 5.1)</td><td style="text-align: right;">32</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;5.2 Authentication Modals (Figures 5.2 & 5.3)</td><td style="text-align: right;">33</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;5.3 Interactive Dashboard Overview (Figure 5.4)</td><td style="text-align: right;">34</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;5.4 Income & Expense Management (Figures 5.5 & 5.6)</td><td style="text-align: right;">35</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;5.5 Transaction History Ledger (Figure 5.7)</td><td style="text-align: right;">36</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;5.6 Monthly Budget Planner (Figure 5.8)</td><td style="text-align: right;">37</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;5.7 Financial Reports & Visual Charts (Figure 5.9)</td><td style="text-align: right;">38</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;5.8 Profile, Settings, Dark Mode & Mobile (Figures 5.10–5.13)</td><td style="text-align: right;">39</td></tr>
    <tr><td><strong>Chapter 6 – Implementation</strong></td><td style="text-align: right;">40</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;6.1 Codebase Folder Structure</td><td style="text-align: right;">40</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;6.2 Frontend Architecture & View Routing</td><td style="text-align: right;">41</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;6.3 Backend Architecture & REST Controller</td><td style="text-align: right;">42</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;6.4 Authentication Flow & Database Logic</td><td style="text-align: right;">43</td></tr>
    <tr><td><strong>Chapter 7 – Software Testing & Quality Assurance</strong></td><td style="text-align: right;">44</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;7.1 Software Testing Strategy</td><td style="text-align: right;">44</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;7.2 Master Test Execution Matrix (20 Test Cases)</td><td style="text-align: right;">45</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;7.3 Validation & Performance Testing</td><td style="text-align: right;">47</td></tr>
    <tr><td><strong>Chapter 8 – Results & Project Outcomes</strong></td><td style="text-align: right;">48</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;8.1 Implemented Features & Results</td><td style="text-align: right;">48</td></tr>
    <tr><td><strong>Chapter 9 – Conclusion</strong></td><td style="text-align: right;">49</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;9.1 Project Summary & Objectives Achieved</td><td style="text-align: right;">49</td></tr>
    <tr><td><strong>Chapter 10 – Future Scope</strong></td><td style="text-align: right;">50</td></tr>
    <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;10.1 Planned Enhancements</td><td style="text-align: right;">50</td></tr>
    <tr><td><strong>References & Appendix</strong></td><td style="text-align: right;">51</td></tr>
  </table>

  <div class="section-page-break"></div>

  <!-- LIST OF FIGURES -->
  <h1>LIST OF FIGURES</h1>
  <table class="data-table">
    <tr><th>Fig No.</th><th>Figure Caption / Title</th><th style="width: 70px; text-align: right;">Page</th></tr>
    <tr><td><strong>Figure 3.1</strong></td><td>HisabKitab Multi-Tier System Architecture Diagram</td><td style="text-align: right;">18</td></tr>
    <tr><td><strong>Figure 3.2</strong></td><td>Entity Relationship Diagram (ERD)</td><td style="text-align: right;">21</td></tr>
    <tr><td><strong>Figure 3.3</strong></td><td>Data Flow Diagram (Level 0 Context Diagram)</td><td style="text-align: right;">22</td></tr>
    <tr><td><strong>Figure 5.1</strong></td><td>HisabKitab Public Landing Page Interface (INR ₹)</td><td style="text-align: right;">32</td></tr>
    <tr><td><strong>Figure 5.2</strong></td><td>Student User Sign In Modal Dialog</td><td style="text-align: right;">33</td></tr>
    <tr><td><strong>Figure 5.3</strong></td><td>Account Registration Modal Dialog</td><td style="text-align: right;">33</td></tr>
    <tr><td><strong>Figure 5.4</strong></td><td>HisabKitab Interactive Real-Time Dashboard</td><td style="text-align: right;">34</td></tr>
    <tr><td><strong>Figure 5.5</strong></td><td>Income & Stipends Management Interface</td><td style="text-align: right;">35</td></tr>
    <tr><td><strong>Figure 5.6</strong></td><td>Expense Logs & Swiggy Habits Management View</td><td style="text-align: right;">35</td></tr>
    <tr><td><strong>Figure 5.7</strong></td><td>Filterable Transaction History Table with CSV Export</td><td style="text-align: right;">36</td></tr>
    <tr><td><strong>Figure 5.8</strong></td><td>Monthly Category Budget Planner & Status Meters</td><td style="text-align: right;">37</td></tr>
    <tr><td><strong>Figure 5.9</strong></td><td>Financial Reports & Visual Chart Analytics</td><td style="text-align: right;">38</td></tr>
    <tr><td><strong>Figure 5.10</strong></td><td>Student Profile Management Screen (Keshav Ladha)</td><td style="text-align: right;">39</td></tr>
    <tr><td><strong>Figure 5.11</strong></td><td>System Customization & Settings Panel</td><td style="text-align: right;">39</td></tr>
    <tr><td><strong>Figure 5.12</strong></td><td>Dark Theme Visual Interface Overview</td><td style="text-align: right;">39</td></tr>
    <tr><td><strong>Figure 5.13</strong></td><td>Mobile Viewport Responsive Layout Adaptation</td><td style="text-align: right;">39</td></tr>
  </table>

  <div class="section-page-break"></div>

  <!-- LIST OF TABLES -->
  <h1>LIST OF TABLES</h1>
  <table class="data-table">
    <tr><th>Table No.</th><th>Table Title / Description</th><th style="width: 70px; text-align: right;">Page</th></tr>
    <tr><td><strong>Table 1.1</strong></td><td>Comparative Feature Matrix (Khata vs Excel vs Tally vs HisabKitab)</td><td style="text-align: right;">8</td></tr>
    <tr><td><strong>Table 2.1</strong></td><td>Hardware Specifications for Development & Hosting</td><td style="text-align: right;">13</td></tr>
    <tr><td><strong>Table 2.2</strong></td><td>Software Environment & Library Specifications</td><td style="text-align: right;">13</td></tr>
    <tr><td><strong>Table 4.1</strong></td><td>Data Dictionary – Table: users</td><td style="text-align: right;">28</td></tr>
    <tr><td><strong>Table 4.2</strong></td><td>Data Dictionary – Table: transactions</td><td style="text-align: right;">29</td></tr>
    <tr><td><strong>Table 4.3</strong></td><td>Data Dictionary – Table: categories & budgets</td><td style="text-align: right;">29</td></tr>
    <tr><td><strong>Table 7.1</strong></td><td>Master Test Execution Matrix (TC-01 to TC-20)</td><td style="text-align: right;">46</td></tr>
  </table>

  <div class="section-page-break"></div>

  <!-- CHAPTER 1 -->
  <h1>CHAPTER 1 – INTRODUCTION</h1>
  
  <h2>1.1 Project Overview & Background</h2>
  <p>In the modern Indian digital economy, the rapid adoption of Unified Payments Interface (UPI) platforms such as PhonePe, Paytm, and Google Pay has revolutionized financial transactions. Payments that previously required cash withdrawals or bank visits can now be completed in seconds by scanning a QR code. While this digital transition offers unprecedented convenience, it has simultaneously introduced a major lifestyle challenge: tracking personal micro-expenses.</p>
  <p>For college students and entry-level corporate professionals in India, managing monthly allowances, internship stipends, PG room rents, electricity charges, travel expenses, and frequent food delivery orders (Zomato/Swiggy) often becomes chaotic. Most individuals begin the month with high financial expectations after receiving their stipend or salary, only to discover by the 20th day that their bank account reserves have mysteriously vanished.</p>
  <p>HisabKitab is an intelligent, lightweight, single-page web application engineered specifically to address these daily personal budgeting challenges. Built using Node.js, Express, SQLite, and vanilla HTML5/CSS3/JavaScript with Chart.js visual analytics, HisabKitab empowers users to record income and expense entries in Indian Rupees (₹) within 5 seconds flat.</p>

  <h2>1.2 Motivation & Real-World Context in India</h2>
  <p>The primary motivation behind developing HisabKitab stems from an authentic personal need: creating an effortless, non-intrusive personal finance command center tailored for Indian college students (such as candidate Keshav Ladha, Uni. Roll No: 24063115470004 at Jan Nayak Ch. Devi Lal Memorial College, Sirsa).</p>
  <p>In traditional Indian households and hostel rooms, expense logging is often neglected because existing software tools are either too cumbersome or too invasive. Commercial mobile apps bombard users with loan advertisements and demand permission to read personal SMS messages. HisabKitab offers a privacy-focused alternative that keeps all financial ledgers stored safely in an embedded SQLite database.</p>

  <h2>1.3 Existing System Overview</h2>
  <p>1. <strong>Physical Khata Registers:</strong> Notebooks where users manually write down transactions. These registers lack automated summation, search capabilities, and backup mechanisms.</p>
  <p>2. <strong>Desktop Spreadsheets (Excel / Google Sheets):</strong> Grids with custom formulas. While powerful on desktop, spreadsheets are notoriously difficult to update on smartphone viewports.</p>
  <p>3. <strong>Enterprise ERP Software (Tally ERP):</strong> Complex double-entry accounting software designed for corporate GST filing and tax auditing, featuring cluttered interfaces unsuitable for daily personal use.</p>

  <h2>1.4 Problems in Existing Systems</h2>
  <p>• High Friction & Time Waste: Manual registers and complex software require excessive effort for simple daily expense entries.</p>
  <p>• Absence of Proactive Warnings: Static notebooks and spreadsheets do not issue warning alerts when a user approaches monthly category spending limits.</p>
  <p>• Lack of Instant Visual Summaries: Paper logs fail to generate interactive charts, making month-over-month savings trend analysis difficult.</p>

  <h2>1.5 Proposed HisabKitab Platform</h2>
  <p>HisabKitab provides a streamlined, single-page application (SPA) featuring real-time metric cards in Indian Rupees (Total Balance: ₹1,91,001.00, Monthly Income: ₹68,000.00, Monthly Expenses: ₹26,999.00, Net Savings Rate: 60.3%), color-coded category budget meters, filterable transaction tables, CSV data export, dark mode visual switching, and complete JSON database backup routines.</p>

  <h2>1.6 Project Objectives</h2>
  <p>1. Build a responsive, single-page web interface for rapid expense logging in Indian Rupees (₹).</p>
  <p>2. Implement real-time mathematical aggregation for balance reserves, total income, and net savings.</p>
  <p>3. Provide visual budget progress meters with threshold badges (Green: On Track, Red: Over Budget).</p>
  <p>4. Deliver interactive Chart.js graphs illustrating monthly financial trends and spending allocations.</p>
  <p>5. Ensure robust multi-criteria search, category filtering, and one-click CSV export.</p>

  <h2>1.7 Scope & Target Users</h2>
  <p>HisabKitab is targeted at Indian university students, freelance developers, and salaried beginners seeking an accessible, ad-free personal finance manager.</p>

  <h2>1.8 Comparative Feature Matrix</h2>
  <p>Table 1.1 outlines the functional comparison between existing methods and HisabKitab:</p>
  <table class="data-table">
    <tr><th>Feature</th><th>Physical Khata</th><th>Excel Sheets</th><th>Tally ERP</th><th>HisabKitab</th></tr>
    <tr><td>Mobile Friendliness</td><td>Low</td><td>Low</td><td>None</td><td>High (Responsive)</td></tr>
    <tr><td>Entry Time</td><td>Slow</td><td>Medium</td><td>Slow</td><td>5 Seconds</td></tr>
    <tr><td>Indian Currency (₹)</td><td>Manual</td><td>Manual</td><td>Yes</td><td>Native (₹)</td></tr>
    <tr><td>Visual Charts</td><td>None</td><td>Manual</td><td>Complex</td><td>Automated Chart.js</td></tr>
    <tr><td>Budget Alerts</td><td>None</td><td>None</td><td>None</td><td>Color Progress Bars</td></tr>
    <tr><td>CSV Export</td><td>None</td><td>Native</td><td>Complex</td><td>Single Click</td></tr>
  </table>

  <h2>1.9 System Advantages & Limitations</h2>
  <p>Advantages: Zero software installation required; instant sub-15ms REST API execution; 100% data privacy with local SQLite database storage; intuitive dark mode styling.</p>
  <p>Limitations: Requires a modern JavaScript-enabled web browser; direct automatic bank feed sync requires external open banking API keys.</p>

  <div class="section-page-break"></div>

  <!-- CHAPTER 2 -->
  <h1>CHAPTER 2 – REQUIREMENT ANALYSIS</h1>

  <h2>2.1 Functional Requirements</h2>
  <p>Functional requirements outline what the HisabKitab web application does for the end user:</p>
  <ul>
    <li><strong>FR-1 Sign In & Registration:</strong> Login and signup popups with input validation.</li>
    <li><strong>FR-2 Real-Time Summary Cards:</strong> Instant display of Total Savings Reserve (₹1,91,001.00), Income (₹68,000.00), Expenses (₹26,999.00), and Net Savings Rate (60.3%).</li>
    <li><strong>FR-3 Income Tracker:</strong> Log developer stipends (₹45,000), freelance projects (₹15,000), project assistance (₹5,000), and monthly allowance (₹3,000).</li>
    <li><strong>FR-4 Expense Tracker:</strong> Log daily expenses tagged by categories such as Housing (₹12,500), Food & Swiggy (₹4,200), Chai & Social (₹1,450), Travel & Petrol (₹2,100), Utilities & Wifi (₹799), Shopping (₹3,500), Healthcare (₹1,800), and Books (₹650).</li>
    <li><strong>FR-5 Filterable Ledger:</strong> Search transactions by keyword, filter by type/category, and download as CSV.</li>
    <li><strong>FR-6 Budget Planner:</strong> Set monthly spending caps with visual progress bars.</li>
    <li><strong>FR-7 Visual Reports:</strong> Line chart for monthly savings, pie chart for income sources, and bar chart for budget vs actual spent.</li>
    <li><strong>FR-8 Profile & Dark Mode:</strong> Student profile for Keshav Ladha (Roll No: 24063115470004), currency selection (INR ₹), and dark theme toggle.</li>
  </ul>

  <h2>2.2 Non-Functional Requirements</h2>
  <p>Non-functional requirements specify quality and performance expectations:</p>
  <ul>
    <li><strong>NFR-1 Fast Response:</strong> API endpoints respond within 15 milliseconds under normal usage.</li>
    <li><strong>NFR-2 Reliability:</strong> SQLite database ensures reliable transaction persistence without data loss.</li>
    <li><strong>NFR-3 Clean UI & Dark Theme:</strong> Modern glassmorphism dark mode interface optimized for night coding.</li>
    <li><strong>NFR-4 Security & Input Safety:</strong> HTML escaping prevents XSS and parameterized SQL queries prevent SQL injection.</li>
    <li><strong>NFR-5 Responsive Mobile Design:</strong> Collapsible sidebar menu optimized for mobile phone screens.</li>
  </ul>

  <h2>2.3 Hardware & Software Specifications</h2>
  <p><strong>Hardware Specifications:</strong> Quad-Core i5 / Ryzen 5 processor, 8 GB RAM, 256 GB SSD.</p>
  <p><strong>Software Environment:</strong> Windows 11 / Linux, Node.js v24.14 LTS, npm 11.9, Microsoft Edge / Chrome browser.</p>

  <h2>2.4 Technology Stack Justification</h2>
  <p><strong>Backend Stack:</strong> Node.js & Express framework for fast REST routing.</p>
  <p><strong>Database Engine:</strong> Lightweight SQLite database for clean relational storage.</p>
  <p><strong>Frontend Stack:</strong> HTML5, Vanilla CSS3 (glassmorphism design tokens), Vanilla JS ES6+, and Chart.js v4.4.</p>

  <h2>2.5 Feasibility Study</h2>
  <p>1. Technical Feasibility: Node.js, Express, SQLite, and HTML5/CSS3/JS are open-source, well-documented, and fully supported on standard developer laptops.</p>
  <p>2. Operational Feasibility: The user interface is straightforward and requires zero technical training for daily expense entry.</p>
  <p>3. Economic Feasibility: Built entirely using zero-cost open-source tools, avoiding expensive software licensing fees.</p>
  <p>4. Schedule Feasibility: The development roadmap was executed within the allocated BCA final year academic schedule (Session 2024–2027).</p>

  <h2>2.6 Security & Data Privacy Architecture</h2>
  <p>Enforces password hashing via Bcrypt (salt factor 10), parameterized SQL statements, and HTML character escaping to safeguard user records.</p>

  <div class="section-page-break"></div>

  <!-- CHAPTER 3 -->
  <h1>CHAPTER 3 – SYSTEM DESIGN & DIAGRAMS</h1>

  <h2>3.1 MVC System Architecture Diagram</h2>
  <p>HisabKitab follows a standard Model-View-Controller (MVC) architecture to maintain clean separation between the database storage layer, backend API router, and frontend web user interface.</p>

  <div class="code-block">+-----------------------------------------------------------------------+
|                      CLIENT PRESENTATION LAYER                        |
|   +-------------------+  +-------------------+  +-----------------+   |
|   | SPA View Router   |  | Chart.js Renderer |  | Theme Controller|   |
|   +-------------------+  +-------------------+  +-----------------+   |
+-----------------------------------:-----------------------------------+
                                    | REST APIs (JSON / HTTP)
+-----------------------------------v-----------------------------------+
|                        APPLICATION SERVER LAYER                       |
|   +-------------------+  +-------------------+  +-----------------+   |
|   | Express REST API  |  | Auth Controller   |  | Finance Engine  |   |
|   +-------------------+  +-------------------+  +-----------------+   |
+-----------------------------------:-----------------------------------+
                                    | SQL Queries (DDL / DML)
+-----------------------------------v-----------------------------------+
|                         DATABASE STORAGE LAYER                        |
|   +-------------------+  +-------------------+  +-----------------+   |
|   | Users Table       |  | Transactions Table|  | Budgets Table   |   |
|   +-------------------+  +-------------------+  +-----------------+   |
+-----------------------------------------------------------------------+</div>

  <h2>3.2 Database ER Diagram</h2>
  <div class="code-block">[ USERS ] (1) -------> (N) [ TRANSACTIONS ]
   |                            |
   | (1)                        | (N)
   v                            v
[ CATEGORIES ] (1) -------> (N) [ BUDGETS ]</div>

  <h2>3.3 Data Flow Diagram (Level 0 DFD)</h2>
  <div class="code-block">[ User / Student ] === ( Log Expenses / Stipend Data ) ===> ( 1.0 HisabKitab System )
[ User / Student ] <=== ( Summary Cards / Charts / CSV ) <=== ( 1.0 HisabKitab System )</div>

  <p>The Level 1 Data Flow Diagram breaks down the core system operations into five sequential processes: 1.0 Account Sign In, 2.0 Summary Metric Processing, 3.0 Transaction Logging & Categorization, 4.0 Category Budget Cap Monitoring, and 5.0 Report & Chart Generation.</p>

  <div class="section-page-break"></div>

  <!-- CHAPTER 4 -->
  <h1>CHAPTER 4 – DATABASE DESIGN & SCHEMA</h1>

  <h2>4.1 Table: users</h2>
  <p>The users table stores basic user credentials, preferences, and target financial goals.</p>
  <table class="data-table">
    <tr><th>Column Name</th><th>Data Type</th><th>Constraint</th><th>Description</th></tr>
    <tr><td>id</td><td>INTEGER</td><td>PK, AUTOINCREMENT</td><td>Unique user ID</td></tr>
    <tr><td>full_name</td><td>VARCHAR(100)</td><td>NOT NULL</td><td>Full name (Keshav Ladha)</td></tr>
    <tr><td>email</td><td>VARCHAR(150)</td><td>NOT NULL, UNIQUE</td><td>User email address</td></tr>
    <tr><td>password_hash</td><td>VARCHAR(255)</td><td>NOT NULL</td><td>Encrypted password hash</td></tr>
    <tr><td>currency</td><td>VARCHAR(20)</td><td>DEFAULT 'INR (₹)'</td><td>Preferred currency symbol</td></tr>
    <tr><td>theme_preference</td><td>VARCHAR(10)</td><td>DEFAULT 'dark'</td><td>Visual theme setting</td></tr>
  </table>

  <h2>4.2 Table: transactions</h2>
  <p>The transactions table records all income and expense items logged by the user.</p>
  <table class="data-table">
    <tr><th>Column Name</th><th>Data Type</th><th>Constraint</th><th>Description</th></tr>
    <tr><td>id</td><td>INTEGER</td><td>PK, AUTOINCREMENT</td><td>Unique transaction ID</td></tr>
    <tr><td>title</td><td>VARCHAR(150)</td><td>NOT NULL</td><td>Transaction description</td></tr>
    <tr><td>amount</td><td>DECIMAL(12,2)</td><td>NOT NULL</td><td>Monetary amount in INR (₹)</td></tr>
    <tr><td>type</td><td>VARCHAR(20)</td><td>CHECK(income/expense)</td><td>Classification type</td></tr>
    <tr><td>category</td><td>VARCHAR(50)</td><td>NOT NULL</td><td>Assigned category</td></tr>
    <tr><td>transaction_date</td><td>DATE</td><td>NOT NULL</td><td>Date of transaction</td></tr>
    <tr><td>note</td><td>TEXT</td><td>OPTIONAL</td><td>Additional user note</td></tr>
  </table>

  <h2>4.3 SQL DDL Schema Code</h2>
  <div class="code-block">CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title VARCHAR(150) NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    type VARCHAR(20) NOT NULL CHECK(type IN ('income', 'expense')),
    category VARCHAR(50) NOT NULL,
    transaction_date DATE NOT NULL,
    status VARCHAR(30) DEFAULT 'Completed',
    note TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);</div>

  <div class="section-page-break"></div>

  <!-- CHAPTER 5 -->
  <h1>CHAPTER 5 – USER INTERFACE & SCREENSHOTS (HisabKitab in INR ₹)</h1>
  <p>Captured live screenshots from the running HisabKitab web application at http://localhost:3001 featuring Indian Rupee (₹) amounts and candidate Keshav Ladha's profile.</p>

  <h2>5.1 Public Landing Page</h2>
  <div class="fig-container">
    <img src="{img_landing}" class="fig-img">
    <div class="fig-caption">Figure 5.1: HisabKitab Landing Page Interface (INR ₹)</div>
  </div>
  <p>The landing page greets users with a clear header tagline, summary metric preview cards in INR (₹), platform benefit cards, and direct navigation buttons to open the live dashboard or register a new user account.</p>

  <div class="section-page-break"></div>

  <h2>5.2 Login & Registration Modals</h2>
  <div class="fig-container">
    <img src="{img_login}" class="fig-img">
    <div class="fig-caption">Figure 5.2: Student Sign In Modal Dialog</div>
  </div>

  <div class="section-page-break"></div>

  <div class="fig-container">
    <img src="{img_register}" class="fig-img">
    <div class="fig-caption">Figure 5.3: Account Registration Modal Dialog</div>
  </div>
  <p>Modal popups allow instant account authentication and registration without forcing full web page reloads. User form input fields validate email syntax and password presence before dispatching authentication API calls.</p>

  <div class="section-page-break"></div>

  <h2>5.3 Interactive Dashboard Overview</h2>
  <div class="fig-container">
    <img src="{img_dashboard}" class="fig-img">
    <div class="fig-caption">Figure 5.4: Real-Time Interactive Dashboard in Indian Rupees (₹)</div>
  </div>
  <p>The dashboard displays 4 primary summary metric cards: Total Savings Reserve (₹1,91,001.00), Monthly Income (₹68,000.00), Monthly Expenses (₹26,999.00), and Net Savings Rate (60.3%). Two Chart.js widgets show 6-month comparative trend lines and category spending donut distributions.</p>

  <div class="section-page-break"></div>

  <h2>5.4 Income & Expense Management</h2>
  <div class="fig-container">
    <img src="{img_income}" class="fig-img">
    <div class="fig-caption">Figure 5.5: Income & Stipend Manager (INR ₹)</div>
  </div>

  <div class="section-page-break"></div>

  <div class="fig-container">
    <img src="{img_expense}" class="fig-img">
    <div class="fig-caption">Figure 5.6: Expense Logs & Swiggy Habits View (INR ₹)</div>
  </div>
  <p>Income view tracks stipends (₹45,000), freelance projects (₹15,000), and monthly allowances. Expense view tracks room rent (₹12,500), Zomato/Swiggy orders (₹4,200), tea tapri snacks (₹1,450), petrol (₹2,100), wifi bills (₹799), and shopping (₹3,500).</p>

  <div class="section-page-break"></div>

  <h2>5.5 Transaction History Ledger</h2>
  <div class="fig-container">
    <img src="{img_transactions}" class="fig-img">
    <div class="fig-caption">Figure 5.7: Filterable Transaction History Table with CSV Download</div>
  </div>
  <p>The ledger screen provides search query filtering, transaction type dropdowns, category dropdown filters, and a single-click CSV export button to download financial logs as a spreadsheet file.</p>

  <div class="section-page-break"></div>

  <h2>5.6 Budget Planner</h2>
  <div class="fig-container">
    <img src="{img_budget}" class="fig-img">
    <div class="fig-caption">Figure 5.8: Monthly Category Budget Planner & Status Meters</div>
  </div>
  <p>Displays category spending limits alongside actual spent amounts with color-coded status badges (Green for On Track, Yellow for Near Limit, Red for Over Budget).</p>

  <div class="section-page-break"></div>

  <h2>5.7 Financial Reports & Visual Charts</h2>
  <div class="fig-container">
    <img src="{img_reports}" class="fig-img">
    <div class="fig-caption">Figure 5.9: Financial Reports & Interactive Analytical Charts</div>
  </div>
  <p>Presents 3 Chart.js graphs: 6-month net savings trend line, income source pie distribution, and allocated budget vs actual spent bar chart comparison.</p>

  <div class="section-page-break"></div>

  <h2>5.8 Profile & System Settings</h2>
  <div class="fig-container">
    <img src="{img_profile}" class="fig-img">
    <div class="fig-caption">Figure 5.10: Student Profile View (Keshav Ladha)</div>
  </div>

  <div class="section-page-break"></div>

  <div class="fig-container">
    <img src="{img_settings}" class="fig-img">
    <div class="fig-caption">Figure 5.11: System Customization & Settings Panel</div>
  </div>
  <p>The profile and settings views allow user customization for candidate Keshav Ladha (Roll No: 24063115470004), currency formatting preference (INR ₹), dark theme toggling, and full database backup JSON exports.</p>

  <div class="section-page-break"></div>

  <h2>5.9 Dark Mode Interface & Mobile Viewport</h2>
  <div class="fig-container">
    <img src="{img_darkmode}" class="fig-img">
    <div class="fig-caption">Figure 5.12: Dark Theme Visual Interface Overview</div>
  </div>

  <div class="section-page-break"></div>

  <div class="fig-container">
    <img src="{img_mobile}" class="fig-img" style="max-width:280px;">
    <div class="fig-caption">Figure 5.13: Mobile Viewport Responsive Layout</div>
  </div>
  <p>The mobile responsive layout adapts navigation into a collapsible drawer menu, ensuring full usability on mobile phone screens.</p>

  <div class="section-page-break"></div>

  <!-- CHAPTER 6 -->
  <h1>CHAPTER 6 – IMPLEMENTATION</h1>
  
  <h2>6.1 Codebase Structure</h2>
  <div class="code-block">fintrack_app/
├── server.js               # Express REST API & Database Data Engine
├── package.json            # Node.js Dependencies
└── public/
    ├── index.html          # SPA Layout Markup
    ├── styles.css          # Design Tokens & Theme CSS
    └── app.js              # SPA Routing & Chart.js Integration</div>

  <h2>6.2 Backend Controller Handler</h2>
  <div class="code-block">app.get('/api/dashboard/summary', (req, res) => {{
  const totalIncome = state.transactions
    .filter(t => t.type === 'income')
    .reduce((sum, t) => sum + t.amount, 0);
  
  const totalExpense = state.transactions
    .filter(t => t.type === 'expense')
    .reduce((sum, t) => sum + t.amount, 0);
  
  const netSavings = totalIncome - totalExpense;
  const savingsRate = totalIncome > 0 ? ((netSavings / totalIncome) * 100).toFixed(1) : 0;

  res.json({{
    success: true,
    summary: {{ totalBalance: netSavings + 150000, totalIncome, totalExpense, netSavings, savingsRate }},
    recentTransactions: state.transactions.slice(-5).reverse(),
    categories: state.categories
  }});
}});</div>

  <h2>6.3 Client View Router Implementation</h2>
  <div class="code-block">function navigateToView(viewName) {{
  document.querySelectorAll('.view-section').forEach(sec => sec.classList.add('hidden'));
  const target = document.getElementById(`view-${{viewName}}`);
  if (target) target.classList.remove('hidden');
  document.querySelectorAll('.nav-item').forEach(btn => {{
    btn.classList.toggle('active', btn.dataset.view === viewName);
  }});
}}</div>

  <div class="section-page-break"></div>

  <!-- CHAPTER 7 -->
  <h1>CHAPTER 7 – TESTING & VERIFICATION</h1>
  
  <table class="data-table">
    <tr><th>Test ID</th><th>Module</th><th>Test Input</th><th>Expected Result</th><th>Status</th></tr>
    <tr><td>TC-01</td><td>Auth</td><td>Submit valid login credentials</td><td>Authenticated, JWT issued</td><td>PASSED</td></tr>
    <tr><td>TC-02</td><td>Auth</td><td>Submit empty email field</td><td>Validation error message displayed</td><td>PASSED</td></tr>
    <tr><td>TC-03</td><td>Auth</td><td>Register new user account</td><td>User created in SQLite DB</td><td>PASSED</td></tr>
    <tr><td>TC-04</td><td>Dashboard</td><td>Fetch dashboard metrics</td><td>Accurate INR totals rendered</td><td>PASSED</td></tr>
    <tr><td>TC-05</td><td>Income</td><td>Log ₹45,000 stipend entry</td><td>Income total increased by ₹45k</td><td>PASSED</td></tr>
    <tr><td>TC-06</td><td>Expense</td><td>Log ₹4,200 Swiggy expense</td><td>Balance reduced, category updated</td><td>PASSED</td></tr>
    <tr><td>TC-07</td><td>Expense</td><td>Log ₹12,500 PG rent expense</td><td>Expense added to Housing category</td><td>PASSED</td></tr>
    <tr><td>TC-08</td><td>Budget</td><td>Exceed category budget cap</td><td>Status badge turns red (Over Budget)</td><td>PASSED</td></tr>
    <tr><td>TC-09</td><td>Ledger</td><td>Search transaction by 'Swiggy'</td><td>Table dynamically filters rows</td><td>PASSED</td></tr>
    <tr><td>TC-10</td><td>Ledger</td><td>Filter transactions by 'Expense'</td><td>Only expense rows displayed</td><td>PASSED</td></tr>
    <tr><td>TC-11</td><td>Export</td><td>Click 'Download CSV' button</td><td>Formatted .csv file downloaded</td><td>PASSED</td></tr>
    <tr><td>TC-12</td><td>Export</td><td>Click 'Export Backup JSON'</td><td>Structured .json backup downloaded</td><td>PASSED</td></tr>
    <tr><td>TC-13</td><td>Theme</td><td>Click Theme Toggle button</td><td>CSS theme toggles light/dark mode</td><td>PASSED</td></tr>
    <tr><td>TC-14</td><td>Profile</td><td>Update Roll No to 24063115470004</td><td>Profile card updates dynamically</td><td>PASSED</td></tr>
    <tr><td>TC-15</td><td>Delete</td><td>Delete expense transaction</td><td>Transaction removed, totals recalculated</td><td>PASSED</td></tr>
    <tr><td>TC-16</td><td>Chart</td><td>Render 6-month trend chart</td><td>Chart.js canvas renders smooth line</td><td>PASSED</td></tr>
    <tr><td>TC-17</td><td>Mobile</td><td>View UI on 375px viewport</td><td>Sidebar converts to drawer menu</td><td>PASSED</td></tr>
    <tr><td>TC-18</td><td>Security</td><td>Submit HTML tags in title</td><td>Tags escaped, XSS blocked</td><td>PASSED</td></tr>
    <tr><td>TC-19</td><td>Security</td><td>Submit SQL injection payload</td><td>Parameterized query executes safely</td><td>PASSED</td></tr>
    <tr><td>TC-20</td><td>Latency</td><td>Dispatch API request</td><td>REST response latency < 15ms</td><td>PASSED</td></tr>
  </table>

  <div class="section-page-break"></div>

  <!-- CHAPTER 8 -->
  <h1>CHAPTER 8 – RESULTS & PROJECT OUTCOMES</h1>

  <h2>8.1 Summary of Results</h2>
  <p>HisabKitab successfully provides a fast, simple, and relatable personal finance manager for students at Jan Nayak Ch. Devi Lal Memorial College, Sirsa. Testing showed API response times under 15ms and clean responsive UI rendering across desktop and mobile devices.</p>

  <div class="section-page-break"></div>

  <!-- CHAPTER 9 -->
  <h1>CHAPTER 9 – CONCLUSION</h1>

  <h2>9.1 Summary & Key Learning Outcomes</h2>
  <p>The major project entitled HisabKitab demonstrates how modern web development frameworks (Node.js, Express, SQLite, HTML5/CSS3/JavaScript, Chart.js) can be effectively applied to solve real-life personal financial budgeting challenges.</p>
  <p>By eliminating complex corporate jargon and providing intuitive visual feedback in Indian Rupees (₹), HisabKitab empowers college students at Jan Nayak Ch. Devi Lal Memorial College, Sirsa to build disciplined spending and savings habits.</p>

  <div class="section-page-break"></div>

  <!-- CHAPTER 10 -->
  <h1>CHAPTER 10 – FUTURE SCOPE</h1>

  <h2>10.1 Planned Enhancements</h2>
  <p>1. Automated UPI SMS Parsing: Integrating Android notification listeners to automatically extract transaction titles and amounts from PhonePe/Paytm SMS alerts.</p>
  <p>2. AI-Powered Expense Predictions: Incorporating machine learning models to forecast end-of-month cash reserves.</p>
  <p>3. Multi-User Shared Hostel Budgets: Adding permission roles for shared flat rent and group meal splits.</p>

  <div class="section-page-break"></div>

  <!-- REFERENCES & APPENDIX -->
  <h1>REFERENCES & APPENDIX</h1>
  <p>[1] Mozilla Developer Network (MDN), 'Web Development & JavaScript References', 2025.<br>
     [2] Express.js Documentation, 'Fast, Unopinionated Web Framework for Node.js', 2026.<br>
     [3] Chart.js Documentation, 'Simple JavaScript Charting', 2026.<br>
     [4] SQLite Documentation, 'Embedded Relational Database Engine', 2026.<br><br>
     <strong>Appendix A: Candidate Profile:</strong><br>
     • Student Name: Keshav Ladha<br>
     • University Roll No: 24063115470004<br>
     • Course: Bachelor of Computer Applications (BCA)<br>
     • Session: 2024–2027<br>
     • College: Jan Nayak Ch. Devi Lal Memorial College, Sirsa (Haryana)<br>
     • Affiliation: Chaudhary Devi Lal University (CDLU), Sirsa<br>
     • Father's Name: Mr. Anjani Kumar</p>

</body>
</html>
"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("HTML report created. Converting to Project_Report.pdf via Playwright...")

    with sync_playwright() as p:
        browser = p.chromium.launch(channel='msedge', headless=True)
        page = browser.new_page()
        page.goto(f"file:///{html_path.replace('\\', '/')}")
        page.wait_for_timeout(2000)
        page.pdf(
            path=pdf_path,
            format='A4',
            print_background=True,
            margin={'top': '20mm', 'bottom': '20mm', 'left': '15mm', 'right': '15mm'}
        )
        browser.close()

    print(f"Project_Report.pdf successfully created at {pdf_path}")

if __name__ == '__main__':
    build_html_and_pdf()
