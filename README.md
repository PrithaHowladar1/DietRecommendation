AI-powered personalized health assistant built with Flask and Google Gemini.
Get tailored meal (including regional cuisine) suggestions based on your age, gender, health profile, allergies and dietary preferences — all in seconds.

Powered By
- 🧬 Google Gemini 1.5 Flash — for fast, intelligent content generation
- 🐍 Flask — lightweight Python web framework
- 🎨 Bootstrap 4 — responsive, modern UI
- 🔍 Regex Parsing — clean extraction of AI-generated content


✨ Features
- ✅ Personalized Diet Plans — breakfast, lunch, dinner, snacks
- ✅ Responsive UI — sleek cards, dark mode, mobile-friendly
- ✅ Downloadable Results — save recommendations as .txt
- ✅ Gemini Integration — real-time AI responses
- ✅ Regex Extraction — structured parsing of AI output

<img width="1917" height="1015" alt="Screenshot 2025-08-23 011925" src="https://github.com/user-attachments/assets/97e6bbf2-b939-40f3-9ecd-c7cc4a46c37e" />
<img width="1913" height="1035" alt="Screenshot 2025-08-23 010206" src="https://github.com/user-attachments/assets/ca662af1-77b8-45ad-adfe-d85c017e2e25" />
<img width="1910" height="1022" alt="Screenshot 2025-08-23 012107" src="https://github.com/user-attachments/assets/25ff928a-ac90-417e-9d29-02192254b59c" />


🔐 Coming Soon
- 🔑 User Authentication — login/signup with Flask-Login
- 💾 Save Recommendations — revisit your plans anytime
- 📊 Progress Tracker — visualize weight and fitness goals
  

🛠️ Installation
git clone https://github.com/yourusername/diet-recommendation-app.git
cd diet-recommendation-app
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt



🔑 Setup Gemini API
- Go to Google AI Studio
- Generate your API key
- Add it to your environment:
os.environ["GOOGLE_API_KEY"] = "your-api-key-here"



🧪 Run the App
python app.py


Visit http://localhost:5000 in your browser.

📁 Project Structure
diet-recommendation-app/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── images/ (optional background)
│
├── app.py
├── forms.py (optional for login/signup)
├── requirements.txt
└── README.md




Would you like me to generate a matching requirements.txt or help you deploy this live?
