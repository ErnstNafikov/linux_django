from rest_framework import serializers
from .models import DataSet

class DataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = ['flg_contry_usr', 'flg_contry_card', 'flg_contry_lng', 'flg_big_tr', 'flg_small_tr', 'flg_chg_card', 'flg_chg_contry', 'flg_nigth', 'flg_rep_tr', 'flg_bank_decl', 'flg_fraud']