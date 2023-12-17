from django.db import models
from django.conf import settings

class DataSet(models.Model):
    flg_contry_usr = models.BooleanField()
    flg_contry_card = models.BooleanField()
    flg_contry_lng = models.BooleanField()
    flg_big_tr = models.BooleanField()
    flg_small_tr = models.BooleanField()
    flg_chg_card = models.BooleanField()
    flg_chg_contry = models.BooleanField()
    flg_nigth = models.BooleanField()
    flg_rep_tr = models.BooleanField()
    flg_bank_decl = models.BooleanField()
    flg_fraud = models.BooleanField()