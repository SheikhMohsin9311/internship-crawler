import asyncio
import random
import pandas as pd
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

# We use Hacker News Jobs for this test because it is safe and doesn't block bots.
TARGET_URL = "https://news.ycombinator.com/jobs"

async def run():
    print(f"[*] Starting scraper for: {TARGET_URL}")
    
    async with async_playwright() as p:
        # headless=False means you will SEE the browser open. 
        # If you get an error about 'displays', change this to True.
        browser = await p.chromium.launch(headless=False)
        
        # Create a browser context (like a user profile)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        print("[*] Navigating...")
        await page.goto(TARGET_URL, wait_until="domcontentloaded")
        
        # Random sleep to mimic human behavior
        await asyncio.sleep(random.uniform(2, 4))

        # Get the HTML content
        content = await page.content()
        print("[*] Page loaded. Parsing HTML...")
        
        soup = BeautifulSoup(content, 'html.parser')
        jobs_found = []

        # Select job rows (Specific to Hacker News HTML structure)
        rows = soup.select('tr.athing')
        
        for row in rows:
            title_elem = row.select_one('.titleline > a')
            if title_elem:
                title = title_elem.get_text(strip=True)
                link = title_elem['href']
                
                # Simple keyword check
                is_intern = "intern" in title.lower()
                
                jobs_found.append({
                    "title": title,
                    "url": link,
                    "is_intern": is_intern
                })

        await browser.close()
        
        # Save results
        if jobs_found:
            df = pd.DataFrame(jobs_found)
            print(f"\n[+] Found {len(jobs_found)} jobs.")
            
            # Print any potential internships found
            internships = df[df['is_intern'] == True]
            if not internships.empty:
                print(f"[!] Found {len(internships)} POTENTIAL INTERNSHIPS:")
                print(internships[['title', 'url']])
            
            # Save to CSV
            df.to_csv("jobs.csv", index=False)
            print("\n[+] Data saved to 'jobs.csv'")
        else:
            print("[-] No jobs found. Check your selectors.")

if __name__ == "__main__":
    asyncio.run(run())