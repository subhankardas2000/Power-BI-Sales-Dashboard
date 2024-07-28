import pandas as pd
import random

# Order IDs
order_ids = [f'PHS2024{i:03}' for i in range(1, 1000)]

# Amounts
amounts = [random.randint(10000, 120000) for _ in range(999)]

# Profits (5% to 25% of Amount)
profits = [round(amount * random.uniform(0.05, 0.25), 2) for amount in amounts]

# Quantities
quantities = [random.randint(1, 100) for _ in range(999)]

# Categories and Sub-Categories
categories = {
    'Paints': ['Asian Paint', 'Barzer', 'Tata Colors', 'Birla Opus'],
    'TMT Bar': ['Shyam Steel', 'Tata TMT', 'Elegant'],
    'Cements': ['Tata', 'Ambuja', 'Concreto', 'Emami Double'],
    'Bricks': ['Regular', 'Fly Ash'],
    'Furnitures': ['Door', 'Window', 'Table', 'Chair']
}
category_list = []
subcategory_list = []
for _ in range(999):
    category = random.choice(list(categories.keys()))
    subcategory = random.choice(categories[category])
    category_list.append(category)
    subcategory_list.append(subcategory)

# Payment Modes
payment_modes = ['Cash', 'EMI', 'Credit Card', 'Debit Card', 'Cheque', 'Bank Draft', 'BHIM UPI']
payment_mode_list = [random.choice(payment_modes) for _ in range(999)]

# Create DataFrame
data = {
    'Order ID': order_ids,
    'Amount': amounts,
    'Profit': profits,
    'Quantity': quantities,
    'Category': category_list,
    'Sub-Category': subcategory_list,
    'Payment Mode': payment_mode_list
}

df_new = pd.DataFrame(data)

# Save to Excel
file_path_new = '/mnt/data/demo_sales.xlsx'
df_new.to_excel(file_path_new, index=False)
file_path_new
