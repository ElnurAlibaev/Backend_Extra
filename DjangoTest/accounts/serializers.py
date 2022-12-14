from rest_framework import serializers
from accounts import models


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Wallet
        fields = '__all__'


class _AccountWalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Wallet
        fields = (
            'id',
            'amount',
            'amount_currency',
        )


class AccountSerializer(serializers.ModelSerializer):
    # wallets = _AccountWalletSerializer(read_only=True, many=True) при отображении аккаунта, покажутся вся инфа о его кошельках
    # wallets = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = models.Account
        fields = '__all__'


