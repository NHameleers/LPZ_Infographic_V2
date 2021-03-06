# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Lpz2019V1(models.Model):
    index = models.IntegerField(blank=True, null=True)
    measurementday = models.TextField(db_column='Measurementday', blank=True, null=True)  # Field name made lowercase.
    ward_name = models.TextField(db_column='Ward_name', blank=True, null=True)  # Field name made lowercase.
    ward_type = models.TextField(db_column='Ward_type', blank=True, null=True)  # Field name made lowercase.
    d_num_clients_part = models.IntegerField(db_column='D_Num_clients_part', blank=True, null=True)  # Field name made lowercase.
    d_num_clients_beh = models.IntegerField(db_column='D_Num_clients_beh', blank=True, null=True)  # Field name made lowercase.
    qf_ward_pu_discussed = models.TextField(db_column='QF_Ward_PU_Discussed', blank=True, null=True)  # Field name made lowercase.
    qf_ward_pu_discussed_afd = models.FloatField(db_column='QF_Ward_PU_Discussed_afd', blank=True, null=True)  # Field name made lowercase.
    pu_prev = models.FloatField(db_column='PU_Prev', blank=True, null=True)  # Field name made lowercase.
    pu_prev_ward = models.FloatField(db_column='PU_Prev_ward', blank=True, null=True)  # Field name made lowercase.
    med_fouten = models.TextField(db_column='Med_fouten', blank=True, null=True)  # Field name made lowercase.
    med_fouten_ward_nee = models.FloatField(db_column='Med_fouten_ward_nee', blank=True, null=True)  # Field name made lowercase.
    med_fouten_ward_ja_nietmultid = models.FloatField(db_column='Med_fouten_ward_ja_nietmultid', blank=True, null=True)  # Field name made lowercase.
    med_fouten_ward_ja = models.FloatField(db_column='Med_fouten_ward_ja', blank=True, null=True)  # Field name made lowercase.
    med_review = models.TextField(db_column='Med_review', blank=True, null=True)  # Field name made lowercase.
    med_review_ward = models.FloatField(db_column='Med_review_ward', blank=True, null=True)  # Field name made lowercase.
    acp_reanimeren = models.FloatField(db_column='ACP_reanimeren', blank=True, null=True)  # Field name made lowercase.
    acp_reanimeren_ward = models.FloatField(db_column='ACP_reanimeren_ward', blank=True, null=True)  # Field name made lowercase.
    acp_lifeending = models.FloatField(db_column='ACP_lifeending', blank=True, null=True)  # Field name made lowercase.
    acp_lifeending_ward = models.FloatField(db_column='ACP_lifeending_ward', blank=True, null=True)  # Field name made lowercase.
    acp_ziekenhuis = models.FloatField(db_column='ACP_ziekenhuis', blank=True, null=True)  # Field name made lowercase.
    acp_ziekenhuis_ward = models.FloatField(db_column='ACP_ziekenhuis_ward', blank=True, null=True)  # Field name made lowercase.
    acp_anders = models.FloatField(db_column='ACP_anders', blank=True, null=True)  # Field name made lowercase.
    acp_anders_ward = models.FloatField(db_column='ACP_anders_ward', blank=True, null=True)  # Field name made lowercase.
    vbm_mechanisch = models.FloatField(db_column='VBM_Mechanisch', blank=True, null=True)  # Field name made lowercase.
    vbm_mechanisch_ward = models.FloatField(db_column='VBM_Mechanisch_ward', blank=True, null=True)  # Field name made lowercase.
    vbm_elektronisch = models.FloatField(db_column='VBM_elektronisch', blank=True, null=True)  # Field name made lowercase.
    vbm_elektronisch_ward = models.FloatField(db_column='VBM_elektronisch_ward', blank=True, null=True)  # Field name made lowercase.
    vbm_fysiek = models.FloatField(db_column='VBM_fysiek', blank=True, null=True)  # Field name made lowercase.
    vbm_fysiek_ward = models.FloatField(db_column='VBM_fysiek_ward', blank=True, null=True)  # Field name made lowercase.
    vbm_1op1toezicht = models.IntegerField(db_column='VBM_1op1toezicht', blank=True, null=True)  # Field name made lowercase.
    vbm_1op1toezicht_ward = models.IntegerField(db_column='VBM_1op1toezicht_ward', blank=True, null=True)  # Field name made lowercase.
    vbm_farmacologisch = models.FloatField(db_column='VBM_farmacologisch', blank=True, null=True)  # Field name made lowercase.
    vbm_farmacologisch_ward = models.FloatField(db_column='VBM_farmacologisch_ward', blank=True, null=True)  # Field name made lowercase.
    vbm_psychologisch = models.IntegerField(db_column='VBM_psychologisch', blank=True, null=True)  # Field name made lowercase.
    vbm_psychologisch_ward = models.IntegerField(db_column='VBM_psychologisch_ward', blank=True, null=True)  # Field name made lowercase.
    vbm_afzondering = models.IntegerField(db_column='VBM_afzondering', blank=True, null=True)  # Field name made lowercase.
    vbm_afzondering_ward = models.IntegerField(db_column='VBM_afzondering_ward', blank=True, null=True)  # Field name made lowercase.
    vbm_overig = models.FloatField(db_column='VBM_overig', blank=True, null=True)  # Field name made lowercase.
    vbm_overig_ward = models.FloatField(db_column='VBM_overig_ward', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LPZ2019V1'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
