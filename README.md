# Power-BI-Sales-Dashboard
Sales Dashboard for Pahari Home Solutions Private Limited using Power BI

# Pahari Home Solutions Private Limited - Sales Dashboard

This repository contains sample data for creating a sales dashboard using Power BI for Pahari Home Solutions Private Limited. The data is organized in two Excel files: `updated_demo_orders.xlsx` and `demo_sales.xlsx`.

## Files

### `updated_demo_orders.xlsx`

This file contains information about customer orders. The columns included are:

- **Order ID**: Unique identifier for each order (PHS2024001 to PHS2024999).
- **Order Date**: Date of the order (from January 1, 2024, to December 31, 2024).
- **Customer Name**: Randomly generated names resembling those common in West Bengal.
- **District**: Districts in West Bengal where the orders were placed.
- **Village**: Villages corresponding to the districts.

### `demo_sales.xlsx`

This file contains sales-related data corresponding to the orders in `updated_demo_orders.xlsx`. The columns included are:

- **Order ID**: Matches the Order ID in `updated_demo_orders.xlsx`.
- **Amount**: Random value between ₹10,000 and ₹120,000.
- **Profit**: Random value between 5% and 25% of the Amount.
- **Quantity**: Random integer representing the quantity of items ordered.
- **Category**: Category of the items ordered (e.g., Paints, TMT Bar, Cements, Bricks, Furnitures).
- **Sub-Category**: Sub-category of the items corresponding to the category.
- **Payment Mode**: Payment mode used for the order (e.g., Cash, EMI, Credit Card, Debit Card, Cheque, Bank Draft, BHIM UPI).

## Usage

1. **Power BI Dashboard Creation**:
   - Load the Excel files into Power BI.
   - Establish a relationship between the two tables using the `Order ID` column.
   - Create visualizations and reports to analyze sales performance, customer distribution, and other key metrics.

2. **Data Analysis**:
   - Use the provided data to perform various analyses such as sales trends, profit margins, category-wise sales distribution, and payment mode preferences.

## Company Information

**Pahari Home Solutions Private Limited** is a real estate company focusing on providing quality building materials and home solutions. The data provided here is fictional and intended for demonstration purposes only.

## License

This project is licensed under the MIT License.
