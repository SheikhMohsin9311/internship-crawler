🕷️ Internship Crawler 2026
A Scalable, Intelligent Web Crawler for Aggregating Internship Opportunities.

Status: Active Development
Stack: Python 3.12, Scrapy, Playwright, PostgreSQL, Pandas

📖 Overview
finding internships is a fragmented process. Candidates often miss opportunities because they appear on disparate company career pages or get buried under "Senior" roles on major job boards.

Internship Crawler is a specialized engineering solution designed to:

Aggregate listings from major job boards (LinkedIn, Indeed, Glassdoor) and niche university boards and websites.

Evade modern anti-bot systems using browser fingerprint spoofing (Camoufox).

Filter noise using NLP to strictly target "Intern", "Co-op", and "Summer 2026" roles.

Deduplicate listings across multiple sites using MinHash algorithms.

🚀 Key Features
Hybrid Architecture: Uses lightweight HTTP requests for speed and Playwright (headless browser) for JavaScript-heavy sites.

Stealth Mode: Integrates Camoufox to spoof browser fingerprints (Canvas, WebGL, Fonts) and bypass Cloudflare/PerimeterX protections.

Smart Filtering: Discards "Senior", "Principal", or "Unpaid" roles automatically.

Data Normalization: Extracts unstructured data (e.g., "Stipend: $25/hr", "Duration: 12 weeks") into structured SQL columns using Regex and NLP.

Deduplication: Uses MinHash (LSH) to detect if the same job description exists in the database, even if the URL or formatting is different.

🛠️ Technical Architecture
Code snippet
graph LR
    A --> B(Scrapy Spider);
    B --> C{Dynamic Content?};
    C -- Yes --> D[Playwright/Camoufox];
    C -- No --> E;
    D --> F[Parser];
    E --> F;
    F --> G[Item Pipeline];
    G --> H{Duplicate?};
    H -- No --> I;
    H -- Yes --> J;
📦 Installation & Setup
Prerequisites
OS: Linux (Ubuntu 22.04/24.04 recommended), macOS, or Windows (WSL2).

Python: 3.10 or higher.

Database: PostgreSQL (optional for prototype, required for production).

1. Clone & Environment
Bash
# Clone the repository (if applicable)
# git clone https://github.com/yourusername/internship-crawler.git

# Create a virtual environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate  # Linux/Mac
#.\venv\Scripts\Activate  # Windows
2. Install Dependencies
Bash
pip install playwright beautifulsoup4 pandas scrapy scrapy-playwright sqlalchemy psycopg2-binary datasketch
3. Install Browsers
Crucial Step for Ubuntu/Linux Users:
You must install the system-level dependencies for the browsers to run.

Bash
# 1. Install Playwright browsers
playwright install

# 2. Install system dependencies (requires sudo)
sudo./venv/bin/playwright install-deps
🏃 Usage
Running the Prototype
To test the browser automation and extraction logic on a simple target:

Bash
python3 first_crawler.py
Output: A file named jobs.csv containing the scraped data.

Running the Full Scrapy Spider (Upcoming)
Note: This requires the Phase 2 implementation.

Bash
# Start the crawler for a specific spider (e.g., 'indeed' or 'linkedin')
scrapy crawl indeed -o output.json
⚖️ Legal & Ethical Disclaimer
This tool is designed for educational and personal use.

Respect robots.txt: This crawler should be configured to respect the robots.txt policies of target websites.

Rate Limiting: Do not aggressively flood servers. Default settings use a 2-5 second delay between requests.

Data Privacy: Do not collect or distribute personal identifiable information (PII) of recruiters or employees found in job descriptions.

Terms of Service: Users are responsible for ensuring their scraping activities comply with the Terms of Service of the target websites.

Reference Case: hiQ Labs, Inc. v. LinkedIn Corp (2019) - Scrapers accessing publicly available data without authentication are generally not in violation of the CFAA in the US.

🗺️ Roadmap
[x] Phase 1: Prototype with Playwright & BeautifulSoup.

[ ] Phase 2: Scrapy integration & PostgreSQL Database connection.

[ ] Phase 3: Intelligent Deduplication (MinHash).

[ ] Phase 4: Anti-Bot Evasion (Camoufox Integration).

[ ] Phase 5: Automate daily runs via Cron/GitHub Actions.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.