import pathlib
import textwrap

import google.generativeai as genai

# Used to securely store your API key


from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="AIzaSyBiJP5jccCgmtz3FaQz9UAOKo470f9EuGE")

model = genai.GenerativeModel('gemini-pro')

with open('chat.txt', 'r', encoding='utf-8') as file:
    chat_text = file.read()
   

rply = model.generate_content("Summarize and give the emotions for the given whatsapp chat"+chat_text)
to_markdown(rply.text)
print(rply.text)