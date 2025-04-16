# Price Adjustment Script

## Description

This script adjusts product prices based on inventory and sales performance. It uses business rules with defined priorities and enforces a minimum profit margin of 20%.

## Pricing Logic

1. **Rule 1 – Low Stock, High Demand**: +15%
2. **Rule 2 – Dead Stock**: -30%
3. **Rule 3 – Overstocked**: -10%
4. **Rule 4 – Minimum Profit**: Final price must be ≥ cost_price × 1.2

Only one of Rules 1–3 is applied per product. Rule 4 is always applied afterward.

## Input Files

- `products.csv`: SKU, product name, current price, cost price, stock
- `sales.csv`: SKU, quantity sold in past 30 days

## Output

- `updated_prices.csv`: Contains `sku`, `old_price`, and `new_price` with `$` units

## Run Instructions

```bash
python pricing_rules.py
