# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)

# Gematria values for Hebrew characters
gematria_values = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
    'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40, 'נ': 50, 'ן': 50, 'ס': 60, 'ע': 70,
    'פ': 80, 'ף': 80, 'צ': 90, 'ץ': 90, 'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
}

# Function to calculate Gematria value of a word or sentence
def calculate_gematria(hebrew_text):
    total_value = 0
    for letter in hebrew_text:
        value = gematria_values.get(letter, 0)  # Get Gematria value, default to 0 if not found
        total_value += value
    return total_value

# Initialize translator
translator = Translator()

# Define route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route to process the form submission
@app.route('/calculate', methods=['POST'])
def calculate():
    user_input = request.form['hebrew_text']  # Get input from form

    # Try translating the input to Hebrew
    try:
        translation = translator.translate(user_input, src='auto', dest='he').text
        gematria_value = calculate_gematria(translation)  # Calculate Gematria value for the Hebrew translation
        return render_template('index.html', user_input=user_input, translation=translation, gematria_value=gematria_value)
    except Exception as e:
        # Handle translation errors or unknown language input
        error_message = f"Error: Unable to translate or calculate Gematria value. {str(e)}"
        return render_template('index.html', error_message=error_message)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
