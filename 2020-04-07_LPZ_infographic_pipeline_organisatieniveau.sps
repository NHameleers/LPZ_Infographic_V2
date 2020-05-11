﻿* Encoding: UTF-8.


OUTPUT NEW.

CD "E:\2020_01_06_Selectie_backup_I-schijf\LPZ\Infographic_2.0".

* TODO: Als je de syntax wil runnen/gebruiken, dan bestandsnaam aanpassen.
GET
  FILE='NL2019NOV_total_new.sav'.
DATASET NAME LPZ WINDOW=FRONT.


* Opmerking: Een deel van deze syntax is niet relevant voor organisatieniveau, maar is blijven
*  staan uit de syntax op teamniveau. Deze stukken kunnen echter geen kwaad op organisatieniveau.



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
    Coordinator
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
    QF_ACP_no_agreements
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
 * FREQUENCIES D_ZZP_03.
 * SELECT IF D_ZZP_03 = 0.
 * EXECUTE.
 * FREQUENCIES D_ZZP_03.


* Ward_code is waarschijnlijk niet uniek voor alle teams.
* Institution_ID plus Ward_code is dat waarschijnlijk wel.
 * string Ward_code_origineel (A40).
 * COMPUTE Ward_code_origineel = Ward_code.
 * COMPUTE Ward_code = CONCAT(LTRIM(STRING(InstitutionID, 'F11')), '_', IDresponsible, '_', Ward_code).
 * EXECUTE.


* Is Coordinator_IDresponsible_Ward_code ook een unieke teamcode?.
 * CTABLES
  /VLABELS VARIABLES=Coordinator InstitutionID DISPLAY=LABEL
  /TABLE Coordinator > InstitutionID [COUNT F40.0]
  /CATEGORIES VARIABLES=Coordinator InstitutionID ORDER=A KEY=VALUE EMPTY=EXCLUDE
  /CRITERIA CILEVEL=95.

* Custom Tables.
 * CTABLES
  /VLABELS VARIABLES=InstitutionID Coordinator DISPLAY=LABEL
  /TABLE InstitutionID [C] > Coordinator [C][COUNT F40.0]
  /CATEGORIES VARIABLES=InstitutionID Coordinator ORDER=A KEY=VALUE EMPTY=EXCLUDE
  /CRITERIA CILEVEL=95.

* Zo te zien is er geen verschil, en is Coordinator gewoon een andere code voor InstitutionID en dus voor organisatie.











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
902 "Herstel"
903 "Som"
904 "GRZ"
905 "VZ"
906 "Meerz"
907 "PG/kl"
908 "Som/kl"
909 "Extra"
910 "ELV"
998 "overig".

EXECUTE.



FREQUENCIES QF_Ward_ErrorsDiscussed QF_Ward_PU_Discussed.

* ...Discussed variabelen hebben 1 waarde per team (ja/nee of not applicable).
* Percentages per team moeten alleen de ja/nee's als noemer hebben.
* Werkt dit, via aggregate-->mean, als we not applicable op missing zetten?.
MISSING VALUES QF_Ward_ErrorsDiscussed QF_Ward_PU_Discussed (97).




* TOEGEVOEGD OM CIJFERS VOLGENS DASHBOARD-METHODE TE BEREKENEN.
* De noemer voor een aantal variabelen (bijv ACP) moet het totale aantal patienten zijn, ipv het aantal patienten die op zijn minst bij een van de categorieen een ja heeft staan.
* Volgens mij is een simpele en dynamische manier om dit te bereiken om de missende waarden te vervangen door nullen, zodat deze worden meegeteld bij het berekenen van het gemiddelde.
DO IF D_QF_Prev_ACP = 0.
COMPUTE D_QF_ACP_resusication =0.
COMPUTE D_QF_ACP_life_ending_treat = 0.
COMPUTE D_QF_ACP_hosp_adm = 0.
COMPUTE D_QF_ACP_other = 0.
END IF.
EXECUTE.




