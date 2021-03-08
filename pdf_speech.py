#Importing required libraries
import PyPDF2
import pyttsx3

#path of the PDF file
path = open('file.pdf', 'rb')

#Creating a PdfFileReader object
pdf_reader = PyPDF2.PdfFileReader(path)

#The page which you want to start this will read the page of 25th page.
from_page = pdf_reader.getPage(12)

#Now extracting the text from PDF
text = from_page.extractText()

#Reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
