import pandas as pd
from faker import Faker
import random
import os

# Directory for saving data
data_dir = '/Users/anthonytatis/gitfolder/publicstash/open_source_project/coffee-shop-data-viz/data/raw_data'
os.makedirs(data_dir, exist_ok=True)

# Initialize Faker
fake = Faker()

# Number of records to generate
num_records = 100
num_employees = 9  # Less than 10 employees

# Coffee shop-specific lists
coffee_types = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha', 'Macchiato']
pastries = ['Croissant', 'Muffin', 'Doughnut', 'Scone', 'Bagel']
staff_roles = ['Barista', 'Manager', 'Chef', 'Waitstaff', 'Cleaner']
unit_of_measure = ['kg', 'g', 'ml', 'liter']
ingredient_list = [
    {'name': 'Espresso Beans', 'unit': 'kg'},
    {'name': 'Milk', 'unit': 'liter'},
    {'name': 'Chocolate Syrup', 'unit': 'ml'},
    {'name': 'Whipped Cream', 'unit': 'ml'},
    {'name': 'Sugar', 'unit': 'g'},
    {'name': 'Flour', 'unit': 'kg'},
    {'name': 'Butter', 'unit': 'g'},
    {'name': 'Yeast', 'unit': 'g'},
    {'name': 'Eggs', 'unit': 'pcs'},
    {'name': 'Salt', 'unit': 'g'},
    {'name': 'Water', 'unit': 'liter'},
    # Add more ingredients as needed
]

# Map products to ingredients
product_ingredients_map = {
    'Espresso': ['Espresso Beans', 'Water'],
    'Latte': ['Espresso Beans', 'Milk'],
    'Cappuccino': ['Espresso Beans', 'Milk', 'Whipped Cream'],
    'Americano': ['Espresso Beans', 'Water'],
    'Mocha': ['Espresso Beans', 'Milk', 'Chocolate Syrup', 'Whipped Cream'],
    'Macchiato': ['Espresso Beans', 'Milk', 'Whipped Cream'],
    'Croissant': ['Flour', 'Butter', 'Yeast', 'Salt', 'Water'],
    'Muffin': ['Flour', 'Sugar', 'Eggs', 'Milk', 'Butter'],
    'Doughnut': ['Flour', 'Sugar', 'Yeast', 'Milk', 'Butter'],
    'Scone': ['Flour', 'Sugar', 'Eggs', 'Milk', 'Butter'],
    'Bagel': ['Flour', 'Yeast', 'Salt', 'Water']
    # Add more products and their ingredients as needed
}

# Generate Customers
def generate_customers(num_records):
    return [{
        'customer_id': _ + 1,
        'name': fake.name(),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'address_id': random.randint(1, num_records),
        'registration_date': fake.date_this_decade(),
        'loyalty_points': random.randint(0, 100)
    } for _ in range(num_records)]

# Generate Addresses
def generate_addresses(num_records):
    return [{
        'address_id': _ + 1,
        'street': fake.street_address(),
        'city': 'Austin',
        'state': 'Texas',
        'postal_code': fake.zipcode_in_state('TX'),
        'country': 'USA'
    } for _ in range(num_records)]

# Generate Items
def generate_items(num_records):
    items = []
    for _ in range(num_records):
        category = random.choice(['Coffee', 'Pastry', 'Sandwich', 'Beverage'])
        name = random.choice(coffee_types) if category == 'Coffee' else random.choice(pastries)
        items.append({
            'item_id': _ + 1,
            'item_name': name,
            'item_category': category,
            'price': round(random.uniform(1.0, 10.0), 2)
        })
    return items

# Generate Ingredients
def generate_ingredients():
    return [{
        'ingredient_id': i + 1,
        'ingredient_name': ingredient['name'],
        'unit_of_measure': ingredient['unit'],
        'stock_quantity': round(random.uniform(1.0, 100.0), 2),
        'cost_per_unit': round(random.uniform(0.5, 5.0), 2)
    } for i, ingredient in enumerate(ingredient_list)]

# Generate Recipes
def generate_recipes(items):
    recipes = []
    for item in items:
        if item['item_name'] in product_ingredients_map:
            ingredients = product_ingredients_map[item['item_name']]
            for ingredient_name in ingredients:
                ingredient_id = next(
                    (i['ingredient_id'] for i in ingredients_df.to_dict('records') if i['ingredient_name'] == ingredient_name),
                    None
                )
                if ingredient_id is not None:
                    recipes.append({
                        'recipe_id': len(recipes) + 1,
                        'item_id': item['item_id'],
                        'ingredient_id': ingredient_id,
                        'quantity': round(random.uniform(0.1, 1.0), 2)
                    })
    return recipes