* EDITED VOOR ORGANISATIE.
* Gemiddelde van alle organisaties samen voor variabelen die op patientniveau zijn.
* Dit is de 'benchmark-informatie' van alle organisaties.
DATASET ACTIVATE LPZ.
AGGREGATE
  /OUTFILE=* MODE=ADDVARIABLES
  /BREAK= 
  /D_QF_Prev_ACP_mean_van_ALLE_orgs=MEAN(D_QF_Prev_ACP) 
  /D_QF_ACP_resusication_mean_van_ALLE_orgs=MEAN(D_QF_ACP_resusication) 
  /D_QF_ACP_life_ending_treat_mean_van_ALLE_orgs=MEAN(D_QF_ACP_life_ending_treat) 
  /D_QF_ACP_hosp_adm_mean_van_ALLE_orgs=MEAN(D_QF_ACP_hosp_adm) 
  /D_QF_ACP_other_mean_van_ALLE_orgs=MEAN(D_QF_ACP_other) 
  /D_QF_Prev_MR2_mean_van_ALLE_orgs=MEAN(D_QF_Prev_MR2) 
  /D_QF_Nut_foodpreferences_mean_van_ALLE_orgs=MEAN(D_QF_Nut_foodpreferences) 
  /D_QF_Nut_foodpreferences_specific_mean_van_ALLE_orgs=MEAN(D_QF_Nut_foodpreferences_specific) 
  /D_QF_Nut_foodpreferences_offering_mean_van_ALLE_orgs=MEAN(D_QF_Nut_foodpreferences_offering) 
  /D_QF_Nut_foodpreferences_support_mean_van_ALLE_orgs=MEAN(D_QF_Nut_foodpreferences_support) 
  /D_QF_Nut_foodpreferences_time_mean_van_ALLE_orgs=MEAN(D_QF_Nut_foodpreferences_time) 
  /D_QF_Nut_foodpreferences_other_mean_van_ALLE_orgs=MEAN(D_QF_Nut_foodpreferences_other) 
  /D_QF_PU_Prev_cat2_mean_van_ALLE_orgs=MEAN(D_QF_PU_Prev_cat2) 
  /D_QF_Inc_toiletingplan_mean_van_ALLE_orgs=MEAN(D_QF_Inc_toiletingplan) 
  /D_QF_Inc_toiletingplan_preferences_mean_van_ALLE_orgs=MEAN(D_QF_Inc_toiletingplan_preferences) 
  /D_QF_Inc_toiletingplan_independent_mean_van_ALLE_orgs=MEAN(D_QF_Inc_toiletingplan_independent) 
  /D_QF_Inc_toiletingplan_support_mean_van_ALLE_orgs=MEAN(D_QF_Inc_toiletingplan_support) 
  /D_QF_Inc_toiletingplan_materials_mean_van_ALLE_orgs=MEAN(D_QF_Inc_toiletingplan_materials) 
  /D_QF_Inc_toiletingplan_other_mean_van_ALLE_orgs=MEAN(D_QF_Inc_toiletingplan_other) 
  /D_QF_Rest_Prev_mean_van_ALLE_orgs=MEAN(D_QF_Rest_Prev) 
  /D_QF_Rest_mechanical_mean_van_ALLE_orgs=MEAN(D_QF_Rest_mechanical) 
  /D_QF_Rest_physical_mean_van_ALLE_orgs=MEAN(D_QF_Rest_physical) 
  /D_QF_Rest_pharmacologic_mean_van_ALLE_orgs=MEAN(D_QF_Rest_pharmacologic) 
  /D_QF_Rest_psych_mean_van_ALLE_orgs=MEAN(D_QF_Rest_psych) 
  /D_QF_Rest_electronic_mean_van_ALLE_orgs=MEAN(D_QF_Rest_electronic) 
  /D_QF_Rest_supervision_mean_van_ALLE_orgs=MEAN(D_QF_Rest_supervision) 
  /D_QF_Rest_seclusion_mean_van_ALLE_orgs=MEAN(D_QF_Rest_seclusion) 
  /D_QF_Rest_other_Rest_mean_van_ALLE_orgs=MEAN(D_QF_Rest_other_Rest)
  /aantal_patienten_totaal=N.


* Face validity check steekproef.
CTABLES
  /VLABELS VARIABLES=InstitutionID IDresponsible 
    D_QF_Inc_toiletingplan_independent_mean_van_ALLE_orgs 
    D_QF_Inc_toiletingplan_materials_mean_van_ALLE_orgs D_QF_Rest_supervision_mean_van_ALLE_orgs 
    DISPLAY=LABEL
  /TABLE InstitutionID [C] > IDresponsible [C] BY 
    D_QF_Inc_toiletingplan_independent_mean_van_ALLE_orgs [MEAN] + 
    D_QF_Inc_toiletingplan_materials_mean_van_ALLE_orgs [MEAN] + 
    D_QF_Rest_supervision_mean_van_ALLE_orgs [MEAN]
  /CATEGORIES VARIABLES=InstitutionID IDresponsible ORDER=A KEY=VALUE EMPTY=EXCLUDE
  /CRITERIA CILEVEL=95.



