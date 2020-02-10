"# LPZ_Infographic_V2" 

Voorbereidingen

Data in database zetten met:
python data_to_db.py

Model van data naar models.py met
python manage.py inspectdb LPZ2019Teams > posters/models.py

In models.py:
add primary_key=True to id variable and removed blank=True and null=True.

Maak pie-charts voor elk team met:
in helper_scripts map:
python create_all_pies.py
