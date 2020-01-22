import pdfkit
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
import os

# from PIL import Image
from PIL import Image as PILI
from wand.image import Image



team_html_path = os.path.join('http://127.0.0.1:8000/posters/')


pdf_output = 'Teamposter_test.pdf'


options = {
'page-size': 'A4',
'orientation': 'Landscape',
'dpi': 400,
'margin-top': '0in',
'margin-right': '0in',
'margin-bottom': '0in',
'margin-left': '0in'}

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