************ Mini exploratie ************.
 * DATASET COPY lpz_copy.
 * DATASET ACTIVATE lpz_copy.
 * FREQUENCIES D_QF_Prev_ACP.
 * do if D_QF_Prev_ACP = 0.
 * recode D_QF_ACP_resusication
D_QF_ACP_life_ending_treat
D_QF_ACP_hosp_adm
D_QF_ACP_other (sysmis=0).
 * EXECUTE.
 * end if.
 * DATASET DECLARE test_aggvars.
 * AGGREGATE
 /outfile='test_aggvars'
 /break=
  /D_QF_ACP_resusication_mean_van_ALLE_orgs=MEAN(D_QF_ACP_resusication) 
  /D_QF_ACP_life_ending_treat_mean_van_ALLE_orgs=MEAN(D_QF_ACP_life_ending_treat) 
  /D_QF_ACP_hosp_adm_mean_van_ALLE_orgs=MEAN(D_QF_ACP_hosp_adm) 
  /D_QF_ACP_other_mean_van_ALLE_orgs=MEAN(D_QF_ACP_other).
 * DATASET ACTIVATE test_aggvars.

 * DATASET CLOSE LPZ_COPY.
 * DATASET CLOSE test_aggvars.
 * DATASET ACTIVATE LPZ.
*******************************************.





