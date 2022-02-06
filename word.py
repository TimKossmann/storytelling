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
from data_breaches_attack_vectors_treemap import Chart_AttackVectors
from phishing_graphs import Phishing_Graphs
from passwords_wordcloud import Chart_WordCloud

import numpy as np


date = datetime.date.today()
actual_year = date.strftime("%Y")

#Laden der Diagramme
#Data Breaches
dbr = Charts_DataBreaches()
dbr.update_bubblechart_by_year(int(actual_year) -1, False).write_image("fig_bubblechart.png")
dbr.create_lineplot(int(actual_year) -1, False).write_image("fig_lineplot.png")
dbr.create_table().write_image('fig_table.png')


#Cyber Attacken
atp = Chart_AttackVectors()
atp.fig.write_image("treemap.png")
atp.create_treemap_mensch().write_image("treemap_mensch.png")
#Phishing
pg = Phishing_Graphs()
pg.get_link_donut(False).write_image("phising_link.png")
pg.get_input_donut(False).write_image("phising_input.png")
pg.get_attach_donut(False).write_image("phising_attach.png")
pg.get_fail_bar('Branche', None, False).write_image("fail_bar_mark.png")
pg.get_fail_bar('Abteilung', None, False).write_image("fail_bar_type_name.png")
#WordCloud
wc = Chart_WordCloud()
wc.create_wordcloud(False).save("word_cloud.png", format="png")

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
'Schnell wird jedoch klar, dass diese Transformation auch Risiken herbeiführen kann. Dabei ist fast jeder, ' \
'also Unternehmen, öffentliche Institutionen, andere Organisationen sowie Privatpersonen das Ziel von Cyber-Attacken.' \
'Die Bedrohungslage nimmt stetig zu. Ziel sind die sensiblen und wertvollen Daten. '\
'Cyber Security wird in vielen deutschen Unternehmen vernachlässigt. Oft können die Unternehmen die Risiken der Cyberkriminalität nicht abschätzen.' \
'Die Angst vor Cyberkriminalität ist meist nicht groß genug.'\
'Betrachtet man im Gegenzug dazu erfasste Fälle von Cyberkriminalität in den letzten zehn Jahren in Deutschland, so kann man die '\
'Cyberkriminalität geradezu als Wachstumsbranche bezeichnen. Neben den Hobby-Hackern gibt es mittlerweile professionelle Anbieter, die ihre Hacker-Services' \
'als Dienstleistung anbieten.'\
'Besonders kleine und mittelständische Unternehmen stehen im Visier von Cyberkriminiellen. Denn diese haben meist unterdurchschnittliche Sicherheitsvorkehrungen.')
einleitung.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY


#paragraph.add_run('intro').bold = True

#Seitenumbruch
document.add_page_break()

# Thema Data Breaches
heading2 = document.add_heading('Schaden durch Hacks', level = 1)
document.add_picture('fig_lineplot.png', width=Inches(6.0))
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
abbildung_1 = document.add_paragraph('Abbildung 1: Data Breaches über die letzten 8 Jahre')
abbildung_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

document.add_picture('fig_bubblechart.png', width=Inches(6.0))
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
abbildung_2 = document.add_paragraph('Abbildung 2: Data Breaches im Jahr 2021')
abbildung_2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

document.add_picture('fig_table.png', width=Inches(3.0))
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
table_1 = document.add_paragraph('Tabelle 1: Unternehmen mit dem höchsten Schaden durch Data Breaches von Jahr 2014 bis 2021 inklusive der Mediane')
table_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

#Seitenumbruch
document.add_page_break()

#Thema Cyber Attacken
heading2 = document.add_heading('Cyber Attacken', level = 1)
document.add_picture('treemap.png', width=Inches(6.0))
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
abbildung_3 = document.add_paragraph('Abbildung 3: Cyber Attacken nach Angriffsvektor Mensch und System aufgeteilt')
abbildung_3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

document.add_picture('treemap_mensch.png', width=Inches(6.0))
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
abbildung_4 = document.add_paragraph('Abbildung 400: Cyber Attacken mit Angriffsvektor Mensch')
abbildung_4.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

#Seitenumbruch
document.add_page_break()

#Thema Phising
heading3 = document.add_heading('Phising', level = 1)
document.add_picture('phising_link.png', width=Inches(4.0))
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
abbildung_5 = document.add_paragraph('Abbildung 5: Phising via Link')
abbildung_5.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

document.add_picture('phising_input.png', width=Inches(4.0))
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
abbildung_6 = document.add_paragraph('Abbildung 6: Phising via Input')
abbildung_6.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

document.add_picture('phising_attach.png', width=Inches(4.0))
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
abbildung_6 = document.add_paragraph('Abbildung 6: Phising via Anhang')
abbildung_6.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

document.add_picture('fail_bar_mark.png', width=Inches(5.0))
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
abbildung_7 = document.add_paragraph('Abbildung 7: Phising nach Branche')
abbildung_7.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

document.add_picture('fail_bar_type_name.png', width=Inches(5.0))
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
abbildung_7 = document.add_paragraph('Abbildung 7: Phising nach Branche')
abbildung_7.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

#Seitenumbruch
document.add_page_break()

#Thema Passwortsicherheit
heading4 = document.add_heading('Passwortsicherheit', level = 1)
document.add_picture('word_cloud.png', width=Inches(3.0))
last_paragraph = document.paragraphs[-1] 
last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
abbildung_5 = document.add_paragraph('Abbildung 8: Wordcloud zu den meist genutzten Passwörtern')
abbildung_5.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER


document.save('LaCTiS_Report.docx')

wdFormatPDF = 17
'''inputFile = os.path.abspath("LaCTiS_Report.docx")
outputFile = os.path.abspath("LaCTis_Report.pdf")
word = win32com.client.Dispatch('Word.Application')
doc = word.Documents.Open(inputFile)
doc.SaveAs(outputFile, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()'''