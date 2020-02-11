* Encoding: UTF-8.

CD "F:\2020_01_06_Selectie_backup_I-schijf\LPZ\Infographic_2.0".

* TODO: Als je de syntax wil runnen/gebruiken, dan bestandsnaam aanpassen.
GET
  FILE='NL2019NOV_total.sav'.
DATASET NAME LPZ WINDOW=FRONT.






**************** Variabelen weglaten die we niet nodig hebben. Of selecteren wat we wel gebruiken.


* Zet hier een lijst met variabelen die we gaan gebruiken. Niet wat weg moet.

**Algemeen**.

 * ID
Measurementday
InstitutionID
CompletedDateTime
InstitutionForm_Type_Inst
InstitutionForm_Mod_Qualityframework
Ward_code
Type_Ward
G_pat_part
D_Age
D_ZZP_03
D_ZZP_type_VV_WithTreatment
D_ZZP_type_VV_WithoutTreatment

***Beleidsafspraken**.

 * D_QF_Prev_ACP
D_QF_ACP_resusication
D_QF_ACP_life_ending_treat
D_QF_ACP_hosp_adm
D_QF_ACP_other

***Medicatiefouten**.

 * QF_Ward_ErrorsDiscussed

***Medicatiereview**.

 * D_QF_Prev_MR2

***Aandacht voor eten en drinken***.

 * D_QF_Nut_foodpreferences
D_QF_Nut_foodpreferences_specific
D_QF_Nut_foodpreferences_offering
D_QF_Nut_foodpreferences_support
D_QF_Nut_foodpreferences_time
D_QF_Nut_foodpreferences_other

**Decubitus**.

 * D_QF_PU_Prev_cat2

**Casuïstiekbespreking**.

 * QF_Ward_PU_Discussed

**Continentieplan**.

 * D_QF_Inc_toiletingplan
D_QF_Inc_toiletingplan_preferences
D_QF_Inc_toiletingplan_independent
D_QF_Inc_toiletingplan_support
D_QF_Inc_toiletingplan_materials
D_QF_Inc_toiletingplan_other

***M&M rond vrijheid**.

 * D_QF_Rest_Prev
D_QF_Rest_mechanical
D_QF_Rest_physical
D_QF_Rest_pharmacologic
D_QF_Rest_psych
D_QF_Rest_electronic
D_QF_Rest_supervision
D_QF_Rest_seclusion
D_QF_Rest_other_Rest.




*** Selecteren van de variabelen die we nodig hebben. Andere variabelen/kolommen verdwijnen dus.
ADD FILES FILE *
 /KEEP=ID
    Measurementday
    InstitutionID
    IDresponsible
    CompletedDateTime
    InstitutionForm_Type_Inst
    InstitutionForm_Mod_Qualityframework
    Ward_code
    Type_Ward
    G_pat_part
    D_Age
    D_ZZP_03
    D_ZZP_type_VV_WithTreatment
    D_ZZP_type_VV_WithoutTreatment
    D_QF_Prev_ACP
    D_QF_ACP_resusication
    D_QF_ACP_life_ending_treat
    D_QF_ACP_hosp_adm
    D_QF_ACP_other
    QF_Ward_ErrorsDiscussed
    D_QF_Prev_MR2
    D_QF_Nut_foodpreferences
    D_QF_Nut_foodpreferences_specific
    D_QF_Nut_foodpreferences_offering
    D_QF_Nut_foodpreferences_support
    D_QF_Nut_foodpreferences_time
    D_QF_Nut_foodpreferences_other
    D_QF_PU_Prev_cat2
    QF_Ward_PU_Discussed
    D_QF_Inc_toiletingplan
    D_QF_Inc_toiletingplan_preferences
    D_QF_Inc_toiletingplan_independent
    D_QF_Inc_toiletingplan_support
    D_QF_Inc_toiletingplan_materials
    D_QF_Inc_toiletingplan_other
    D_QF_Rest_Prev
    D_QF_Rest_mechanical
    D_QF_Rest_physical
    D_QF_Rest_pharmacologic
    D_QF_Rest_psych
    D_QF_Rest_electronic
    D_QF_Rest_supervision
    D_QF_Rest_seclusion
    D_QF_Rest_other_Rest.

EXECUTE.






******* Rijen weghalen die we niet nodig hebben. Filter op type organisatie en/of type ward.
SHOW N.
FREQUENCIES InstitutionForm_Type_Inst.