* Gemiddelden per organisatie (InstitutionID) uitrekenen (voor alle relevante variabelen).
DATASET DECLARE LPZ_organisaties.
AGGREGATE
  /OUTFILE='LPZ_organisaties'
  /BREAK=InstitutionID
  /Measurementday=MAX(Measurementday) 
  /Coordinator=MAX(Coordinator)
  /InstitutionForm_Type_Inst=MAX(InstitutionForm_Type_Inst) 
  /InstitutionForm_Mod_Qualityframework=MAX(InstitutionForm_Mod_Qualityframework) 
  /D_Age_mean_organisatie=MEAN(D_Age) 
  /D_QF_Prev_ACP_mean_organisatie=MEAN(D_QF_Prev_ACP) 
  /D_QF_ACP_resusication_mean_organisatie=MEAN(D_QF_ACP_resusication) 
  /D_QF_ACP_life_ending_treat_mean_organisatie=MEAN(D_QF_ACP_life_ending_treat) 
  /D_QF_ACP_hosp_adm_mean_organisatie=MEAN(D_QF_ACP_hosp_adm) 
  /D_QF_ACP_other_mean_organisatie=MEAN(D_QF_ACP_other) 
  /D_QF_Prev_MR2_mean_organisatie=MEAN(D_QF_Prev_MR2) 
  /D_QF_Nut_foodpreferences_mean_organisatie=MEAN(D_QF_Nut_foodpreferences) 
  /D_QF_Nut_foodpreferences_specific_mean_organisatie=MEAN(D_QF_Nut_foodpreferences_specific) 
  /D_QF_Nut_foodpreferences_offering_mean_organisatie=MEAN(D_QF_Nut_foodpreferences_offering) 
  /D_QF_Nut_foodpreferences_support_mean_organisatie=MEAN(D_QF_Nut_foodpreferences_support) 
  /D_QF_Nut_foodpreferences_time_mean_organisatie=MEAN(D_QF_Nut_foodpreferences_time) 
  /D_QF_Nut_foodpreferences_other_mean_organisatie=MEAN(D_QF_Nut_foodpreferences_other) 
  /D_QF_PU_Prev_cat2_mean_organisatie=MEAN(D_QF_PU_Prev_cat2) 
  /D_QF_Inc_toiletingplan_mean_organisatie=MEAN(D_QF_Inc_toiletingplan) 
  /D_QF_Inc_toiletingplan_preferences_mean_organisatie=MEAN(D_QF_Inc_toiletingplan_preferences) 
  /D_QF_Inc_toiletingplan_independent_mean_organisatie=MEAN(D_QF_Inc_toiletingplan_independent) 
  /D_QF_Inc_toiletingplan_support_mean_organisatie=MEAN(D_QF_Inc_toiletingplan_support) 
  /D_QF_Inc_toiletingplan_materials_mean_organisatie=MEAN(D_QF_Inc_toiletingplan_materials) 
  /D_QF_Inc_toiletingplan_other_mean_organisatie=MEAN(D_QF_Inc_toiletingplan_other) 
  /D_QF_Rest_Prev_mean_organisatie=MEAN(D_QF_Rest_Prev) 
  /D_QF_Rest_mechanical_mean_organisatie=MEAN(D_QF_Rest_mechanical) 
  /D_QF_Rest_physical_mean_organisatie=MEAN(D_QF_Rest_physical) 
  /D_QF_Rest_pharmacologic_mean_organisatie=MEAN(D_QF_Rest_pharmacologic) 
  /D_QF_Rest_psych_mean_organisatie=MEAN(D_QF_Rest_psych) 
  /D_QF_Rest_electronic_mean_organisatie=MEAN(D_QF_Rest_electronic) 
  /D_QF_Rest_supervision_mean_organisatie=MEAN(D_QF_Rest_supervision) 
  /D_QF_Rest_seclusion_mean_organisatie=MEAN(D_QF_Rest_seclusion) 
  /D_QF_Rest_other_Rest_mean_organisatie=MEAN(D_QF_Rest_other_Rest)
  /D_QF_Prev_ACP_mean_van_ALLE_orgs=MEAN(D_QF_Prev_ACP_mean_van_ALLE_orgs) 
  /D_QF_ACP_resusication_mean_van_ALLE_orgs=MEAN(D_QF_ACP_resusication_mean_van_ALLE_orgs) 
  /D_QF_ACP_life_ending_treat_mean_van_ALLE_orgs=MEAN(D_QF_ACP_life_ending_treat_mean_van_ALLE_orgs) 
  /D_QF_ACP_hosp_adm_mean_van_ALLE_orgs=MEAN(D_QF_ACP_hosp_adm_mean_van_ALLE_orgs) 
  /D_QF_ACP_other_mean_van_ALLE_orgs=MEAN(D_QF_ACP_other_mean_van_ALLE_orgs) 
  /D_QF_Prev_MR2_mean_van_ALLE_orgs=MEAN(D_QF_Prev_MR2_mean_van_ALLE_orgs) 
  /D_QF_Nut_foodpreferences_mean_van_ALLE_orgs=MEAN(D_QF_Nut_foodpreferences_mean_van_ALLE_orgs) 
  /D_QF_Nut_foodpreferences_specific_mean_van_ALLE_orgs=
    MEAN(D_QF_Nut_foodpreferences_specific_mean_van_ALLE_orgs) 
  /D_QF_Nut_foodpreferences_offering_mean_van_ALLE_orgs=
    MEAN(D_QF_Nut_foodpreferences_offering_mean_van_ALLE_orgs) 
  /D_QF_Nut_foodpreferences_support_mean_van_ALLE_orgs=
    MEAN(D_QF_Nut_foodpreferences_support_mean_van_ALLE_orgs) 
  /D_QF_Nut_foodpreferences_time_mean_van_ALLE_orgs=
    MEAN(D_QF_Nut_foodpreferences_time_mean_van_ALLE_orgs) 
  /D_QF_Nut_foodpreferences_other_mean_van_ALLE_orgs=
    MEAN(D_QF_Nut_foodpreferences_other_mean_van_ALLE_orgs) 
  /D_QF_PU_Prev_cat2_mean_van_ALLE_orgs=MEAN(D_QF_PU_Prev_cat2_mean_van_ALLE_orgs) 
  /D_QF_Inc_toiletingplan_mean_van_ALLE_orgs=MEAN(D_QF_Inc_toiletingplan_mean_van_ALLE_orgs) 
  /D_QF_Inc_toiletingplan_preferences_mean_van_ALLE_orgs=
    MEAN(D_QF_Inc_toiletingplan_preferences_mean_van_ALLE_orgs) 
  /D_QF_Inc_toiletingplan_independent_mean_van_ALLE_orgs=
    MEAN(D_QF_Inc_toiletingplan_independent_mean_van_ALLE_orgs) 
  /D_QF_Inc_toiletingplan_support_mean_van_ALLE_orgs=
    MEAN(D_QF_Inc_toiletingplan_support_mean_van_ALLE_orgs) 
  /D_QF_Inc_toiletingplan_materials_mean_van_ALLE_orgs=
    MEAN(D_QF_Inc_toiletingplan_materials_mean_van_ALLE_orgs) 
  /D_QF_Inc_toiletingplan_other_mean_van_ALLE_orgs=
    MEAN(D_QF_Inc_toiletingplan_other_mean_van_ALLE_orgs) 
  /D_QF_Rest_Prev_mean_van_ALLE_orgs=MEAN(D_QF_Rest_Prev_mean_van_ALLE_orgs) 
  /D_QF_Rest_mechanical_mean_van_ALLE_orgs=MEAN(D_QF_Rest_mechanical_mean_van_ALLE_orgs) 
  /D_QF_Rest_physical_mean_van_ALLE_orgs=MEAN(D_QF_Rest_physical_mean_van_ALLE_orgs) 
  /D_QF_Rest_pharmacologic_mean_van_ALLE_orgs=MEAN(D_QF_Rest_pharmacologic_mean_van_ALLE_orgs) 
  /D_QF_Rest_psych_mean_van_ALLE_orgs=MEAN(D_QF_Rest_psych_mean_van_ALLE_orgs) 
  /D_QF_Rest_electronic_mean_van_ALLE_orgs=MEAN(D_QF_Rest_electronic_mean_van_ALLE_orgs) 
  /D_QF_Rest_supervision_mean_van_ALLE_orgs=MEAN(D_QF_Rest_supervision_mean_van_ALLE_orgs) 
  /D_QF_Rest_seclusion_mean_van_ALLE_orgs=MEAN(D_QF_Rest_seclusion_mean_van_ALLE_orgs) 
  /D_QF_Rest_other_Rest_mean_van_ALLE_orgs=MEAN(D_QF_Rest_other_Rest_mean_van_ALLE_orgs) 
  /aantal_patienten_totaal=MEAN(aantal_patienten_totaal)
  /aantal_patienten_in_organisatie=N
  /aantal_patienten_in_organisatie_met_behandeling=SUM(D_ZZP_type_VV_WithTreatment).

