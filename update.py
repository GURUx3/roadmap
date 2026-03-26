import re

css = """
:root {
  --bg: #FAFAFA;
  --surface: #FFFFFF;
  --surface2: #F5F5F7;
  --border: rgba(0, 0, 0, 0.08);
  --border-hover: rgba(0, 0, 0, 0.15);
  --accent: #111111;
  --accent2: #F56E0F;
  --accent3: #0066CC;
  --text: #1D1D1F;
  --muted: #86868B;
  --muted2: #6E6E73;
  --easy: #34C759;
  --easy-bg: #E8F8EE;
  --medium: #F5A623;
  --medium-bg: #FEF5E8;
  --hard: #FF3B30;
  --hard-bg: #FEECEB;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: var(--bg);
  color: var(--text);
  font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  min-height: 100vh;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h1, h2, h3, h4, h5, h6, .brand, .num, .day-name, .week-title {
  font-family: "Plus Jakarta Sans", "Inter", sans-serif;
  letter-spacing: -0.02em;
}

/* HEADER */
.header {
  background: rgba(255, 255, 255, 0.85);
  border-bottom: 1px solid var(--border);
  padding: 20px 32px;
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

.header-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  gap: 32px;
  flex-wrap: wrap;
}

.logo-area h1 {
  font-weight: 700;
  font-size: 20px;
  color: var(--accent);
}

.logo-area p {
  font-size: 13px;
  color: var(--muted);
  font-family: "JetBrains Mono", monospace;
  margin-top: 4px;
}

.header-stats {
  display: flex;
  gap: 16px;
  margin-left: auto;
  flex-wrap: wrap;
}

.stat-chip {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 8px 16px;
  text-align: center;
  transition: all 0.2s ease;
  box-shadow: 0 1px 2px rgba(0,0,0,0.02);
}

.stat-chip:hover {
  border-color: var(--border-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.04);
}

.stat-chip .num {
  font-weight: 700;
  font-size: 16px;
  color: var(--text);
}

.stat-chip .lbl {
  font-size: 11px;
  color: var(--muted);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-top: 2px;
}

/* LAYOUT */
.layout {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 240px 1fr;
  min-height: calc(100vh - 80px);
}

/* SIDEBAR */
.sidebar {
  padding: 32px 24px 32px 0;
  position: sticky;
  top: 80px;
  height: calc(100vh - 80px);
  overflow-y: auto;
}

.sidebar::-webkit-scrollbar {
  width: 4px;
}
.sidebar::-webkit-scrollbar-track {
  background: transparent;
}
.sidebar::-webkit-scrollbar-thumb {
  background: rgba(0,0,0,0.1);
  border-radius: 4px;
}

.sidebar-section {
  margin-bottom: 12px;
}

.month-label {
  font-weight: 700;
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 16px 16px 8px;
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--muted);
}

.month-label .dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  flex-shrink: 0;
}

.m1 { color: var(--accent); }
.m1 .dot { background: var(--accent); }
.m2 { color: var(--accent3); }
.m2 .dot { background: var(--accent3); }
.m3 { color: var(--accent2); }
.m3 .dot { background: var(--accent2); }

.week-btn {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
  background: transparent;
  border: none;
  color: var(--muted2);
  font-size: 13px;
  font-weight: 500;
  padding: 10px 16px;
  cursor: pointer;
  text-align: left;
  border-radius: 8px;
  transition: all 0.2s ease;
  margin-bottom: 2px;
}

.week-btn:hover {
  color: var(--text);
  background: var(--surface2);
}

.week-btn.active {
  color: var(--text);
  background: #FFFFFF;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.02);
  font-weight: 600;
}

.week-num {
  font-family: "JetBrains Mono", monospace;
  font-size: 11px;
  color: var(--muted);
  opacity: 0.7;
}

/* MAIN */
.main {
  padding: 32px 0 64px 48px;
  overflow-y: auto;
}

/* WEEK VIEW */
.week-hero {
  margin-bottom: 40px;
}

.week-title-row {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 12px;
}

.week-title {
  font-weight: 700;
  font-size: 28px;
  color: var(--text);
}

.week-tag {
  background: var(--surface2);
  color: var(--muted2);
  font-family: "JetBrains Mono", monospace;
  font-size: 11px;
  padding: 4px 10px;
  border-radius: 6px;
  white-space: nowrap;
  font-weight: 500;
}

.week-meta {
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
  margin-bottom: 24px;
}

.week-meta span {
  font-size: 14px;
  color: var(--muted2);
  display: flex;
  align-items: center;
  gap: 6px;
}

.week-meta strong {
  color: var(--text);
  font-weight: 500;
}

.mentor-note {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px 24px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--muted2);
  box-shadow: 0 2px 8px rgba(0,0,0,0.02);
}

.mentor-note strong {
  color: var(--text);
  font-weight: 600;
}

/* DAYS GRID */
.days-grid {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.day-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
  transition: all 0.2s ease;
}

.day-card:hover {
  border-color: var(--border-hover);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
}

.day-header {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px 20px;
  background: var(--surface);
  cursor: pointer;
  user-select: none;
  border-bottom: 1px solid transparent;
  transition: background 0.2s;
}

.day-card.open .day-header {
  background: var(--surface2);
  border-bottom: 1px solid var(--border);
}

.day-num {
  font-family: "JetBrains Mono", monospace;
  font-weight: 500;
  font-size: 12px;
  color: var(--muted);
  min-width: 48px;
}

.day-name {
  font-weight: 600;
  font-size: 15px;
  color: var(--text);
  flex: 1;
}

.day-meta {
  display: flex;
  gap: 12px;
  align-items: center;
}

.problem-count {
  font-size: 13px;
  color: var(--muted);
}

.expand-icon {
  color: var(--muted);
  font-size: 16px;
  transition: transform 0.2s ease;
}

.day-card.open .expand-icon {
  transform: rotate(180deg);
}

.day-body {
  display: none;
  padding: 20px;
  flex-direction: column;
  gap: 12px;
}

.day-card.open .day-body {
  display: flex;
}

.day-note {
  font-size: 13px;
  color: var(--muted2);
  line-height: 1.5;
  margin-bottom: 8px;
}

.problem-row {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 12px 16px;
  background: var(--bg);
  border-radius: 8px;
  border: 1px solid var(--border);
  transition: all 0.2s ease;
}

.problem-row:hover {
  border-color: var(--border-hover);
  background: var(--surface);
  box-shadow: 0 2px 8px rgba(0,0,0,0.03);
  transform: translateX(2px);
}

.p-num {
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  color: var(--muted);
  min-width: 28px;
}

.p-name {
  flex: 1;
  font-size: 14px;
  color: var(--text);
  font-weight: 500;
}

.p-lc {
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  color: var(--muted);
}

.p-tag {
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 6px;
  min-width: 60px;
  text-align: center;
  text-transform: uppercase;
}

.p-tag.easy {
  background: var(--easy-bg);
  color: var(--easy);
}

.p-tag.medium {
  background: var(--medium-bg);
  color: var(--medium);
}

.p-tag.hard {
  background: var(--hard-bg);
  color: var(--hard);
}

.p-link {
  color: var(--text);
  text-decoration: none;
  font-size: 12px;
  font-family: inherit;
  font-weight: 500;
  padding: 6px 12px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 6px;
  transition: all 0.2s ease;
  white-space: nowrap;
  box-shadow: 0 1px 2px rgba(0,0,0,0.02);
}

.p-link:hover {
  background: var(--surface2);
  border-color: var(--border-hover);
}

.p-link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

/* REST DAY */
.rest-day .day-header {
  opacity: 0.7;
}

.rest-banner {
  padding: 24px;
  text-align: center;
  font-size: 14px;
  color: var(--muted2);
  line-height: 1.6;
}

/* OVERVIEW BANNER */
.overview {
  margin-bottom: 48px;
}

.overview h2 {
  font-size: 24px;
  margin-bottom: 24px;
  color: var(--text);
}

.phases {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.phase-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.02);
}

.phase-card h3 {
  font-size: 16px;
  margin-bottom: 8px;
  color: var(--text);
}

.phase-card p {
  font-size: 14px;
  color: var(--muted2);
  line-height: 1.6;
}

.phase-card .weeks-tag {
  display: inline-block;
  font-family: "JetBrains Mono", monospace;
  font-size: 11px;
  font-weight: 600;
  color: var(--muted);
  margin-bottom: 12px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* PYTHON/JS TIP */
.lang-tip {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px 20px;
  margin-top: 24px;
  font-size: 14px;
  color: var(--muted2);
  display: flex;
  gap: 16px;
  align-items: flex-start;
  box-shadow: 0 2px 8px rgba(0,0,0,0.02);
}

.lang-icon {
  font-size: 20px;
  line-height: 1;
  flex-shrink: 0;
}

/* RULES */
.rules {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  margin-top: 24px;
}

.rule-item {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px 20px;
  display: flex;
  gap: 12px;
  align-items: flex-start;
  box-shadow: 0 2px 8px rgba(0,0,0,0.02);
}

.rule-icon {
  font-size: 18px;
  flex-shrink: 0;
}

.rule-text {
  font-size: 14px;
  color: var(--muted2);
  line-height: 1.5;
}

.rule-text strong {
  color: var(--text);
}

::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: var(--bg);
}

::-webkit-scrollbar-thumb {
  background: var(--border);
  border-radius: 3px;
}

@media (max-width: 900px) {
  .layout {
    grid-template-columns: 1fr;
    padding: 0 20px;
  }
  .sidebar {
    position: static;
    height: auto;
    padding: 24px 0;
    border-bottom: 1px solid var(--border);
  }
  .main {
    padding: 24px 0 64px 0;
  }
  .phases, .rules {
    grid-template-columns: 1fr;
  }
}
"""

with open(r"c:\\Users\\guru_21\\Roadmaps\\index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_head = '<link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />'
html = re.sub(r'<link[^>]*?href="https://fonts.googleapis.com/css2.*?>', new_head, html, flags=re.DOTALL)
html = re.sub(r'<style>.*?</style>', f'<style>\n{css}\n  </style>', html, flags=re.DOTALL)

with open(r"c:\\Users\\guru_21\\Roadmaps\\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("UI successfully upgraded to 100x clean premium layout.")
