Obstacle Log

Project: Food Delivery Order Processor

During the development of this project, I encountered the following challenges and addressed them using Python concepts.

1. Calculating Order Totals

Obstacle: Calculating the total price when an order contains multiple food items with different quantities.

Solution: Used dictionary iteration to retrieve the price of each item and multiply it by the ordered quantity.

2. Applying Discounts

Obstacle: Applying discounts only when an order reaches the specified minimum value.

Solution: Implemented conditional statements to check whether the subtotal is Rs. 500 or more before applying a 10% discount.

3. Handling Invalid Orders

Obstacle: Orders containing unavailable menu items, invalid quantities, or no items could cause incorrect calculations.

Solution: Added validation conditions to identify invalid menu items, non-positive quantities, and empty orders. Invalid orders are skipped with appropriate error messages.

4. Identifying the Highest-Value Order

Obstacle: Comparing multiple orders to identify the order with the highest final bill.

Solution: Used a variable to track the highest order value and updated it whenever a higher-value order was encountered.

5. Generating the Sales Report

Obstacle: Storing calculated sales information permanently instead of displaying it only in the terminal.

Solution: Used Python file handling with write mode to generate a sales report containing the total number of processed orders, total revenue, and highest-value order.

Conclusion

This project helped me understand and practically implement Python dictionaries, lists, functions, loops, conditional statements, JSON handling, validation, and file operations.