DATASET ACTIVATE LPZ_organisaties.

* Face validity check. Mean van locatie vs mean van org. Aantal van org vs aantal van locatie.
DATASET ACTIVATE LPZ_organisaties.
* Custom Tables.
CTABLES
  /VLABELS VARIABLES=InstitutionID D_QF_Prev_ACP_mean_organisatie 
    D_QF_Nut_foodpreferences_mean_organisatie D_QF_Inc_toiletingplan_mean_organisatie 
    D_QF_Prev_ACP_mean_van_ALLE_orgs D_QF_Nut_foodpreferences_mean_van_ALLE_orgs 
    D_QF_Inc_toiletingplan_mean_van_ALLE_orgs aantal_patienten_totaal aantal_patienten_in_organisatie 
    aantal_patienten_in_organisatie_met_behandeling 
    DISPLAY=LABEL
  /TABLE InstitutionID BY D_QF_Prev_ACP_mean_organisatie [MEAN] + 
    D_QF_Nut_foodpreferences_mean_organisatie [MEAN] + D_QF_Inc_toiletingplan_mean_organisatie [MEAN] + 
    D_QF_Prev_ACP_mean_van_ALLE_orgs [MEAN] + D_QF_Nut_foodpreferences_mean_van_ALLE_orgs [MEAN] + 
    D_QF_Inc_toiletingplan_mean_van_ALLE_orgs [MEAN] + aantal_patienten_totaal [SUM] + 
    aantal_patienten_in_organisatie [SUM] + aantal_patienten_in_organisatie_met_behandeling [SUM]
  /CATEGORIES VARIABLES=InstitutionID ORDER=A KEY=VALUE EMPTY=EXCLUDE
  /CRITERIA CILEVEL=95.




* Gemiddelden voor variabelen die op teamniveau zijn.
* Bij een locatie poster neem ik aan dat we elk team hier 1 keer wegen, en niet een weging naar aantal patienten gebruiken.
* QF_Ward_ErrorsDiscussed
* QF_Ward_PU_Discussed.
DATASET ACTIVATE LPZ.
* Dus eerst een dataset per team/ward_code.
DATASET DECLARE LPZ_specialvars_teamniveau.
AGGREGATE
  /OUTFILE='LPZ_specialvars_teamniveau'
  /BREAK=InstitutionID IDresponsible Ward_code
  /QF_Ward_ErrorsDiscussed_mean_van_team=MEAN(QF_Ward_ErrorsDiscussed) 
  /QF_Ward_PU_Discussed_mean_van_team=MEAN(QF_Ward_PU_Discussed).
