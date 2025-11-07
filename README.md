# Linkedin-Scrapper-App
Full-stack LinkedIn scraper powered by Flask, Selenium, and Pandas with a modern UI and dynamic CSV export functionality.
🧩 LinkedIn Profile Scraper — Flask + Selenium App
🔍 Overview

The LinkedIn Profile Scraper App is a full-stack web application that allows users to extract basic public details (like name and headline) from multiple LinkedIn profiles and export them into a CSV file — all through an interactive and elegant web interface.

Built using Python, Flask, Selenium, HTML, CSS, and JavaScript, this project demonstrates the integration of backend automation with a dynamic frontend interface, creating a seamless experience for scraping and data export.

⚙️ Key Features

🧠 AI-inspired Web Automation: Automates profile scraping using Selenium WebDriver.

🌐 Interactive Frontend: Users can enter multiple LinkedIn profile URLs directly from the browser.

📊 Progress Tracking: Real-time progress bar displays scraping status dynamically.

📁 CSV Export: Automatically generates and allows downloading of extracted data in CSV format.

🎨 Modern UI/UX: Designed with clean CSS animations, responsive layout, and smooth transitions.

🔒 Session-Based Login: Authenticates into LinkedIn securely before fetching profile data.

🛠️ Tech Stack

Frontend:

HTML5

CSS3 (modern gradients, animations)

JavaScript (live progress updates using Fetch API)

Backend:

Flask (Python Web Framework)

Selenium WebDriver (Chrome)

Pandas (for CSV data handling)

Fake-UserAgent (for browser fingerprinting avoidance)

🚀 How It Works

Enter one or more LinkedIn profile URLs in the input form.

The app logs into LinkedIn via Selenium (with your credentials).

It scrapes each profile’s name and headline using dynamic XPaths.

A real-time progress bar updates as each profile is processed.

Once complete, a Download CSV button appears for instant export.

⚡ Setup Instructions

Clone the repository:

git clone https://github.com/your-username/linkedin-scraper-app.git
cd linkedin-scraper-app


Install dependencies:

pip install -r requirements.txt


Add your LinkedIn credentials inside scraper.py

driver.find_element(By.ID, "username").send_keys("YOUR_LINKEDIN_EMAIL")
driver.find_element(By.ID, "password").send_keys("YOUR_PASSWORD")


Run the app:

python app.py


Open in browser:

http://127.0.0.1:5000

⚠️ Important Note

This project is intended strictly for educational and personal use.
LinkedIn prohibits automated data scraping without explicit consent.
Use responsibly — only on profiles you have permission to access or your own test accounts.

🧠 Future Enhancements

Add login form for user credentials input via frontend.

Extract additional details (location, company, about section).

Save past scraping sessions with timestamps.

Deploy to Render / AWS for online access.

📸 Preview
🔹 User enters LinkedIn URLs  
🔹 Progress bar shows scraping status  
🔹 CSV file downloads instantly  

🧑‍💻 Author

Sambit Saha

🎓 M.Tech in Geomatics, IIT (ISM) Dhanbad

💻 Software Developer | AI & Web Development Enthusiast

🌐 LinkedIn
 • GitHub
