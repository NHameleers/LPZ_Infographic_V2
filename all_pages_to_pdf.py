import pdfkit
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from pathlib import Path
import pandas as pd

import sqlite3

# from PIL import Image
from PIL import Image as PILI
from wand.image import Image

import sys


unit_of_analysis = ''

if len(sys.argv) < 2:
    print("Usage: python all_teampages_to_pdf.py unit_of_analysis")
    print("Unit of analysis can be one of: team, locatie, organisatie")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Usage: python all_teampages_to_pdf.py unit_of_analysis")
    print("Unit of analysis can be one of: team, locatie, organisatie")
    sys.exit(1)
else:
    unit_of_analysis = sys.argv[1]


conn = sqlite3.connect('TeamInfographics/db.sqlite3')  # pass your db url

df = pd.read_sql(f'SELECT * FROM Lpz2019{unit_of_analysis.title()}s', conn)

outputdir = f'Output/{unit_of_analysis}'

Path(outputdir).mkdir(exist_ok=True)


for i in range(df.shape[0]):

    team_html_path = os.path.join(f'http://127.0.0.1:8000/posters/nov2019/{unit_of_analysis}/{i+1}')

    # not such an elegant way, but since the length of the df changes with unit of analysis
    #  this is the best I can come up with now

    pdf_output_base = f'{outputdir}/poster_{i+1}_{df["Organisatie"][i]}'
    if unit_of_analysis == 'locatie':
        pdf_output_base = f'{pdf_output_base}_{df["Locatie"][i].replace("/", "-")}'
    elif unit_of_analysis == 'team':
        pdf_output_base = f'{pdf_output_base}_{df["Ward_code_origineel"].replace("/", "-")}'

    pdf_output = f'{pdf_output_base}.pdf'

    options = {
    'page-size': 'A3',
    'orientation': 'Landscape',
    'dpi': 400,
    'margin-top': '0in',
    'margin-right': '0in',
    'margin-bottom': '0in',
    'margin-left': '0.15in',
    # 'disable-smart-shrinking': '',
    # 'print-media-type': '',
    'zoom': 1.15,
    'encoding': 'utf-8'
    }

    path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

    # save the pdf
    pdfkit.from_url(team_html_path, 'temp.pdf', options=options, configuration=config)
    print('Temp.pdf written to disk')


    # pdf split, save only first page.
    with open('temp.pdf', 'rb') as r:
        reader = PdfFileReader(r)
        writer = PdfFileWriter()
        writer.addPage(reader.getPage(0))
        with open(pdf_output, 'wb') as w:
            writer.write(w)
        print('Output successfully written to', pdf_output)



    # # To remove color differences of transparent PNG files,
    # # convert pdf to jpg and back
    # print('Converting PDF to JPG...')
    # f = str(pdf_output)
    # newfilename = ''
    # with(Image(filename=f, resolution=600)) as source: 
    #     images = source.sequence
    #     pages = len(images)
    #     for i in range(pages):
    #         n = i + 1
    #         newfilename = f[:-4] + str(n) + '.jpeg'
    #         Image(images[i]).save(filename=newfilename)

    # # convert the team JPG back to single page PDF
    # teamposter_img = PILI.open(newfilename)
    # final_pdf_output = OUTPUT_JPG_TO_PDF / f'Teamposter_{team}.pdf'
    # teamposter_img.save(final_pdf_output, "PDF" ,resolution=600.0, save_all=True)

    # # add filename to list as preparation for pdf with all team posters (60-pages)
    # jpgs.append(newfilename)




    # print('Adding all JPGs to PDF...')
    # im1 = PILI.open(jpgs[0])
    # im_list = [PILI.open(img_path) for img_path in jpgs[1:]]

    # pdf1_filename = OUTPUT_DIR / 'all_team_posters.pdf'

    # im1.save(pdf1_filename, "PDF" ,resolution=600.0, save_all=True, append_images=im_list)


    # end_time = datetime.datetime.now()
    # print(f'Ending script at {end_time}')
    # print(f'Runtime was: {end_time - start_time}')