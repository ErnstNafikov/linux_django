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

class WeightNN(models.Model):
    w0 = models.FloatField()
    w1 = models.FloatField() 
    w2 = models.FloatField()
    w3 = models.FloatField()
    w4 = models.FloatField()
    w5 = models.FloatField()
    w6 = models.FloatField()
    w7 = models.FloatField()
    w8 = models.FloatField()
    w9 = models.FloatField()
    w10 = models.FloatField()
    
class BiasNN(models.Model):
    w0 = models.FloatField()
    w1 = models.FloatField() 
    w2 = models.FloatField()
    w3 = models.FloatField()
    w4 = models.FloatField()
    w5 = models.FloatField()
    w6 = models.FloatField()
    w7 = models.FloatField()
    w8 = models.FloatField()
    w9 = models.FloatField()
    w10 = models.FloatField()
    
class FraudScore(models.Model):
    EventDT = models.DateTimeField(auto_now_add=True)
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
    flg_fraud = models.IntegerField(null=True, default=None)
    
class Log(models.Model):
    EventDT = models.DateTimeField(auto_now_add=True)
    log = models.TextField()