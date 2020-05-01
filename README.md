"# LPZ_Infographic_V2" 

Voorbereidingen

SPSS syntax runnen om teamdata te creeren

Data in database zetten met:
python data_to_db.py



Model van data naar models.py met:
python manage.py inspectdb LPZ2019Teams > posters/models.py
OF BIJ MEERDERE NIVEAUS VAN ANALYSE (TEAM-LOCATIE-ORG):
python manage.py inspectdb > posters/models.py


In models.py:
add primary_key=True to id variable and removed blank=True and null=True. (voor team, locatie en organisatie)



Maak pie-charts voor elk team met:
in helper_scripts map:
python create_all_pies.py unit_of_analysis
bijv:
python create_all_pies.py team
python create_all_pies.py locatie
python create_all_pies.py organisatie

Maak dan alle posters met:
in terminal 1: python manage.py runserver
in terminal 2: python all_pages_to_pdf.py unit_of_analysis
bijv:
python all_pages_to_pdf.py team
python all_pages_to_pdf.py locatie
python all_pages_to_pdf.py organisatie