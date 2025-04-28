# Pulse-AI Module Extraction Agent

This project is developed for the Pulse-AI assignment.  
It extracts structured information (Modules and Submodules) from help documentation websites using an AI-powered agent.

## 🚀 Technologies Used
- Python 3.10+
- Streamlit (for building the Web App)
- BeautifulSoup4 (for parsing HTML)
- Requests (for downloading web pages)
- lxml (for faster HTML parsing)
- tqdm (for progress visualization)

## 🛠️ Setup Instructions
1. Clone this repository or download the ZIP file.
2. Create a virtual environment:
   python -m venv venv
3. Activate the virtual environment:
   - Windows:
     venv\Scripts\activate
4. Install dependencies:
   pip install -r requirements.txt
5. Run the Streamlit app:
   streamlit run app.py

## 📋 How the Project Works
- The user enters one or multiple help documentation URLs (one per line).
- The crawler visits the pages and collects all important content.
- The extractor processes the HTML to identify:
  - Modules (using <h1> tags)
  - Submodules (using <h2> tags)
  - Descriptions (using <p> tags)
- The app displays the structured JSON output.
- The output is also saved locally as output.json.

## 🧪 Testing
This project was tested successfully on the following websites:
- https://support.neo.space/hc/en-us
- https://wordpress.org/documentation/
- https://help.zluri.com/
- https://www.chargebee.com/docs/2.0/

## 📦 Example Usage
Input URL:
https://support.neo.space/hc/en-us

Example Output:
[
  {
    "Account Settings": {
      "Description": "Manage your account preferences and login information.",
      "Submodules": {
        "Change Username": "Steps to change your username.",
        "Delete Account": "How to permanently delete your account."
      }
    }
  }
]

## ⚙️ Assumptions
- Only internal links from the same domain are crawled.
- Garbage headings like "Learn More", "Contact Us", etc. are ignored.
- A maximum of 20 pages are crawled per URL to avoid excessive crawling.

## 🚫 Limitations
- Some websites with very unusual HTML structures may produce incomplete outputs.
- Crawling speed is limited intentionally (0.5-second delay) to avoid server overload.

## 🎥 Demo Video
👉 https://www.loom.com/share/48aad4241dd44cb9ac4981be653d78da

## 📂 Folder Structure
pulse_ai_module_extractor/
├── app.py

├── crawler.py 

├── extractor.py

├── requirements.txt

├── README.md

├── venv/ (virtual environment - not uploaded to GitHub)
