import os
from flask import Flask, request, render_template
import textwrap
from IPython.display import display, Markdown

import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)

# Configure GenerativeAI API key
genai.configure(api_key="AIzaSyBiJP5jccCgmtz3FaQz9UAOKo470f9EuGE")

# Function to convert text to Markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Function to generate summary and emotions for the chat text
def generate_summary_and_emotions(chat_text):
    model = genai.GenerativeModel('gemini-pro')
    rply = model.generate_content("Summarize and give the emotions for the given WhatsApp chat"+chat_text)
    to_markdown(rply.text)
    return rply.text

# Route for home page with file upload form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'Chat_file' not in request.files:
            return render_template('error.html', message='No file part')

        file = request.files['Chat_file']

        # Check if the file is empty
        if file.filename == '':
            return render_template('error.html', message='No selected file')

        # Check if the file is of allowed type
        if file and file.filename.endswith('.txt'):
            # Read the file content
            chat_text = file.read().decode('utf-8')

            # Generate summary and emotions
            summary_and_emotions = generate_summary_and_emotions(chat_text)
            
            # Render the result template with summary and emotions
            return render_template('result.html', summary_and_emotions=summary_and_emotions)

        else:
            return render_template('error.html', message='Invalid file type. Please upload a text file')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
