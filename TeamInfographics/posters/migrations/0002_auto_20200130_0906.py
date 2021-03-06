# Generated by Django 2.2.5 on 2020-01-30 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lpz2019Teams',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ward_code', models.TextField(blank=True, db_column='Ward_code', null=True)),
                ('measurementday', models.TextField(blank=True, db_column='Measurementday', null=True)),
                ('institutionid', models.IntegerField(blank=True, db_column='InstitutionID', null=True)),
                ('institutionform_type_inst', models.TextField(blank=True, db_column='InstitutionForm_Type_Inst', null=True)),
                ('institutionform_mod_qualityframework', models.TextField(blank=True, db_column='InstitutionForm_Mod_Qualityframework', null=True)),
                ('type_ward', models.TextField(blank=True, db_column='Type_Ward', null=True)),
                ('d_age_mean_team', models.FloatField(blank=True, db_column='D_Age_mean_team', null=True)),
                ('d_qf_prev_acp_mean_team', models.FloatField(blank=True, db_column='D_QF_Prev_ACP_mean_team', null=True)),
                ('d_qf_acp_resusication_mean_team', models.TextField(blank=True, db_column='D_QF_ACP_resusication_mean_team', null=True)),
                ('d_qf_acp_life_ending_treat_mean_team', models.TextField(blank=True, db_column='D_QF_ACP_life_ending_treat_mean_team', null=True)),
                ('d_qf_acp_hosp_adm_mean_team', models.TextField(blank=True, db_column='D_QF_ACP_hosp_adm_mean_team', null=True)),
                ('d_qf_acp_other_mean_team', models.TextField(blank=True, db_column='D_QF_ACP_other_mean_team', null=True)),
                ('d_qf_prev_mr2_mean_team', models.TextField(blank=True, db_column='D_QF_Prev_MR2_mean_team', null=True)),
                ('d_qf_nut_foodpreferences_mean_team', models.FloatField(blank=True, db_column='D_QF_Nut_foodpreferences_mean_team', null=True)),
                ('d_qf_nut_foodpreferences_specific_mean_team', models.FloatField(blank=True, db_column='D_QF_Nut_foodpreferences_specific_mean_team', null=True)),
                ('d_qf_nut_foodpreferences_offering_mean_team', models.FloatField(blank=True, db_column='D_QF_Nut_foodpreferences_offering_mean_team', null=True)),
                ('d_qf_nut_foodpreferences_support_mean_team', models.FloatField(blank=True, db_column='D_QF_Nut_foodpreferences_support_mean_team', null=True)),
                ('d_qf_nut_foodpreferences_time_mean_team', models.FloatField(blank=True, db_column='D_QF_Nut_foodpreferences_time_mean_team', null=True)),
                ('d_qf_nut_foodpreferences_other_mean_team', models.FloatField(blank=True, db_column='D_QF_Nut_foodpreferences_other_mean_team', null=True)),
                ('d_qf_pu_prev_cat2_mean_team', models.FloatField(blank=True, db_column='D_QF_PU_Prev_cat2_mean_team', null=True)),
                ('d_qf_inc_toiletingplan_mean_team', models.FloatField(blank=True, db_column='D_QF_Inc_toiletingplan_mean_team', null=True)),
                ('d_qf_inc_toiletingplan_preferences_mean_team', models.FloatField(blank=True, db_column='D_QF_Inc_toiletingplan_preferences_mean_team', null=True)),
                ('d_qf_inc_toiletingplan_independent_mean_team', models.FloatField(blank=True, db_column='D_QF_Inc_toiletingplan_independent_mean_team', null=True)),
                ('d_qf_inc_toiletingplan_support_mean_team', models.FloatField(blank=True, db_column='D_QF_Inc_toiletingplan_support_mean_team', null=True)),
                ('d_qf_inc_toiletingplan_materials_mean_team', models.FloatField(blank=True, db_column='D_QF_Inc_toiletingplan_materials_mean_team', null=True)),
                ('d_qf_inc_toiletingplan_other_mean_team', models.FloatField(blank=True, db_column='D_QF_Inc_toiletingplan_other_mean_team', null=True)),
                ('d_qf_rest_prev_mean_team', models.FloatField(blank=True, db_column='D_QF_Rest_Prev_mean_team', null=True)),
                ('d_qf_rest_mechanical_mean_team', models.FloatField(blank=True, db_column='D_QF_Rest_mechanical_mean_team', null=True)),
                ('d_qf_rest_physical_mean_team', models.FloatField(blank=True, db_column='D_QF_Rest_physical_mean_team', null=True)),
                ('d_qf_rest_pharmacologic_mean_team', models.FloatField(blank=True, db_column='D_QF_Rest_pharmacologic_mean_team', null=True)),
                ('d_qf_rest_psych_mean_team', models.FloatField(blank=True, db_column='D_QF_Rest_psych_mean_team', null=True)),
                ('d_qf_rest_electronic_mean_team', models.FloatField(blank=True, db_column='D_QF_Rest_electronic_mean_team', null=True)),
                ('d_qf_rest_supervision_mean_team', models.FloatField(blank=True, db_column='D_QF_Rest_supervision_mean_team', null=True)),
                ('d_qf_rest_seclusion_mean_team', models.FloatField(blank=True, db_column='D_QF_Rest_seclusion_mean_team', null=True)),
                ('d_qf_rest_other_rest_mean_team', models.FloatField(blank=True, db_column='D_QF_Rest_other_Rest_mean_team', null=True)),
                ('qf_ward_errorsdiscussed', models.TextField(blank=True, db_column='QF_Ward_ErrorsDiscussed', null=True)),
                ('qf_ward_pu_discussed', models.TextField(blank=True, db_column='QF_Ward_PU_Discussed', null=True)),
                ('d_qf_prev_acp_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Prev_ACP_mean_type_ward', null=True)),
                ('d_qf_acp_resusication_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_ACP_resusication_mean_type_ward', null=True)),
                ('d_qf_acp_life_ending_treat_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_ACP_life_ending_treat_mean_type_ward', null=True)),
                ('d_qf_acp_hosp_adm_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_ACP_hosp_adm_mean_type_ward', null=True)),
                ('d_qf_acp_other_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_ACP_other_mean_type_ward', null=True)),
                ('d_qf_prev_mr2_mean_type_ward', models.TextField(blank=True, db_column='D_QF_Prev_MR2_mean_type_ward', null=True)),
                ('d_qf_nut_foodpreferences_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Nut_foodpreferences_mean_type_ward', null=True)),
                ('d_qf_nut_foodpreferences_specific_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Nut_foodpreferences_specific_mean_type_ward', null=True)),
                ('d_qf_nut_foodpreferences_offering_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Nut_foodpreferences_offering_mean_type_ward', null=True)),
                ('d_qf_nut_foodpreferences_support_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Nut_foodpreferences_support_mean_type_ward', null=True)),
                ('d_qf_nut_foodpreferences_time_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Nut_foodpreferences_time_mean_type_ward', null=True)),
                ('d_qf_nut_foodpreferences_other_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Nut_foodpreferences_other_mean_type_ward', null=True)),
                ('d_qf_pu_prev_cat2_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_PU_Prev_cat2_mean_type_ward', null=True)),
                ('d_qf_inc_toiletingplan_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Inc_toiletingplan_mean_type_ward', null=True)),
                ('d_qf_inc_toiletingplan_preferences_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Inc_toiletingplan_preferences_mean_type_ward', null=True)),
                ('d_qf_inc_toiletingplan_independent_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Inc_toiletingplan_independent_mean_type_ward', null=True)),
                ('d_qf_inc_toiletingplan_support_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Inc_toiletingplan_support_mean_type_ward', null=True)),
                ('d_qf_inc_toiletingplan_materials_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Inc_toiletingplan_materials_mean_type_ward', null=True)),
                ('d_qf_inc_toiletingplan_other_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Inc_toiletingplan_other_mean_type_ward', null=True)),
                ('d_qf_rest_prev_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Rest_Prev_mean_type_ward', null=True)),
                ('d_qf_rest_mechanical_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Rest_mechanical_mean_type_ward', null=True)),
                ('d_qf_rest_physical_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Rest_physical_mean_type_ward', null=True)),
                ('d_qf_rest_pharmacologic_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Rest_pharmacologic_mean_type_ward', null=True)),
                ('d_qf_rest_psych_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Rest_psych_mean_type_ward', null=True)),
                ('d_qf_rest_electronic_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Rest_electronic_mean_type_ward', null=True)),
                ('d_qf_rest_supervision_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Rest_supervision_mean_type_ward', null=True)),
                ('d_qf_rest_seclusion_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Rest_seclusion_mean_type_ward', null=True)),
                ('d_qf_rest_other_rest_mean_type_ward', models.FloatField(blank=True, db_column='D_QF_Rest_other_Rest_mean_type_ward', null=True)),
                ('aantal_patienten_per_ward_type', models.IntegerField(blank=True, null=True)),
                ('aantal_patienten_in_team', models.IntegerField(blank=True, null=True)),
                ('aantal_patienten_in_team_met_behandeling', models.IntegerField(blank=True, null=True)),
                ('qf_ward_errorsdiscussed_mean_type_ward', models.FloatField(blank=True, db_column='QF_Ward_ErrorsDiscussed_mean_type_ward', null=True)),
                ('qf_ward_pu_discussed_mean_type_ward', models.FloatField(blank=True, db_column='QF_Ward_PU_Discussed_mean_type_ward', null=True)),
                ('missing_per_rij', models.IntegerField(blank=True, null=True)),
                ('mr_missing', models.IntegerField(blank=True, db_column='MR_Missing', null=True)),
                ('acp_isnul', models.IntegerField(blank=True, db_column='ACP_ISNUL', null=True)),
                ('errors_discussed_missing', models.IntegerField(blank=True, db_column='Errors_Discussed_Missing', null=True)),
                ('pu_discussed_missing', models.IntegerField(blank=True, db_column='PU_Discussed_Missing', null=True)),
                ('max_missing_allowed', models.IntegerField(blank=True, db_column='MAX_MISSING_ALLOWED', null=True)),
                ('teveel_missing', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'LPZ2019Teams',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Lpz2019V1',
        ),
    ]