# Generate Inventory
def generate_inventory(ingredients):
    return [{
        'inventory_id': i + 1,
        'ingredient_id': ingredient['ingredient_id'],
        'quantity': ingredient['stock_quantity'],
        'last_updated': fake.date_this_year()
    } for i, ingredient in enumerate(ingredients)]

# Generate Staff
def generate_staff(num_records):
    return [{
        'staff_id': _ + 1,
        'name': fake.name(),
        'role': random.choice(staff_roles),
        'email': fake.email(),
        'phone': fake.phone_number()
    } for _ in range(num_records)]

# Generate Shifts
def generate_shifts(num_records):
    return [{
        'shift_id': _ + 1,
        'shift_start_time': fake.time(),
        'shift_end_time': fake.time()
    } for _ in range(num_records)]

# Generate Rota
def generate_rota(num_records):
    return [{
        'rota_id': _ + 1,
        'staff_id': random.randint(1, num_employees),
        'shift_id': random.randint(1, num_records),
        'start_date': fake.date_this_month(),
        'end_date': fake.date_this_month()
    } for _ in range(num_records)]

# Generate Roles
def generate_roles(num_records):
    coffee_shop_roles = ['Barista', 'Manager', 'Chef', 'Waitstaff', 'Cleaner', 'Cashier', 'Supervisor', 'Roaster']
    return [{
        'role_id': _ + 1,
        'role_name': random.choice(coffee_shop_roles),
        'description': fake.sentence(nb_words=6)
    } for _ in range(num_records)]

# Generate User Role Assignments
def generate_user_role_assignments(num_records):
    return [{
        'assignment_id': _ + 1,
        'user_id': random.randint(1, num_employees),
        'role_id': random.randint(1, num_records),
        'assignment_date': fake.date_this_year()
    } for _ in range(num_records)]

# Generate Orders
def generate_orders(num_records, num_customers):
    return [{
        'order_id': _ + 1,
        'customer_id': random.randint(1, num_customers),
        'order_date': fake.date_this_year(),
        'total_amount': round(random.uniform(5.0, 50.0), 2)
    } for _ in range(num_records)]

# Generate Order Items
def generate_order_items(num_records, num_orders, num_items):
    return [{
        'order_item_id': _ + 1,
        'order_id': random.randint(1, num_orders),
        'item_id': random.randint(1, num_items),
        'quantity': random.randint(1, 5),
        'price': round(random.uniform(1.0, 10.0), 2)
    } for _ in range(num_records)]

# Create DataFrames
customers_df = pd.DataFrame(generate_customers(num_records))
addresses_df = pd.DataFrame(generate_addresses(num_records))
items_df = pd.DataFrame(generate_items(num_records))
ingredients_df = pd.DataFrame(generate_ingredients())
recipes_df = pd.DataFrame(generate_recipes(items_df.to_dict('records')))
inventory_df = pd.DataFrame(generate_inventory(ingredients_df.to_dict('records')))
staff_df = pd.DataFrame(generate_staff(num_employees))
shifts_df = pd.DataFrame(generate_shifts(num_records))
rota_df = pd.DataFrame(generate_rota(num_records))
roles_df = pd.DataFrame(generate_roles(num_employees))
assignments_df = pd.DataFrame(generate_user_role_assignments(num_employees))
orders_df = pd.DataFrame(generate_orders(num_records, num_records))
order_items_df = pd.DataFrame(generate_order_items(num_records, num_records, num_records))

# Save DataFrames to CSV
customers_df.to_csv(os.path.join(data_dir, 'customers.csv'), index=False)
addresses_df.to_csv(os.path.join(data_dir, 'addresses.csv'), index=False)
items_df.to_csv(os.path.join(data_dir, 'items.csv'), index=False)
ingredients_df.to_csv(os.path.join(data_dir, 'ingredients.csv'), index=False)
recipes_df.to_csv(os.path.join(data_dir, 'recipes.csv'), index=False)
inventory_df.to_csv(os.path.join(data_dir, 'inventory.csv'), index=False)
staff_df.to_csv(os.path.join(data_dir, 'staff.csv'), index=False)
shifts_df.to_csv(os.path.join(data_dir, 'shifts.csv'), index=False)
rota_df.to_csv(os.path.join(data_dir, 'rota.csv'), index=False)
roles_df.to_csv(os.path.join(data_dir, 'roles.csv'), index=False)
assignments_df.to_csv(os.path.join(data_dir, 'assignments.csv'), index=False)
orders_df.to_csv(os.path.join(data_dir, 'orders.csv'), index=False)
order_items_df.to_csv(os.path.join(data_dir, 'order_items.csv'), index=False)

print("Data generation complete!")
