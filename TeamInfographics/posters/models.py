# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Lpz2019Locaties(models.Model):
    id = models.IntegerField(primary_key=True)
    institutionid = models.IntegerField(db_column='InstitutionID', blank=True, null=True)  # Field name made lowercase.
    idresponsible = models.IntegerField(db_column='IDresponsible', blank=True, null=True)  # Field name made lowercase.
    measurementday = models.TextField(db_column='Measurementday', blank=True, null=True)  # Field name made lowercase.
    coordinator = models.IntegerField(db_column='Coordinator', blank=True, null=True)  # Field name made lowercase.
    institutionform_type_inst = models.TextField(db_column='InstitutionForm_Type_Inst', blank=True, null=True)  # Field name made lowercase.
    institutionform_mod_qualityframework = models.TextField(db_column='InstitutionForm_Mod_Qualityframework', blank=True, null=True)  # Field name made lowercase.
    d_age_mean_locatie = models.FloatField(db_column='D_Age_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_prev_acp_mean_locatie = models.FloatField(db_column='D_QF_Prev_ACP_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_resusication_mean_locatie = models.TextField(db_column='D_QF_ACP_resusication_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_life_ending_treat_mean_locatie = models.TextField(db_column='D_QF_ACP_life_ending_treat_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_hosp_adm_mean_locatie = models.TextField(db_column='D_QF_ACP_hosp_adm_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_other_mean_locatie = models.TextField(db_column='D_QF_ACP_other_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_prev_mr2_mean_locatie = models.TextField(db_column='D_QF_Prev_MR2_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_mean_locatie = models.FloatField(db_column='D_QF_Nut_foodpreferences_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_specific_mean_locatie = models.FloatField(db_column='D_QF_Nut_foodpreferences_specific_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_offering_mean_locatie = models.FloatField(db_column='D_QF_Nut_foodpreferences_offering_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_support_mean_locatie = models.FloatField(db_column='D_QF_Nut_foodpreferences_support_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_time_mean_locatie = models.FloatField(db_column='D_QF_Nut_foodpreferences_time_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_other_mean_locatie = models.FloatField(db_column='D_QF_Nut_foodpreferences_other_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_pu_prev_cat2_mean_locatie = models.FloatField(db_column='D_QF_PU_Prev_cat2_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_mean_locatie = models.FloatField(db_column='D_QF_Inc_toiletingplan_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_preferences_mean_locatie = models.FloatField(db_column='D_QF_Inc_toiletingplan_preferences_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_independent_mean_locatie = models.FloatField(db_column='D_QF_Inc_toiletingplan_independent_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_support_mean_locatie = models.FloatField(db_column='D_QF_Inc_toiletingplan_support_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_materials_mean_locatie = models.FloatField(db_column='D_QF_Inc_toiletingplan_materials_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_other_mean_locatie = models.FloatField(db_column='D_QF_Inc_toiletingplan_other_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_prev_mean_locatie = models.FloatField(db_column='D_QF_Rest_Prev_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_mechanical_mean_locatie = models.FloatField(db_column='D_QF_Rest_mechanical_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_physical_mean_locatie = models.FloatField(db_column='D_QF_Rest_physical_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_pharmacologic_mean_locatie = models.FloatField(db_column='D_QF_Rest_pharmacologic_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_psych_mean_locatie = models.FloatField(db_column='D_QF_Rest_psych_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_electronic_mean_locatie = models.FloatField(db_column='D_QF_Rest_electronic_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_supervision_mean_locatie = models.FloatField(db_column='D_QF_Rest_supervision_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_seclusion_mean_locatie = models.FloatField(db_column='D_QF_Rest_seclusion_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_other_rest_mean_locatie = models.FloatField(db_column='D_QF_Rest_other_Rest_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_prev_acp_mean_van_org = models.FloatField(db_column='D_QF_Prev_ACP_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_resusication_mean_van_org = models.FloatField(db_column='D_QF_ACP_resusication_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_life_ending_treat_mean_van_org = models.FloatField(db_column='D_QF_ACP_life_ending_treat_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_hosp_adm_mean_van_org = models.FloatField(db_column='D_QF_ACP_hosp_adm_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_other_mean_van_org = models.FloatField(db_column='D_QF_ACP_other_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_prev_mr2_mean_van_org = models.FloatField(db_column='D_QF_Prev_MR2_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_mean_van_org = models.FloatField(db_column='D_QF_Nut_foodpreferences_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_specific_mean_van_org = models.FloatField(db_column='D_QF_Nut_foodpreferences_specific_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_offering_mean_van_org = models.FloatField(db_column='D_QF_Nut_foodpreferences_offering_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_support_mean_van_org = models.FloatField(db_column='D_QF_Nut_foodpreferences_support_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_time_mean_van_org = models.FloatField(db_column='D_QF_Nut_foodpreferences_time_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_other_mean_van_org = models.FloatField(db_column='D_QF_Nut_foodpreferences_other_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_pu_prev_cat2_mean_van_org = models.FloatField(db_column='D_QF_PU_Prev_cat2_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_mean_van_org = models.FloatField(db_column='D_QF_Inc_toiletingplan_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_preferences_mean_van_org = models.FloatField(db_column='D_QF_Inc_toiletingplan_preferences_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_independent_mean_van_org = models.FloatField(db_column='D_QF_Inc_toiletingplan_independent_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_support_mean_van_org = models.FloatField(db_column='D_QF_Inc_toiletingplan_support_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_materials_mean_van_org = models.FloatField(db_column='D_QF_Inc_toiletingplan_materials_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_other_mean_van_org = models.FloatField(db_column='D_QF_Inc_toiletingplan_other_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_prev_mean_van_org = models.FloatField(db_column='D_QF_Rest_Prev_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_mechanical_mean_van_org = models.FloatField(db_column='D_QF_Rest_mechanical_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_physical_mean_van_org = models.FloatField(db_column='D_QF_Rest_physical_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_pharmacologic_mean_van_org = models.FloatField(db_column='D_QF_Rest_pharmacologic_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_psych_mean_van_org = models.FloatField(db_column='D_QF_Rest_psych_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_electronic_mean_van_org = models.FloatField(db_column='D_QF_Rest_electronic_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_supervision_mean_van_org = models.FloatField(db_column='D_QF_Rest_supervision_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_seclusion_mean_van_org = models.FloatField(db_column='D_QF_Rest_seclusion_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_other_rest_mean_van_org = models.FloatField(db_column='D_QF_Rest_other_Rest_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    aantal_patienten_per_org = models.IntegerField(blank=True, null=True)
    aantal_patienten_in_locatie = models.IntegerField(blank=True, null=True)
    aantal_patienten_in_locatie_met_behandeling = models.IntegerField(blank=True, null=True)
    qf_ward_errorsdiscussed_mean_locatie = models.TextField(db_column='QF_Ward_ErrorsDiscussed_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    qf_ward_pu_discussed_mean_locatie = models.TextField(db_column='QF_Ward_PU_Discussed_mean_locatie', blank=True, null=True)  # Field name made lowercase.
    qf_ward_errorsdiscussed_mean_van_org = models.FloatField(db_column='QF_Ward_ErrorsDiscussed_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    qf_ward_pu_discussed_mean_van_org = models.TextField(db_column='QF_Ward_PU_Discussed_mean_van_org', blank=True, null=True)  # Field name made lowercase.
    missing_per_rij = models.IntegerField(blank=True, null=True)
    mr_missing = models.IntegerField(db_column='MR_Missing', blank=True, null=True)  # Field name made lowercase.
    acp_isnul = models.IntegerField(db_column='ACP_ISNUL', blank=True, null=True)  # Field name made lowercase.
    errors_discussed_missing = models.IntegerField(db_column='Errors_Discussed_Missing', blank=True, null=True)  # Field name made lowercase.
    pu_discussed_missing = models.IntegerField(db_column='PU_Discussed_Missing', blank=True, null=True)  # Field name made lowercase.
    errors_discussed_org_missing = models.IntegerField(db_column='Errors_Discussed_org_Missing', blank=True, null=True)  # Field name made lowercase.
    pu_discussed_org_missing = models.IntegerField(db_column='PU_Discussed_org_Missing', blank=True, null=True)  # Field name made lowercase.
    max_missing_allowed = models.IntegerField(db_column='MAX_MISSING_ALLOWED', blank=True, null=True)  # Field name made lowercase.
    teveel_missing = models.TextField(blank=True, null=True)
    ciw = models.IntegerField(db_column='CIW', blank=True, null=True)  # Field name made lowercase.
    primarylast = models.TextField(db_column='PrimaryLast', blank=True, null=True)  # Field name made lowercase.
    organisatie = models.TextField(db_column='Organisatie', blank=True, null=True)  # Field name made lowercase.
    locatie = models.TextField(db_column='Locatie', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LPZ2019Locaties'


class Lpz2019Organisaties(models.Model):
    id = models.IntegerField(primary_key=True)
    institutionid = models.IntegerField(db_column='InstitutionID', blank=True, null=True)  # Field name made lowercase.
    measurementday = models.TextField(db_column='Measurementday', blank=True, null=True)  # Field name made lowercase.
    coordinator = models.IntegerField(db_column='Coordinator', blank=True, null=True)  # Field name made lowercase.
    institutionform_type_inst = models.TextField(db_column='InstitutionForm_Type_Inst', blank=True, null=True)  # Field name made lowercase.
    institutionform_mod_qualityframework = models.TextField(db_column='InstitutionForm_Mod_Qualityframework', blank=True, null=True)  # Field name made lowercase.
    d_age_mean_organisatie = models.FloatField(db_column='D_Age_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_prev_acp_mean_organisatie = models.FloatField(db_column='D_QF_Prev_ACP_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_resusication_mean_organisatie = models.FloatField(db_column='D_QF_ACP_resusication_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_life_ending_treat_mean_organisatie = models.FloatField(db_column='D_QF_ACP_life_ending_treat_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_hosp_adm_mean_organisatie = models.FloatField(db_column='D_QF_ACP_hosp_adm_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_other_mean_organisatie = models.FloatField(db_column='D_QF_ACP_other_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_prev_mr2_mean_organisatie = models.FloatField(db_column='D_QF_Prev_MR2_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_mean_organisatie = models.FloatField(db_column='D_QF_Nut_foodpreferences_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_specific_mean_organisatie = models.FloatField(db_column='D_QF_Nut_foodpreferences_specific_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_offering_mean_organisatie = models.FloatField(db_column='D_QF_Nut_foodpreferences_offering_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_support_mean_organisatie = models.FloatField(db_column='D_QF_Nut_foodpreferences_support_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_time_mean_organisatie = models.FloatField(db_column='D_QF_Nut_foodpreferences_time_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_other_mean_organisatie = models.FloatField(db_column='D_QF_Nut_foodpreferences_other_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_pu_prev_cat2_mean_organisatie = models.FloatField(db_column='D_QF_PU_Prev_cat2_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_mean_organisatie = models.FloatField(db_column='D_QF_Inc_toiletingplan_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_preferences_mean_organisatie = models.FloatField(db_column='D_QF_Inc_toiletingplan_preferences_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_independent_mean_organisatie = models.FloatField(db_column='D_QF_Inc_toiletingplan_independent_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_support_mean_organisatie = models.FloatField(db_column='D_QF_Inc_toiletingplan_support_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_materials_mean_organisatie = models.FloatField(db_column='D_QF_Inc_toiletingplan_materials_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_other_mean_organisatie = models.FloatField(db_column='D_QF_Inc_toiletingplan_other_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_prev_mean_organisatie = models.FloatField(db_column='D_QF_Rest_Prev_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_mechanical_mean_organisatie = models.FloatField(db_column='D_QF_Rest_mechanical_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_physical_mean_organisatie = models.FloatField(db_column='D_QF_Rest_physical_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_pharmacologic_mean_organisatie = models.FloatField(db_column='D_QF_Rest_pharmacologic_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_psych_mean_organisatie = models.FloatField(db_column='D_QF_Rest_psych_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_electronic_mean_organisatie = models.FloatField(db_column='D_QF_Rest_electronic_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_supervision_mean_organisatie = models.FloatField(db_column='D_QF_Rest_supervision_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_seclusion_mean_organisatie = models.FloatField(db_column='D_QF_Rest_seclusion_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_other_rest_mean_organisatie = models.FloatField(db_column='D_QF_Rest_other_Rest_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    d_qf_prev_acp_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Prev_ACP_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_resusication_mean_van_alle_orgs = models.FloatField(db_column='D_QF_ACP_resusication_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_life_ending_treat_mean_van_alle_orgs = models.FloatField(db_column='D_QF_ACP_life_ending_treat_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_hosp_adm_mean_van_alle_orgs = models.FloatField(db_column='D_QF_ACP_hosp_adm_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_other_mean_van_alle_orgs = models.FloatField(db_column='D_QF_ACP_other_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_prev_mr2_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Prev_MR2_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Nut_foodpreferences_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_specific_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Nut_foodpreferences_specific_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_offering_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Nut_foodpreferences_offering_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_support_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Nut_foodpreferences_support_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_time_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Nut_foodpreferences_time_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_other_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Nut_foodpreferences_other_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_pu_prev_cat2_mean_van_alle_orgs = models.FloatField(db_column='D_QF_PU_Prev_cat2_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Inc_toiletingplan_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_preferences_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Inc_toiletingplan_preferences_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_independent_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Inc_toiletingplan_independent_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_support_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Inc_toiletingplan_support_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_materials_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Inc_toiletingplan_materials_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_other_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Inc_toiletingplan_other_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_prev_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Rest_Prev_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_mechanical_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Rest_mechanical_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_physical_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Rest_physical_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_pharmacologic_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Rest_pharmacologic_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_psych_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Rest_psych_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_electronic_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Rest_electronic_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_supervision_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Rest_supervision_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_seclusion_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Rest_seclusion_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_other_rest_mean_van_alle_orgs = models.FloatField(db_column='D_QF_Rest_other_Rest_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    aantal_patienten_totaal = models.IntegerField(blank=True, null=True)
    aantal_patienten_in_organisatie = models.IntegerField(blank=True, null=True)
    aantal_patienten_in_organisatie_met_behandeling = models.IntegerField(blank=True, null=True)
    qf_ward_errorsdiscussed_mean_organisatie = models.FloatField(db_column='QF_Ward_ErrorsDiscussed_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    qf_ward_pu_discussed_mean_organisatie = models.TextField(db_column='QF_Ward_PU_Discussed_mean_organisatie', blank=True, null=True)  # Field name made lowercase.
    qf_ward_errorsdiscussed_mean_van_alle_orgs = models.FloatField(db_column='QF_Ward_ErrorsDiscussed_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    qf_ward_pu_discussed_mean_van_alle_orgs = models.FloatField(db_column='QF_Ward_PU_Discussed_mean_van_ALLE_orgs', blank=True, null=True)  # Field name made lowercase.
    missing_per_rij = models.IntegerField(blank=True, null=True)
    mr_missing = models.IntegerField(db_column='MR_Missing', blank=True, null=True)  # Field name made lowercase.
    acp_isnul = models.IntegerField(db_column='ACP_ISNUL', blank=True, null=True)  # Field name made lowercase.
    errors_discussed_missing = models.IntegerField(db_column='Errors_Discussed_Missing', blank=True, null=True)  # Field name made lowercase.
    pu_discussed_missing = models.IntegerField(db_column='PU_Discussed_Missing', blank=True, null=True)  # Field name made lowercase.
    errors_discussed_org_missing = models.IntegerField(db_column='Errors_Discussed_org_Missing', blank=True, null=True)  # Field name made lowercase.
    pu_discussed_org_missing = models.IntegerField(db_column='PU_Discussed_org_Missing', blank=True, null=True)  # Field name made lowercase.
    max_missing_allowed = models.IntegerField(db_column='MAX_MISSING_ALLOWED', blank=True, null=True)  # Field name made lowercase.
    teveel_missing = models.TextField(blank=True, null=True)
    ciw = models.IntegerField(db_column='CIW', blank=True, null=True)  # Field name made lowercase.
    primarylast = models.TextField(db_column='PrimaryLast', blank=True, null=True)  # Field name made lowercase.
    organisatie = models.TextField(db_column='Organisatie', blank=True, null=True)  # Field name made lowercase.
    locatie = models.TextField(db_column='Locatie', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LPZ2019Organisaties'


class Lpz2019Teams(models.Model):
    id = models.IntegerField(primary_key=True)
    ward_code = models.TextField(db_column='Ward_code', blank=True, null=True)  # Field name made lowercase.
    measurementday = models.TextField(db_column='Measurementday', blank=True, null=True)  # Field name made lowercase.
    coordinator = models.IntegerField(db_column='Coordinator', blank=True, null=True)  # Field name made lowercase.
    institutionid = models.IntegerField(db_column='InstitutionID', blank=True, null=True)  # Field name made lowercase.
    idresponsible = models.IntegerField(db_column='IDresponsible', blank=True, null=True)  # Field name made lowercase.
    ward_code_origineel = models.TextField(db_column='Ward_code_origineel', blank=True, null=True)  # Field name made lowercase.
    institutionform_type_inst = models.TextField(db_column='InstitutionForm_Type_Inst', blank=True, null=True)  # Field name made lowercase.
    institutionform_mod_qualityframework = models.TextField(db_column='InstitutionForm_Mod_Qualityframework', blank=True, null=True)  # Field name made lowercase.
    type_ward = models.TextField(db_column='Type_Ward', blank=True, null=True)  # Field name made lowercase.
    afkorting_type_ward = models.TextField(blank=True, null=True)
    d_age_mean_team = models.FloatField(db_column='D_Age_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_prev_acp_mean_team = models.FloatField(db_column='D_QF_Prev_ACP_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_resusication_mean_team = models.TextField(db_column='D_QF_ACP_resusication_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_life_ending_treat_mean_team = models.TextField(db_column='D_QF_ACP_life_ending_treat_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_hosp_adm_mean_team = models.TextField(db_column='D_QF_ACP_hosp_adm_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_other_mean_team = models.TextField(db_column='D_QF_ACP_other_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_prev_mr2_mean_team = models.TextField(db_column='D_QF_Prev_MR2_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_mean_team = models.FloatField(db_column='D_QF_Nut_foodpreferences_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_specific_mean_team = models.FloatField(db_column='D_QF_Nut_foodpreferences_specific_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_offering_mean_team = models.FloatField(db_column='D_QF_Nut_foodpreferences_offering_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_support_mean_team = models.FloatField(db_column='D_QF_Nut_foodpreferences_support_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_time_mean_team = models.FloatField(db_column='D_QF_Nut_foodpreferences_time_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_other_mean_team = models.FloatField(db_column='D_QF_Nut_foodpreferences_other_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_pu_prev_cat2_mean_team = models.FloatField(db_column='D_QF_PU_Prev_cat2_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_mean_team = models.FloatField(db_column='D_QF_Inc_toiletingplan_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_preferences_mean_team = models.FloatField(db_column='D_QF_Inc_toiletingplan_preferences_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_independent_mean_team = models.FloatField(db_column='D_QF_Inc_toiletingplan_independent_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_support_mean_team = models.FloatField(db_column='D_QF_Inc_toiletingplan_support_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_materials_mean_team = models.FloatField(db_column='D_QF_Inc_toiletingplan_materials_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_other_mean_team = models.FloatField(db_column='D_QF_Inc_toiletingplan_other_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_prev_mean_team = models.FloatField(db_column='D_QF_Rest_Prev_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_mechanical_mean_team = models.FloatField(db_column='D_QF_Rest_mechanical_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_physical_mean_team = models.FloatField(db_column='D_QF_Rest_physical_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_pharmacologic_mean_team = models.FloatField(db_column='D_QF_Rest_pharmacologic_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_psych_mean_team = models.FloatField(db_column='D_QF_Rest_psych_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_electronic_mean_team = models.FloatField(db_column='D_QF_Rest_electronic_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_supervision_mean_team = models.FloatField(db_column='D_QF_Rest_supervision_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_seclusion_mean_team = models.FloatField(db_column='D_QF_Rest_seclusion_mean_team', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_other_rest_mean_team = models.FloatField(db_column='D_QF_Rest_other_Rest_mean_team', blank=True, null=True)  # Field name made lowercase.
    qf_ward_errorsdiscussed = models.TextField(db_column='QF_Ward_ErrorsDiscussed', blank=True, null=True)  # Field name made lowercase.
    qf_ward_pu_discussed = models.TextField(db_column='QF_Ward_PU_Discussed', blank=True, null=True)  # Field name made lowercase.
    d_qf_prev_acp_mean_type_ward = models.FloatField(db_column='D_QF_Prev_ACP_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_resusication_mean_type_ward = models.FloatField(db_column='D_QF_ACP_resusication_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_life_ending_treat_mean_type_ward = models.FloatField(db_column='D_QF_ACP_life_ending_treat_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_hosp_adm_mean_type_ward = models.FloatField(db_column='D_QF_ACP_hosp_adm_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_acp_other_mean_type_ward = models.FloatField(db_column='D_QF_ACP_other_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_prev_mr2_mean_type_ward = models.TextField(db_column='D_QF_Prev_MR2_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_mean_type_ward = models.FloatField(db_column='D_QF_Nut_foodpreferences_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_specific_mean_type_ward = models.FloatField(db_column='D_QF_Nut_foodpreferences_specific_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_offering_mean_type_ward = models.FloatField(db_column='D_QF_Nut_foodpreferences_offering_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_support_mean_type_ward = models.FloatField(db_column='D_QF_Nut_foodpreferences_support_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_time_mean_type_ward = models.FloatField(db_column='D_QF_Nut_foodpreferences_time_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_nut_foodpreferences_other_mean_type_ward = models.FloatField(db_column='D_QF_Nut_foodpreferences_other_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_pu_prev_cat2_mean_type_ward = models.FloatField(db_column='D_QF_PU_Prev_cat2_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_mean_type_ward = models.FloatField(db_column='D_QF_Inc_toiletingplan_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_preferences_mean_type_ward = models.FloatField(db_column='D_QF_Inc_toiletingplan_preferences_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_independent_mean_type_ward = models.FloatField(db_column='D_QF_Inc_toiletingplan_independent_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_support_mean_type_ward = models.FloatField(db_column='D_QF_Inc_toiletingplan_support_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_materials_mean_type_ward = models.FloatField(db_column='D_QF_Inc_toiletingplan_materials_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_inc_toiletingplan_other_mean_type_ward = models.FloatField(db_column='D_QF_Inc_toiletingplan_other_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_prev_mean_type_ward = models.FloatField(db_column='D_QF_Rest_Prev_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_mechanical_mean_type_ward = models.FloatField(db_column='D_QF_Rest_mechanical_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_physical_mean_type_ward = models.FloatField(db_column='D_QF_Rest_physical_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_pharmacologic_mean_type_ward = models.FloatField(db_column='D_QF_Rest_pharmacologic_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_psych_mean_type_ward = models.FloatField(db_column='D_QF_Rest_psych_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_electronic_mean_type_ward = models.FloatField(db_column='D_QF_Rest_electronic_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_supervision_mean_type_ward = models.FloatField(db_column='D_QF_Rest_supervision_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_seclusion_mean_type_ward = models.FloatField(db_column='D_QF_Rest_seclusion_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    d_qf_rest_other_rest_mean_type_ward = models.FloatField(db_column='D_QF_Rest_other_Rest_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    aantal_patienten_per_ward_type = models.IntegerField(blank=True, null=True)
    aantal_patienten_in_team = models.IntegerField(blank=True, null=True)
    aantal_patienten_in_team_met_behandeling = models.IntegerField(blank=True, null=True)
    qf_ward_errorsdiscussed_mean_type_ward = models.FloatField(db_column='QF_Ward_ErrorsDiscussed_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    qf_ward_pu_discussed_mean_type_ward = models.FloatField(db_column='QF_Ward_PU_Discussed_mean_type_ward', blank=True, null=True)  # Field name made lowercase.
    missing_per_rij = models.IntegerField(blank=True, null=True)
    mr_missing = models.IntegerField(db_column='MR_Missing', blank=True, null=True)  # Field name made lowercase.
    acp_isnul = models.IntegerField(db_column='ACP_ISNUL', blank=True, null=True)  # Field name made lowercase.
    errors_discussed_missing = models.IntegerField(db_column='Errors_Discussed_Missing', blank=True, null=True)  # Field name made lowercase.
    pu_discussed_missing = models.IntegerField(db_column='PU_Discussed_Missing', blank=True, null=True)  # Field name made lowercase.
    max_missing_allowed = models.IntegerField(db_column='MAX_MISSING_ALLOWED', blank=True, null=True)  # Field name made lowercase.
    teveel_missing = models.TextField(blank=True, null=True)
    ciw = models.TextField(db_column='CIW', blank=True, null=True)  # Field name made lowercase.
    primarylast = models.TextField(db_column='PrimaryLast', blank=True, null=True)  # Field name made lowercase.
    organisatie = models.TextField(db_column='Organisatie', blank=True, null=True)  # Field name made lowercase.
    locatie = models.TextField(db_column='Locatie', blank=True, null=True)  # Field name made lowercase.
    teamnaam = models.TextField(db_column='Teamnaam', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LPZ2019Teams'

