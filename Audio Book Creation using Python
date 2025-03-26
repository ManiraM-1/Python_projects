import PyPDF2  # Library for working with PDFs
import pyttsx3  # Library for text-to-speech conversion

# Open the PDF file in read-binary mode
book = open('<File_name.pdf>', 'rb')

# Create a PDF reader object
pdfReader = PyPDF2.PdfReader(book)

# Get the total number of pages in the PDF
pages = len(pdfReader.pages)
print(f"Total pages: {pages}")  # Print the total number of pages

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Set a slower speech rate for better clarity
speaker.setProperty('rate', 80)

# Get available voices and set the second one (commonly female)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)

print(voices)  # Print available voices for debugging

# Loop through all pages and read them
for num in range(pages):  # Start from 0 to include the first page
    page = pdfReader.pages[num]  # Get the current page
    text = page.extract_text()  # Use the correct method to extract text

    if text.strip():  # Avoid reading empty pages
        speaker.say(text)
        speaker.runAndWait()  # Wait until speaking is finished before proceeding

# Close the PDF file after use
book.close()