DATASET ACTIVATE LPZ_specialvars_teamniveau.
* Die we vervolgens kunnen aggregeren tot organisatieniveau.
DATASET DECLARE LPZ_specialvars_organisatieniveau.
AGGREGATE
 /OUTFILE='LPZ_specialvars_organisatieniveau'
 /BREAK=InstitutionID
 /QF_Ward_ErrorsDiscussed_mean_organisatie=MEAN(QF_Ward_ErrorsDiscussed_mean_van_team) 
  /QF_Ward_PU_Discussed_mean_organisatie=MEAN(QF_Ward_PU_Discussed_mean_van_team).
DATASET ACTIVATE LPZ_specialvars_organisatieniveau.

* En deze hebben we ook op landelijk niveau nodig.
AGGREGATE
 /OUTFILE=* MODE=ADDVARIABLES
 /BREAK=
  /QF_Ward_ErrorsDiscussed_mean_van_ALLE_orgs=MEAN(QF_Ward_ErrorsDiscussed_mean_organisatie) 
  /QF_Ward_PU_Discussed_mean_van_ALLE_orgs=MEAN(QF_Ward_PU_Discussed_mean_organisatie).
 

* Face validity check voor de ...discussed variabelen.
* Zien er OK uit in de data.

* Nu nog samenvoegen...
DATASET ACTIVE LPZ_organisaties.
SORT CASES BY InstitutionID.
DATASET ACTIVATE LPZ_specialvars_organisatieniveau.
SORT CASES BY InstitutionID.
DATASET ACTIVATE LPZ_organisaties.
MATCH FILES /FILE=*
  /FILE='LPZ_specialvars_organisatieniveau'
  /BY InstitutionID.
EXECUTE.



*** Aandacht voor missende waarden ***.

* Teams met teveel missende waarden kunnen verwijderd worden.
MVA D_QF_Prev_ACP_mean_organisatie TO QF_Ward_PU_Discussed_mean_van_ALLE_orgs.

* en aantal missing per rij.
compute missing_per_rij = nmiss(D_QF_Prev_ACP_mean_organisatie TO QF_Ward_PU_Discussed_mean_van_ALLE_orgs).
frequencies missing_per_rij.

COMPUTE MR_Missing = MISSING(D_QF_Prev_MR2_mean_organisatie).
COMPUTE ACP_ISNUL= D_QF_Prev_ACP_mean_organisatie = 0.
COMPUTE Errors_Discussed_Missing = MISSING(QF_Ward_ErrorsDiscussed_mean_organisatie).
COMPUTE PU_Discussed_Missing = MISSING(QF_Ward_PU_Discussed_mean_organisatie).
COMPUTE Errors_Discussed_org_Missing = MISSING(QF_Ward_ErrorsDiscussed_mean_van_ALLE_orgs).
COMPUTE PU_Discussed_org_Missing = MISSING(QF_Ward_PU_Discussed_mean_van_ALLE_orgs).
COMPUTE MAX_MISSING_ALLOWED = MR_Missing + ACP_ISNUL * 4 + Errors_Discussed_Missing + PU_Discussed_Missing + PU_Discussed_org_Missing + PU_Discussed_org_Missing. 
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



* Formatting.
* Nu zijn percentages weergegeven als proporties (schaal 0 tot 1). Maak dit schaal 0-100.

DO REPEAT V = D_QF_Prev_ACP_mean_organisatie TO D_QF_Rest_other_Rest_mean_van_ALLE_orgs
QF_Ward_ErrorsDiscussed_mean_organisatie
QF_Ward_PU_Discussed_mean_organisatie
QF_Ward_ErrorsDiscussed_mean_van_ALLE_orgs
QF_Ward_PU_Discussed_mean_van_ALLE_orgs.
COMPUTE V = V * 100.
END REPEAT PRINT.




FORMATS D_QF_Prev_ACP_mean_organisatie TO QF_Ward_PU_Discussed_mean_van_ALLE_orgs (F4.0).

EXECUTE.




