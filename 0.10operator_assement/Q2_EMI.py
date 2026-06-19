mobile_price=30000
down_payment=5000
interest_rate=10
months=10
remainging_amount=mobile_price-down_payment
total_with_interest=remainging_amount+(remainging_amount*interest_rate)//100
monthly_emi=total_with_interest/months
print(f"the remainging amount={remainging_amount} \n the toatl with interest={total_with_interest}\n monthly emi={monthly_emi}")