from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import RGBColor
import os
import win32com.client
import datetime
import plotly.io as pio
import plotly
from docx.shared import Pt
from data_breaches_bar_chart_bubble_plot_actual_year import Charts_DataBreaches

date = datetime.date.today()
actual_year = date.strftime("%Y")

#Laden der Diagramme
dbr = Charts_DataBreaches()
dbr.fig_bubblechart.write_image("fig_bubblechart.png")
dbr.create_lineplot(int(actual_year) -1).write_image("fig_lineplot.png")

#Dokument laden
document = Document('LaCTiS_Report - Template.docx')

#Text-Style-Überschriften
'''style = document.styles['Normal']
font = style.font
font.name = 'Arial'
font.size = Pt(14)'''

# Überschriften

header1 = 'CYBER SECURITY REPORT '
heading = document.add_heading(header1 + '|' + actual_year, level = 0)
header2 = document.add_paragraph().add_run('LaCTiS - Your expert in Cyber Security!')
#header2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
header2.font.size = Pt(16)
header2.font.name = 'Calibri'
header2.font.color.rgb = RGBColor(0x2F, 0x54, 0x96)
header2.bold = True

document.add_picture('LaCTis_Logo.png', width=Inches(1.5))
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT

header3 = document.add_paragraph().add_run('We are happy, to Cyber Secure you.')
header3.font.size = Pt(14)
header3.font.name = 'Calibri'
header3.font.color.rgb = RGBColor(0x2F, 0x54, 0x96) 
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT

#Einleitung
einleitung = document.add_paragraph('Die digitale Transformation bietet den meisten Unternehmen viele neue und bedeutende Chancen.'\
'Schnell wird jedoch klar, dass diese Transformation auch Risiken herbeiführen kann. Dabei ist fast jeder,' \
'also Unternehmen, öffentliche Institutionen, andere Organisationen sowie Privatpersonen das Ziel von Cyber-Attacken.' \
'Die Bedrohungslage nimmt stetig zu. Ziel sind die sensiblen und wertvollen Daten. '\
'Cyber Security wird in vielen deutschen Unternehmen vernachlässigt. Oft können die Unternehmen die Risiken der Cyberkriminalität nicht abschätzen.' \
'Die Angst vor Cyberkriminalität ist meist nicht groß genug.'\
'Betrachtet man im Gegenzug dazu erfasste Fälle von Cyberkriminalität in den letzten zehn Jahren in Deutschland, so kann man 2020 fast vierfach so viele Fälle feststellen.'\
'Cyberkriminalität lässt sich geradezu als Wachstumsbranche bezeichnen. Neben den Hobby-Hackern gibt es mittlerweile professionelle Anbieter, die ihre Hacker-Services' \
'als Dienstleistung anbieten.'\
'Besonders kleine und mittelständische Unternehmen stehen im Visier von Cyberkriminiellen. Denn diese haben meist unterdurchschnittliche Sicherheitsvorkehrungen.')
einleitung.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY


#paragraph.add_run('intro').bold = True

#Seitenumbruch
document.add_page_break()

# Thema Data Breaches
document.add_picture('fig_lineplot.png', width=Inches(5.0))
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
abbildung_1 = document.add_paragraph('Abbildung 1: Data Breaches über x Jahre')
abbildung_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

document.add_picture('fig_bubblechart.png', width=Inches(5.0))
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
abbildung_2 = document.add_paragraph('Abbildung 2: Data Breaches')
abbildung_2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER



document.save('LaCTiS_Report.docx')

wdFormatPDF = 17
'''inputFile = os.path.abspath("LaCTiS_Report.docx")
outputFile = os.path.abspath("LaCTis_Report.pdf")
word = win32com.client.Dispatch('Word.Application')
doc = word.Documents.Open(inputFile)
doc.SaveAs(outputFile, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()'''