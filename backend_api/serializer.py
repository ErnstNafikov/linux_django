from rest_framework import serializers
from .models import FraudScore

class FraudScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FraudScore
        fields = ['flg_contry_usr', 'flg_contry_card', 'flg_contry_lng', 'flg_big_tr', 'flg_small_tr', 'flg_chg_card', 'flg_chg_contry', 'flg_nigth', 'flg_rep_tr', 'flg_bank_decl']