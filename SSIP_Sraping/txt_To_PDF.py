from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Directory containing .txt files
input_directory = r"D:\Sem-5\adv. python\Vipuls py\lab\webScraping\IndianKanoon\txtFiles"

# Directory to save PDF files
output_directory = r"D:\Sem-5\adv. python\Vipuls py\lab\webScraping\IndianKanoon\PDFs"


# Ensure output directory exists, create it if necessary
os.makedirs(output_directory, exist_ok=True)

# Function to convert .txt file to PDF
def txt_to_pdf(input_file, output_file):
    c = canvas.Canvas(os.path.join(output_directory, output_file), pagesize=letter)
    
    # Open .txt file and add content to PDF
    with open(os.path.join(input_directory, input_file), "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    # Set font and initial position
    c.setFont("Helvetica", 12)
    x_position = 50
    y_position = 750
    line_height = 14  # Adjust the line height as needed
    max_y = 50  # Maximum y-position for new page
    
    # Function to create a new page
    def new_page():
        c.showPage()
        c.setFont("Helvetica", 12)
    
    # Draw text on the PDF
    for line in lines:
        words = line.strip().split()
        for word in words:
            # Check if the word exceeds the line width
            word_width = c.stringWidth(word + " ", "Helvetica", 12)
            if x_position + word_width > 550 or y_position < max_y:
                y_position -= line_height
                if y_position < max_y:
                    new_page()  # Start a new page if y-position is less than the maximum
                    y_position = 750  # Reset y-position for new page
                x_position = 50
            # Draw the word
            c.drawString(x_position, y_position, word + " ")
            x_position += word_width
        y_position -= line_height
        x_position = 50
    
    # Save PDF file
    new_page()  # Add the last page
    c.save()

# List of .txt files in the input directory
txt_files = [file for file in os.listdir(input_directory) if file.endswith(".txt")]

# Convert each .txt file to PDF
for txt_file in txt_files:
    pdf_file = txt_file.replace(".txt", ".pdf")
    pdf_file = pdf_file.replace("×","")
    txt_to_pdf(txt_file, pdf_file)

print("Conversion completed.")
