# PERCENTAGE_INCREASE_ON_INVESTMENT = '50%'
# VAT_ON_WITHDRAWAL_AMOUNT = '7%'
# VAT_IS_CHARGED_ON_WALLET_BALANCE 

print('Welcome to Cohort 2 Investment Ltd')

username = input('Enter your name: ')
amount = input('Enter Investment Amount: ')

user_amount = int(amount)
total = user_amount * 0.50 + user_amount
commission = user_amount * 0.50
print('Your commssion is', commission)
print(username,'Congratulations your balance now is',total)

# SECTION TO MAKE WITHDRAWAL 

withdrawal_amount = input('Enter Withdrawal Amount: ')
withdraw = int(withdrawal_amount)
Balance = total - withdraw
vat = int(withdraw * 0.070)
current_balance = (total - vat) - withdraw

if withdraw >= total:
    print('Insufficient funds! Withraw amount must be less than current balance')
else:
    if vat <= Balance:
        print('your withdrawal amount is', withdraw)
        print('Balance before VAT is', Balance)
        print('VAT is', vat)
        print('Your current balance after VAT is',current_balance)
        print('WITHDRAWAL APPROVED !')
    else:   
        print('Your withdrawal amount is', withdraw)
        print('Balance before VAT is', Balance)
        print('VAT is', vat)
        print( username, 'your available balance', total, 'is Insuffient for VAT charge')
        print('WITHDRAWAL DENIED!')