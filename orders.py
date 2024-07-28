import pandas as pd
import random
from faker import Faker

fake = Faker('en_IN')

# Generate Order IDs
order_ids = [f'PHS2024{i:03}' for i in range(1, 1000)]

# Generate Order Dates
order_dates = pd.date_range(start='2024-01-01', end='2024-12-31').to_pydatetime().tolist()

# Generate Customer Names
customer_names = [fake.name() for _ in range(999)]

# Generate Districts and Villages
districts = [
    'Purba Medinipur', 'Paschim Medinipur', 'Purulia', 'Bardhaman', 'Bankura', 'Birbhum',
    'Nadia', 'Murshidabad', 'Hooghly', 'North 24 Parganas', 'South 24 Parganas', 'Howrah'
]

villages_dict = {
    'Purba Medinipur': ['Tamluk', 'Argoal', 'Itaberia', 'Tikrapara', 'Contai', 'Digha', 'Kharai', 'Egra'],
    'Paschim Medinipur': ['Midnapore', 'Kharagpur', 'Salboni', 'Jhargram', 'Garhbeta'],
    'Purulia': ['Purulia', 'Jhalda', 'Raghunathpur', 'Adra', 'Barabhum'],
    'Bardhaman': ['Bardhaman', 'Asansol', 'Durgapur', 'Katwa', 'Kalna'],
    'Bankura': ['Bankura', 'Bishnupur', 'Sonamukhi', 'Khatra', 'Indpur'],
    'Birbhum': ['Suri', 'Rampurhat', 'Bolpur', 'Nalhati', 'Sainthia'],
    'Nadia': ['Krishnanagar', 'Ranaghat', 'Kalyani', 'Tehatta', 'Nakashipara'],
    'Murshidabad': ['Baharampur', 'Jangipur', 'Lalbagh', 'Beldanga', 'Domkal'],
    'Hooghly': ['Chinsurah', 'Serampore', 'Arambagh', 'Chandannagar', 'Tarakeswar'],
    'North 24 Parganas': ['Barasat', 'Bongaon', 'Basirhat', 'Barrackpore', 'Dumdum'],
    'South 24 Parganas': ['Alipore', 'Diamond Harbour', 'Canning', 'Baruipur', 'Sonarpur'],
    'Howrah': ['Howrah', 'Shibpur', 'Uluberia', 'Bagnan', 'Domjur']
}

# Generate District and Village combinations
district_list = []
village_list = []
for _ in range(999):
    district = random.choice(districts)
    village = random.choice(villages_dict[district])
    district_list.append(district)
    village_list.append(village)

# Create DataFrame
data = {
    'Order ID': order_ids,
    'Order Date': random.choices(order_dates, k=999),
    'Customer Name': customer_names,
    'District': district_list,
    'Village': village_list
}

df = pd.DataFrame(data)

# Save to Excel
file_path = '/mnt/data/updated_demo_orders.xlsx'
df.to_excel(file_path, index=False)
file_path
