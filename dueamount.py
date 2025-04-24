bill_amount = float(input("Enter total bill amount "))
payment = float(input("Enter amount paid by customer "))
due_amount = bill_amount - payment
if due_amount > 0:
    print(f"The customer has to pay {due_amount:.2f}")