* Selecteer alleen Nursing Home (9) en teams die meedoen aan QualityFramework.
SELECT IF InstitutionForm_Type_Inst = 9 AND InstitutionForm_Mod_Qualityframework = 1.
EXECUTE.

SHOW N.
FREQUENCIES InstitutionForm_Type_Inst InstitutionForm_Mod_Qualityframework.

VARIABLE LEVEL InstitutionID Type_ward (NOMINAL).
FREQUENCIES Type_Ward.



* Patienten verwijderen die D_ZZP_03 hebben.
* D_ZZP_03 heeft ook missende waarden. Dit zijn de patienten die niet mee doen (zie ook G_pat_part).
FREQUENCIES D_ZZP_03.
SELECT IF D_ZZP_03 = 0.
EXECUTE.
FREQUENCIES D_ZZP_03.




* Ward_code is waarschijnlijk niet uniek voor alle teams.
* Institution_ID plus Ward_code is dat waarschijnlijk wel.
string Ward_code_origineel (A40).
COMPUTE Ward_code_origineel = Ward_code.
COMPUTE Ward_code = CONCAT(LTRIM(STRING(InstitutionID, 'F11')), '_', IDresponsible, '_', Ward_code).
EXECUTE.

* LTRIM(STRING(Type_Ward, 'F11'))


* Type_ward.
VALUE LABELS Type_ward
901 "psychogeriatrische afdeling"
902 "somatische reactivering/herstelzorg"
903 "somatische verblijfsafdeling"
904 "geriatrische revalidatiezorg"
905 "verzorgingsafdeling"
906 "meerzorgafdeling"
907 "kleinschalig wonen - psychogeriatrie"
908 "kleinschalig wonen - somatiek"
909 "extramurale zorg"
910 "eerstelijnsverblijf"
998 "anders".




* Extramural care kan uit Type_ward. ---> dit moet nog worden aangepast want moeten toch alle subtypen van 9 (verpleeghuis) in de dataset houden.

FREQUENCIES Type_Ward.

* In Type_ward moeten sommige waarden worden samengevoegd.
* Schrijf hier wat moet worden samengevoegd.
****--> moet NIKS worden samengevoegd ****


* Maak ook een variabele met de afkorting voor type_ward.
COMPUTE afkorting_type_ward = type_ward.

VALUE LABELS afkorting_type_ward
901 "PG"
902 "SOMH"
903 "SOMV"
904 "GR"
905 "VZ"
906 "MZ"
907 "KS-PG"
908 "KS-SOM"
909 "EX"
910 "EV"
998 "AN".







* ...Discussed variabelen hebben 1 waarde per team (ja/nee of not applicable).
* Percentages per team moeten alleen de ja/nee's als noemer hebben.
* Werkt dit, via aggregate-->mean, als we not applicable op missing zetten?.
MISSING VALUES QF_Ward_ErrorsDiscussed QF_Ward_PU_Discussed (97).





