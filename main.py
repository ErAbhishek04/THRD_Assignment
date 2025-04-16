import pandas as pd

# Read input CSVs
products_df = pd.read_csv('products.csv')
sales_df = pd.read_csv('sales.csv')

# Merge on SKU
merged_df = pd.merge(products_df, sales_df, on='sku', how='left')
merged_df['quantity_sold'] = merged_df['quantity_sold'].fillna(0)

def apply_pricing_rules(row):
    old_price = row['current_price']
    cost_price = row['cost_price']
    stock = row['stock']
    quantity_sold = row['quantity_sold']
    new_price = old_price

    # Rule 1
    if stock < 20 and quantity_sold > 30:
        new_price = old_price * 1.15
    # Rule 2
    elif stock > 200 and quantity_sold == 0:
        new_price = old_price * 0.7
    # Rule 3
    elif stock > 100 and quantity_sold < 20:
        new_price = old_price * 0.9

    # Rule 4 – Minimum Profit
    min_allowed = cost_price * 1.2
    if new_price < min_allowed:
        new_price = min_allowed

    return round(new_price, 2)

# Compute new prices
merged_df['new_price'] = merged_df.apply(apply_pricing_rules, axis=1)

# Add dollar units
merged_df['old_price'] = merged_df['current_price'].apply(lambda x: f"${x:.2f}")
merged_df['new_price'] = merged_df['new_price'].apply(lambda x: f"${x:.2f}")

# Save output
output_df = merged_df[['sku', 'old_price', 'new_price']]
output_df.to_csv('result_prices.csv', index=False)
print("✅ result_prices.csv generated.")