*** Toevoegen van namen op wat omslachtige manier, omdat gebaseerd op toevoeging op teamniveau.
STRING CIW (A255).
COMPUTE CIW = Coordinator.
EXECUTE.

* Identify Duplicate Cases.
SORT CASES BY CIW(A).
MATCH FILES
  /FILE=*
  /BY CIW
  /FIRST=PrimaryFirst
  /LAST=PrimaryLast.
DO IF (PrimaryFirst).
COMPUTE  MatchSequence=1-PrimaryLast.
ELSE.
COMPUTE  MatchSequence=MatchSequence+1.
END IF.
LEAVE  MatchSequence.
FORMATS  MatchSequence (f7).
COMPUTE  InDupGrp=MatchSequence>0.
SORT CASES InDupGrp(D).
MATCH FILES
  /FILE=*
  /DROP=PrimaryFirst InDupGrp MatchSequence.
VARIABLE LABELS  PrimaryLast 'Indicator of each last matching case as Primary'.
VALUE LABELS  PrimaryLast 0 'Duplicate Case' 1 'Primary Case'.
VARIABLE LEVEL  PrimaryLast (ORDINAL).
FREQUENCIES VARIABLES=PrimaryLast.
EXECUTE.



* Organisatie-, Locatie- en Teamnamen koppelen.
PRESERVE.
SET DECIMAL DOT.
GET DATA  /TYPE=TXT
  /FILE="teamnamen.txt"
  /ENCODING='UTF8'
  /DELCASE=LINE
  /DELIMITERS=";"
  /ARRANGEMENT=DELIMITED
  /FIRSTCASE=2
  /DATATYPEMIN PERCENTAGE=95.0
  /VARIABLES=
  Coordinator A255
  IDresponsible A255
  Ward_code_origineel A40
  Organisatie AUTO
  Locatie AUTO
  Teamnaam AUTO
  /MAP.
RESTORE.

CACHE.
EXECUTE.
DATASET NAME namen WINDOW=FRONT.


STRING CIW (A255).
COMPUTE CIW = Coordinator.
EXECUTE.

* Identify Duplicate Cases.
SORT CASES BY CIW(A).
MATCH FILES
  /FILE=*
  /BY CIW
  /FIRST=PrimaryFirst
  /LAST=PrimaryLast.
DO IF (PrimaryFirst).
COMPUTE  MatchSequence=1-PrimaryLast.
ELSE.
COMPUTE  MatchSequence=MatchSequence+1.
END IF.
LEAVE  MatchSequence.
FORMATS  MatchSequence (f7).
COMPUTE  InDupGrp=MatchSequence>0.
SORT CASES InDupGrp(D).
MATCH FILES
  /FILE=*
  /DROP=PrimaryFirst InDupGrp MatchSequence.
VARIABLE LABELS  PrimaryLast 'Indicator of each last matching case as Primary'.
VALUE LABELS  PrimaryLast 0 'Duplicate Case' 1 'Primary Case'.
VARIABLE LEVEL  PrimaryLast (ORDINAL).
FREQUENCIES VARIABLES=PrimaryLast.
EXECUTE.

* Remove duplicates.
SELECT IF PrimaryLast = 1.
EXECUTE.

* Dan koppelen. Doen alsof het one-to-many is zodat het een left join wordt.
SORT CASES BY CIW.
DATASET ACTIVATE namen.
SORT CASES BY CIW.
DATASET ACTIVATE LPZ_organisaties.
MATCH FILES /FILE=*
  /TABLE='namen'
  /RENAME (Coordinator IDresponsible PrimaryLast Ward_code_origineel Teamnaam = d0 d1 d2 d3 d4) 
  /BY CIW
  /DROP= d0 d1 d2 d3 d4.
EXECUTE.





DATASET CLOSE LPZ_specialvars_teamniveau.
DATASET CLOSE LPZ_specialvars_organisatieniveau.
DATASET CLOSE LPZ.
DATASET CLOSE namen.
DATASET ACTIVATE LPZ_organisaties.








SAVE OUTFILE='Data\LPZ_organisatiedata.sav'
  /COMPRESSED.


SAVE TRANSLATE OUTFILE='Data\LPZ_organisatiedata.csv'
  /TYPE=CSV
  /ENCODING='UTF8'
  /MAP
  /REPLACE
  /FIELDNAMES
  /CELLS=LABELS.