* Gemiddelden voor type team (Type_ward) (KOR, PG) voor variabelen die op patientniveau zijn.
* Dit is de 'benchmark-informatie' van alle teams van een bepaald type.
DATASET ACTIVATE LPZ.
AGGREGATE
  /OUTFILE=* MODE=ADDVARIABLES
  /BREAK=Type_Ward
  /D_QF_Prev_ACP_mean_type_ward=MEAN(D_QF_Prev_ACP) 
  /D_QF_ACP_resusication_mean_type_ward=MEAN(D_QF_ACP_resusication) 
  /D_QF_ACP_life_ending_treat_mean_type_ward=MEAN(D_QF_ACP_life_ending_treat) 
  /D_QF_ACP_hosp_adm_mean_type_ward=MEAN(D_QF_ACP_hosp_adm) 
  /D_QF_ACP_other_mean_type_ward=MEAN(D_QF_ACP_other) 
  /D_QF_Prev_MR2_mean_type_ward=MEAN(D_QF_Prev_MR2) 
  /D_QF_Nut_foodpreferences_mean_type_ward=MEAN(D_QF_Nut_foodpreferences) 
  /D_QF_Nut_foodpreferences_specific_mean_type_ward=MEAN(D_QF_Nut_foodpreferences_specific) 
  /D_QF_Nut_foodpreferences_offering_mean_type_ward=MEAN(D_QF_Nut_foodpreferences_offering) 
  /D_QF_Nut_foodpreferences_support_mean_type_ward=MEAN(D_QF_Nut_foodpreferences_support) 
  /D_QF_Nut_foodpreferences_time_mean_type_ward=MEAN(D_QF_Nut_foodpreferences_time) 
  /D_QF_Nut_foodpreferences_other_mean_type_ward=MEAN(D_QF_Nut_foodpreferences_other) 
  /D_QF_PU_Prev_cat2_mean_type_ward=MEAN(D_QF_PU_Prev_cat2) 
  /D_QF_Inc_toiletingplan_mean_type_ward=MEAN(D_QF_Inc_toiletingplan) 
  /D_QF_Inc_toiletingplan_preferences_mean_type_ward=MEAN(D_QF_Inc_toiletingplan_preferences) 
  /D_QF_Inc_toiletingplan_independent_mean_type_ward=MEAN(D_QF_Inc_toiletingplan_independent) 
  /D_QF_Inc_toiletingplan_support_mean_type_ward=MEAN(D_QF_Inc_toiletingplan_support) 
  /D_QF_Inc_toiletingplan_materials_mean_type_ward=MEAN(D_QF_Inc_toiletingplan_materials) 
  /D_QF_Inc_toiletingplan_other_mean_type_ward=MEAN(D_QF_Inc_toiletingplan_other) 
  /D_QF_Rest_Prev_mean_type_ward=MEAN(D_QF_Rest_Prev) 
  /D_QF_Rest_mechanical_mean_type_ward=MEAN(D_QF_Rest_mechanical) 
  /D_QF_Rest_physical_mean_type_ward=MEAN(D_QF_Rest_physical) 
  /D_QF_Rest_pharmacologic_mean_type_ward=MEAN(D_QF_Rest_pharmacologic) 
  /D_QF_Rest_psych_mean_type_ward=MEAN(D_QF_Rest_psych) 
  /D_QF_Rest_electronic_mean_type_ward=MEAN(D_QF_Rest_electronic) 
  /D_QF_Rest_supervision_mean_type_ward=MEAN(D_QF_Rest_supervision) 
  /D_QF_Rest_seclusion_mean_type_ward=MEAN(D_QF_Rest_seclusion) 
  /D_QF_Rest_other_Rest_mean_type_ward=MEAN(D_QF_Rest_other_Rest)
  /aantal_patienten_per_ward_type=N.



* face validity check.
CTABLES
  /VLABELS VARIABLES=Type_Ward Ward_code D_QF_Nut_foodpreferences_mean_type_ward 
    D_QF_Nut_foodpreferences_specific_mean_type_ward D_QF_Nut_foodpreferences_offering_mean_type_ward 
    D_QF_Nut_foodpreferences_support_mean_type_ward D_QF_Nut_foodpreferences_time_mean_type_ward 
    D_QF_Nut_foodpreferences_other_mean_type_ward D_QF_PU_Prev_cat2_mean_type_ward 
    D_QF_Inc_toiletingplan_mean_type_ward D_QF_Inc_toiletingplan_preferences_mean_type_ward 
    DISPLAY=LABEL
  /TABLE Type_Ward [C] > Ward_code [C] BY D_QF_Nut_foodpreferences_mean_type_ward [S][MEAN] + 
    D_QF_Nut_foodpreferences_specific_mean_type_ward [S][MEAN] + 
    D_QF_Nut_foodpreferences_offering_mean_type_ward [S][MEAN] + 
    D_QF_Nut_foodpreferences_support_mean_type_ward [S][MEAN] + 
    D_QF_Nut_foodpreferences_time_mean_type_ward [S][MEAN] + 
    D_QF_Nut_foodpreferences_other_mean_type_ward [S][MEAN] + D_QF_PU_Prev_cat2_mean_type_ward 
    [S][MEAN] + D_QF_Inc_toiletingplan_mean_type_ward [S][MEAN] + 
    D_QF_Inc_toiletingplan_preferences_mean_type_ward [S][MEAN]
  /CATEGORIES VARIABLES=Type_Ward Ward_code ORDER=A KEY=VALUE EMPTY=EXCLUDE
  /CRITERIA CILEVEL=95.





