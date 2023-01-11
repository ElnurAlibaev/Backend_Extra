from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)  # Добавляется автоматически при создании 
    updated_at = models.DateTimeField(auto_now=True)  # Добавляется автоматически при обновлении

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#account.wallet_set.all() - чтобы через аккаунт дойти до его кошельков

class Wallet(models.Model):
    account = models.ForeignKey( # Foreign key- One to Many
        to=Account,
        on_delete=models.SET_NULL,  #есть также CASCADE, PROTECT, SET_NULL ставит null при удалении
        null=True, # должен ставиться если SET_NULL
        related_name='wallets'  # теперь пишется не wallet_set, а wallets
    )
    
    amount = models.DecimalField(max_digits=14, decimal_places=2)  # 1- макс. колво цифр, 2- колво цифр после запятой
    amount_currency = models.CharField(max_length=3)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Чтобы создать переменную типа wallet в shell:
# wallet1= Wallet(amount=1000.00, amount_currency='KZT', account=account1) 
# либо можно передать account_id
# wallet1.save()
# account1 был создан и сохранён как переменная заранее
