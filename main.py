from flask import Flask, render_template, request
import os
import re
import google.generativeai as genai

# Set your Gemini API key
os.environ["GOOGLE_API_KEY"] = "Yor-key-here"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

for m in genai.list_models():
    print(m.name)

app = Flask(__name__)

# Initialize Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == "POST":
        # Collect form data
        age = request.form['age']
        gender = request.form['gender']
        weight = request.form['weight']
        height = request.form['height']
        veg_or_nonveg = request.form['veg_or_nonveg']
        disease = request.form['disease']
        region = request.form['region']
        allergies = request.form['allergies']


        # Build prompt
        prompt = (
            "Diet Recommendation System:\n"
            "I want you to recommend 5 breakfast names, 5 lunch names, 5 dinner names and 5 snacks names."
            "based on the following criteria:\n"
            f"Person age: {age}\n"
            f"Person gender: {gender}\n"
            f"Person weight: {weight}\n"
            f"Person height: {height}\n"
            f"Person veg_or_nonveg: {veg_or_nonveg}\n"
            f"Person generic disease: {disease}\n"
            f"Person region: {region}\n"
            f"Person allergies: {allergies}\n"
            "Format your response like this:\n"
            "Breakfast:\n- ...\nLunch\n- ...\nDinner:\n- ...\nSnacks:\n- ..."
        )

        # Get response from Gemini
        response = model.generate_content(prompt)
        results = response.text

        def extract_section(text, start, end):
            pattern = rf"{start}:(.*?){end}:"
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                return [line.strip("-• ").strip() for line in match.group(1).strip().split('\n') if line.strip()]
            return []

        breakfast_names = extract_section(results, "Breakfast", "Lunch")
        lunch_names = extract_section(results, "Lunch", "Dinner")
        dinner_names = extract_section(results, "Dinner", "Snacks")
        snacks_names = extract_section(results, "Snacks", "")


        return render_template(
            'result.html',
            breakfast_names=breakfast_names,
            lunch_names=lunch_names,
            dinner_names=dinner_names,
            snacks_names=snacks_names
        )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)