* Gemiddelden per team (Ward_code) uitrekenen (voor alle relevante variabelen).
DATASET DECLARE LPZ_teams.
AGGREGATE
  /OUTFILE='LPZ_teams'
  /BREAK=Ward_code
  /Measurementday=MAX(Measurementday) 
  /InstitutionID=MAX(InstitutionID) 
  /InstitutionForm_Type_Inst=MAX(InstitutionForm_Type_Inst) 
  /InstitutionForm_Mod_Qualityframework=MAX(InstitutionForm_Mod_Qualityframework) 
  /Type_Ward=MAX(Type_Ward) 
  /D_Age_mean_team=MEAN(D_Age) 
  /D_QF_Prev_ACP_mean_team=MEAN(D_QF_Prev_ACP) 
  /D_QF_ACP_resusication_mean_team=MEAN(D_QF_ACP_resusication) 
  /D_QF_ACP_life_ending_treat_mean_team=MEAN(D_QF_ACP_life_ending_treat) 
  /D_QF_ACP_hosp_adm_mean_team=MEAN(D_QF_ACP_hosp_adm) 
  /D_QF_ACP_other_mean_team=MEAN(D_QF_ACP_other) 
  /D_QF_Prev_MR2_mean_team=MEAN(D_QF_Prev_MR2) 
  /D_QF_Nut_foodpreferences_mean_team=MEAN(D_QF_Nut_foodpreferences) 
  /D_QF_Nut_foodpreferences_specific_mean_team=MEAN(D_QF_Nut_foodpreferences_specific) 
  /D_QF_Nut_foodpreferences_offering_mean_team=MEAN(D_QF_Nut_foodpreferences_offering) 
  /D_QF_Nut_foodpreferences_support_mean_team=MEAN(D_QF_Nut_foodpreferences_support) 
  /D_QF_Nut_foodpreferences_time_mean_team=MEAN(D_QF_Nut_foodpreferences_time) 
  /D_QF_Nut_foodpreferences_other_mean_team=MEAN(D_QF_Nut_foodpreferences_other) 
  /D_QF_PU_Prev_cat2_mean_team=MEAN(D_QF_PU_Prev_cat2) 
  /D_QF_Inc_toiletingplan_mean_team=MEAN(D_QF_Inc_toiletingplan) 
  /D_QF_Inc_toiletingplan_preferences_mean_team=MEAN(D_QF_Inc_toiletingplan_preferences) 
  /D_QF_Inc_toiletingplan_independent_mean_team=MEAN(D_QF_Inc_toiletingplan_independent) 
  /D_QF_Inc_toiletingplan_support_mean_team=MEAN(D_QF_Inc_toiletingplan_support) 
  /D_QF_Inc_toiletingplan_materials_mean_team=MEAN(D_QF_Inc_toiletingplan_materials) 
  /D_QF_Inc_toiletingplan_other_mean_team=MEAN(D_QF_Inc_toiletingplan_other) 
  /D_QF_Rest_Prev_mean_team=MEAN(D_QF_Rest_Prev) 
  /D_QF_Rest_mechanical_mean_team=MEAN(D_QF_Rest_mechanical) 
  /D_QF_Rest_physical_mean_team=MEAN(D_QF_Rest_physical) 
  /D_QF_Rest_pharmacologic_mean_team=MEAN(D_QF_Rest_pharmacologic) 
  /D_QF_Rest_psych_mean_team=MEAN(D_QF_Rest_psych) 
  /D_QF_Rest_electronic_mean_team=MEAN(D_QF_Rest_electronic) 
  /D_QF_Rest_supervision_mean_team=MEAN(D_QF_Rest_supervision) 
  /D_QF_Rest_seclusion_mean_team=MEAN(D_QF_Rest_seclusion) 
  /D_QF_Rest_other_Rest_mean_team=MEAN(D_QF_Rest_other_Rest) 
  /QF_Ward_ErrorsDiscussed=MEAN(QF_Ward_ErrorsDiscussed) 
  /QF_Ward_PU_Discussed=MEAN(QF_Ward_PU_Discussed) 
  /D_QF_Prev_ACP_mean_type_ward=MEAN(D_QF_Prev_ACP_mean_type_ward) 
  /D_QF_ACP_resusication_mean_type_ward=MEAN(D_QF_ACP_resusication_mean_type_ward) 
  /D_QF_ACP_life_ending_treat_mean_type_ward=MEAN(D_QF_ACP_life_ending_treat_mean_type_ward) 
  /D_QF_ACP_hosp_adm_mean_type_ward=MEAN(D_QF_ACP_hosp_adm_mean_type_ward) 
  /D_QF_ACP_other_mean_type_ward=MEAN(D_QF_ACP_other_mean_type_ward) 
  /D_QF_Prev_MR2_mean_type_ward=MEAN(D_QF_Prev_MR2_mean_type_ward) 
  /D_QF_Nut_foodpreferences_mean_type_ward=MEAN(D_QF_Nut_foodpreferences_mean_type_ward) 
  /D_QF_Nut_foodpreferences_specific_mean_type_ward=
    MEAN(D_QF_Nut_foodpreferences_specific_mean_type_ward) 
  /D_QF_Nut_foodpreferences_offering_mean_type_ward=
    MEAN(D_QF_Nut_foodpreferences_offering_mean_type_ward) 
  /D_QF_Nut_foodpreferences_support_mean_type_ward=
    MEAN(D_QF_Nut_foodpreferences_support_mean_type_ward) 
  /D_QF_Nut_foodpreferences_time_mean_type_ward=
    MEAN(D_QF_Nut_foodpreferences_time_mean_type_ward) 
  /D_QF_Nut_foodpreferences_other_mean_type_ward=
    MEAN(D_QF_Nut_foodpreferences_other_mean_type_ward) 
  /D_QF_PU_Prev_cat2_mean_type_ward=MEAN(D_QF_PU_Prev_cat2_mean_type_ward) 
  /D_QF_Inc_toiletingplan_mean_type_ward=MEAN(D_QF_Inc_toiletingplan_mean_type_ward) 
  /D_QF_Inc_toiletingplan_preferences_mean_type_ward=
    MEAN(D_QF_Inc_toiletingplan_preferences_mean_type_ward) 
  /D_QF_Inc_toiletingplan_independent_mean_type_ward=
    MEAN(D_QF_Inc_toiletingplan_independent_mean_type_ward) 
  /D_QF_Inc_toiletingplan_support_mean_type_ward=
    MEAN(D_QF_Inc_toiletingplan_support_mean_type_ward) 
  /D_QF_Inc_toiletingplan_materials_mean_type_ward=
    MEAN(D_QF_Inc_toiletingplan_materials_mean_type_ward) 
  /D_QF_Inc_toiletingplan_other_mean_type_ward=
    MEAN(D_QF_Inc_toiletingplan_other_mean_type_ward) 
  /D_QF_Rest_Prev_mean_type_ward=MEAN(D_QF_Rest_Prev_mean_type_ward) 
  /D_QF_Rest_mechanical_mean_type_ward=MEAN(D_QF_Rest_mechanical_mean_type_ward) 
  /D_QF_Rest_physical_mean_type_ward=MEAN(D_QF_Rest_physical_mean_type_ward) 
  /D_QF_Rest_pharmacologic_mean_type_ward=MEAN(D_QF_Rest_pharmacologic_mean_type_ward) 
  /D_QF_Rest_psych_mean_type_ward=MEAN(D_QF_Rest_psych_mean_type_ward) 
  /D_QF_Rest_electronic_mean_type_ward=MEAN(D_QF_Rest_electronic_mean_type_ward) 
  /D_QF_Rest_supervision_mean_type_ward=MEAN(D_QF_Rest_supervision_mean_type_ward) 
  /D_QF_Rest_seclusion_mean_type_ward=MEAN(D_QF_Rest_seclusion_mean_type_ward) 
  /D_QF_Rest_other_Rest_mean_type_ward=MEAN(D_QF_Rest_other_Rest_mean_type_ward) 
  /aantal_patienten_per_ward_type=MEAN(aantal_patienten_per_ward_type)
  /aantal_patienten_in_team=N
  /aantal_patienten_in_team_met_behandeling=SUM(D_ZZP_type_VV_WithTreatment).

