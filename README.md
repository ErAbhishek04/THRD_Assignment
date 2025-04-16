# Price Adjustment Script

## Description

This script adjusts product prices based on inventory and sales performance. It uses business rules with defined priorities and enforces a minimum profit margin of 20%.

## The Code Logic

1. We use pandas to read `products.csv` and `sales.csv` into DataFrames.
2. `merged_df` combines both datasets on `sku` so we can access all info per product.
3. Missing sales data (NaN) is filled with 0 to avoid calculation errors.
4. We use `.apply()` on `merged_df` with a custom function to process each row.
5. Inside the function, we apply pricing rules in order of priority.
6. Only the first matching rule among Rule 1–3 is applied.
7. Rule 4 ensures the final price gives at least 20% profit margin.
8. We round the final computed price to 2 decimal places using `round()`.
9. We use `lambda` functions to format prices with a dollar sign (`$`).
10. `lambda` is a quick way to define simple inline formatting functions.
11. Only the necessary columns (`sku`, `old_price`, `new_price`) are selected.
12. Finally, we write the result to `result_prices.csv` using `to_csv()`.


## Pricing Logic

1. **Rule 1 – Low Stock, High Demand**: +15%
2. **Rule 2 – Dead Stock**: -30%
3. **Rule 3 – Overstocked**: -10%
4. **Rule 4 – Minimum Profit**: Final price must be ≥ cost_price × 1.2

Only one of Rules 1–3 is applied per product. Rule 4 is always applied afterward.

## Input Files

- `products.csv`: SKU, product name, current price, cost price, stock
- `sales.csv`: SKU, quantity sold in past 30 days
  **(Note : Make sure that you have both the files in same directory as python code)**

## Output

- `result_prices.csv`: Contains `sku`, `old_price`, and `new_price` with `$` units

## Run Instructions

```bash
python pricing_rules.py
