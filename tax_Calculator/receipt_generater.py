# Problem 1: Sales Tax 

# Basic sales tax is applicable at a rate of 10% on all goods, except books, food, and medical products that are exempt. 
# Import duty is an additional sales tax applicable on all imported goods at a rate of 5%, with no exemptions. 
# When I purchase items I receive a receipt which lists the name of all the items and their price (including tax), 
# finishing with the total cost of the items, and the total amounts of sales taxes paid. 
# The rounding rules for sales tax are that for a tax rate of n%, a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of sales tax. 
# Write an application in Python that prints out the receipt details for these shopping baskets. 


import math

EXEMPT_ITEMS = ("book", "food", "medical")
CATEGORIES = {
    "book": ["book"],
    "food": ["chocolate", "biscuit", "bread", "milk", "chips", "snack", "bar", "cheese", "coffee", "tea"],
    "medical": ["pill", "headache", "medicine", "tablet"]
}

def round_tax(tax):
    return math.ceil(tax * 20) / 20.0

def get_category(item_name):
    item_name = item_name.lower()
    for category, keywords in CATEGORIES.items():
        if any(keyword in item_name for keyword in keywords):
            return category
    return "general"

def is_exempt(item_name):
	return get_category(item_name) in EXEMPT_ITEMS

# Function to parse the input list and extract item details 
# The input method or the formate is not defined in the problem statement so i'm using the same format as the sample
def parse_input(input_list):
	try:
		parsed_item = []
		for item in input_list:
			parts = item.rsplit(" at ",1)
			if len(parts) != 2:
				continue

			left_part, right_part = parts
			price = float(right_part)
			quantity_str, *name_parts = left_part.strip().split(" ")
			quantity = int(quantity_str)
			name = " ".join(name_parts)
			imported = "imported" in name.lower()

			parsed_item.append({
		        "name": name,
		        "quantity": quantity,
		        "price": price,
		        "imported": imported,
		        "exempt": is_exempt(name.lower())
		    })
	except Exception as parseError:
		print("Error - Parsing the input", parseError)

	return(parsed_item)

# Function to generate the receipt by calculating the total price and tax
def generate_receipt(items):
	total_tax = 0
	total_price = 0
	receipt_lines = []

	for item in items:
		tax_rate = 0
		if not item["exempt"]:
			tax_rate += 0.10
		if item["imported"]:
			tax_rate += 0.05

		raw_tax = item["price"] * tax_rate
		tax = round_tax(raw_tax)
		total_item_price = item["price"] + tax

		total_tax += tax
		total_price += total_item_price

		receipt_lines.append(f'{item["quantity"]} {item["name"]}: {total_item_price:.2f}')

	receipt_lines.append(f"Sales Taxes: {total_tax:.2f}")
	receipt_lines.append(f"Total: {total_price:.2f}")
	return receipt_lines

def main():
	# Sample input 1
	input1 = ["1 book at 12.49","1 music CD at 14.99", "1 chocolate bar at 0.85"]
	items = parse_input(input1)
	receipt = generate_receipt(items)
	print(f"\nReceipt 1 \n")
	for item in receipt:
		print(item)
	
	# Sample input 2
	input2 = ["1 imported box of chocolates at 10.00","1 imported bottle of perfume at 47.50"]
	items = parse_input(input2)
	receipt = generate_receipt(items)
	print(f"\nReceipt 2 \n")
	for item in receipt:
		print(item)
	
	# Sample input 3
	input3 = ["1 imported bottle of perfume at 27.99", "1 bottle of perfume at 18.99", "1 packet of headache pills at 9.75", "1 box of imported chocolates at 11.25"]
	items = parse_input(input3)
	receipt = generate_receipt(items)
	print(f"\nReceipt 3 \n")
	for item in receipt:
		print(item)

# The flow starts here
if __name__ == "__main__":
    main()