DATASET ACTIVATE LPZ_teams.

* We merken op dat Ward_type niet consistent wordt ingevuld binnen teams.
* Soms worden er 2 ward_typen gebruikt voor 1 ward_code binnen een institution.
* Hoe kan dit? Mogelijke verklaringen:
* Team heeft 2 formulieren ingevuld met conflicterende ward_typen. Vervolgvraag is dan: Hoe komt de ward_type informatie op patientniveau in de data terecht?
* Vult zorgverlener alleen een ward_code in wanneer de patienten-vragenlijst wordt ingevuld? Of vult zorgverlener ward_type in?.
* Ward_code was niet uniek, en is hopelijk uniek binnen institution, maar ook dit weten we niet 100% zeker. Kan dit veroorzaakt worden door niet-unieke ward_codes?.

* Het valt op dat dit probleem vaker voor lijkt te komen bij teams met nummers 1, 2, 3 en minder bij 'hoge' nummers.
* Tel eens het aantal unieke ward_types per ward_code.

* OPGELOST...HET LAG AAN LOCATIE (IDResponsible). Die is nu toegevoegd aan Ward_code, waardoor Ward_code uniek is.

 * DATASET ACTIVATE LPZ.
 * DATASET DECLARE per_team_per_type.
 * AGGREGATE
  /OUTFILE='per_team_per_type'
  /BREAK=Ward_code Type_Ward
  /aantal_patienten_in_team_in_type=N.

 * DATASET ACTIVATE per_team_per_type.
 * DATASET DECLARE ntypes_per_team.
 * AGGREGATE
  /OUTFILE='ntypes_per_team'
  /BREAK=Ward_code
  /aantal_ward_types_per_team=N
  .
 * DATASET ACTIVATE ntypes_per_team.

 * DATASET CLOSE ntypes_per_team.
 * DATASET CLOSE per_team_per_type.






