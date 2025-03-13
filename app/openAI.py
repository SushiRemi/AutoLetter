import base64
from openai import OpenAI
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
import os
import json

# Register Times New Roman font
times_new_roman_path = "C:/Windows/Fonts/times.ttf"  # Windows default Times New Roman path
if os.path.exists(times_new_roman_path):
    pdfmetrics.registerFont(TTFont('Times New Roman', times_new_roman_path))

client = OpenAI(
    api_key ="replace with key lol, git doesn't allow api key commits"
)

# ^^ this is my key, you can use it or use yours ^0^


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image, replace it with your screenshot name
# this will be a screenshot of job listing requirments
image_path = "teslajob.jpg"

# Getting the Base64 string
base64_image = encode_image(image_path)


def create_cover_letter_pdf(content, output_filename="cover_letter.pdf"):
    c = canvas.Canvas(output_filename, pagesize=letter)
    width, height = letter
    
    # Set font and size
    font_name = 'Times New Roman' if os.path.exists(times_new_roman_path) else 'Helvetica'
    c.setFont(font_name, 12)
    
    # Start position
    y = height - 50
    margin = 50
    
    # Split content into lines that fit the page width
    lines = simpleSplit(content, font_name, 12, width - 2*margin)
    
    # Write each line
    for line in lines:
        if y < 50:  # If we're near the bottom of the page
            c.showPage()  # Start a new page
            y = height - 50  # Reset y position
            c.setFont(font_name, 12)  # Reset font
        
        c.drawString(margin, y, line)
        y -= 15  # Move down for next line
    
    c.save()
    return output_filename


def parseJSON(json_file_path="user_info.json"):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            if 'name' in data:
                print(f"Loading profile for: {data['name']}")
            else:
                print("No name found in JSON file")
            return data
    except FileNotFoundError:
        print(f"JSON file not found: {json_file_path}")
        return None
    except json.JSONDecodeError:
        print("Invalid JSON format")
        return None


# Get user data from JSON
user_data = parseJSON()

if user_data:
    # Create a personalized prompt using the JSON data
    prompt = f"""Here's an image with a Software Engineering Internship job listing/description. 
    Please write a cover letter for this position based on the requirements/qualifications.
    
    Use the following information about me in the cover letter:
    Name: {user_data.get('name', '')}
    Education: {user_data.get('education', '')}
    Skills: {', '.join(user_data.get('skills', []))}
    Experience: {user_data.get('experience', '')}
    Projects: {', '.join(user_data.get('projects', []))}
    
    Please create a professional cover letter that highlights how my background matches the job requirements."""
else:
    # Default prompt if no JSON data is available
    prompt = "Here's an image with a Software Engineering Internship job listing/description. Please write a cover letter for this position based on the requirements/qualifications."

# Send the image for analysis
response = client.chat.completions.create(
    model="gpt-4o",  # GPT-4o supports vision
    messages=[
        {"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
        ]}
    ]
)

# Get the cover letter content
#print(response.choices[0].message.content)
cover_letter_content = response.choices[0].message.content

# Create PDF
pdf_filename = create_cover_letter_pdf(cover_letter_content)
print(f"Cover letter has been saved to {pdf_filename}")

# Parse JSON file
parseJSON()