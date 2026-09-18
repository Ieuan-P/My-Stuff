# Program to calculate total cost with discount

items = ["apple", "banana", "chocolate"]
prices = [0.99, 0.50, 1.20]
discount = 10  # 10% discount

total = 0

for i in range(0, len(items)):
    total = total + prices[i]

if total > 2.00:
    discount_amount = total * discount / 100
    final_total = total - discount_amount
else:
    discount_amount = 0
               
final_total = total - discount_amount

print("Total cost before discount: ", total)
print("Discount applied: ", discount_amount)
print("Final total: ", final_total)