* Gemiddelden voor type team voor die variabelen die op teamniveau zijn.
* QF_Ward_ErrorsDiscussed
* QF_Ward_PU_Discussed.
DATASET ACTIVATE LPZ_teams.
AGGREGATE
  /OUTFILE=* MODE=ADDVARIABLES
  /BREAK=Type_Ward
  /QF_Ward_ErrorsDiscussed_mean_type_ward=MEAN(QF_Ward_ErrorsDiscussed) 
  /QF_Ward_PU_Discussed_mean_type_ward=MEAN(QF_Ward_PU_Discussed).


* Face validity check voor de ...discussed variabelen.
* Edit wel eerst de Type_ward value labels, want ctables probeert voor elk label een rij te maken, ongeacht of er data zijn.
CTABLES
  /VLABELS VARIABLES=Type_Ward Ward_code QF_Ward_ErrorsDiscussed QF_Ward_PU_Discussed 
    QF_Ward_ErrorsDiscussed_mean_type_ward QF_Ward_PU_Discussed_mean_type_ward DISPLAY=LABEL
  /TABLE Type_Ward > Ward_code BY QF_Ward_ErrorsDiscussed [MEAN] + QF_Ward_PU_Discussed [MEAN] + 
    QF_Ward_ErrorsDiscussed_mean_type_ward [MEAN] + QF_Ward_PU_Discussed_mean_type_ward [MEAN]
  /CATEGORIES VARIABLES=Type_Ward ORDER=A KEY=VALUE EMPTY=INCLUDE
  /CATEGORIES VARIABLES=Ward_code ORDER=A KEY=VALUE EMPTY=EXCLUDE
  /CRITERIA CILEVEL=95.




*** Aandacht voor missende waarden ***.

* Teams met teveel missende waarden kunnen verwijderd worden.
MVA D_QF_Prev_ACP_mean_team TO QF_Ward_PU_Discussed.

* en aantal missing per rij.
compute missing_per_rij = nmiss(D_QF_Prev_ACP_mean_team TO QF_Ward_PU_Discussed).
execute.

COMPUTE MR_Missing = MISSING(D_QF_Prev_MR2_mean_team).
CROSSTABS
  /TABLES=MR_Missing BY Type_Ward
  /FORMAT=AVALUE TABLES
  /CELLS=COUNT
  /COUNT ROUND CELL.

COMPUTE ACP_ISNUL= D_QF_Prev_ACP_mean_team = 0.
COMPUTE Errors_Discussed_Missing = MISSING(QF_Ward_ErrorsDiscussed).
COMPUTE PU_Discussed_Missing = MISSING(QF_Ward_PU_Discussed).
COMPUTE MAX_MISSING_ALLOWED = MR_Missing + ACP_ISNUL * 4 + Errors_Discussed_Missing + PU_Discussed_Missing.
EXECUTE.

DO IF missing_per_rij > MAX_MISSING_ALLOWED.
COMPUTE teveel_missing = 1.
ELSE.
COMPUTE teveel_missing = 0.
END IF.
VALUE LABELS teveel_missing
1 "PAS OP, er zijn meer missende waarden dan toegestaan!"
0 "Alles ok".
FREQUENCIES teveel_missing.

* Als D_ZZP_type_VV_WithTreatment = Nee, dan kan D_QF_Prev_MR2 missing zijn.




SAVE OUTFILE='Data\LPZ_teamdata.sav'
  /COMPRESSED.


SAVE TRANSLATE OUTFILE='Data\LPZ_teamdata.csv'
  /TYPE=CSV
  /ENCODING='UTF8'
  /MAP
  /REPLACE
  /FIELDNAMES
  /CELLS=LABELS.



* Bestand op teamniveau opslaan.


DATASET CLOSE LPZ.
