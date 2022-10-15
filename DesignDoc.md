# Billing Software
## Functional Requirements:

1. Add inventory
1. Add sales history
1. Show ledger
1. Show Product Details
1. Reminder of Products to the customer via whatsapp/sms
1. A website link to share with the user to see the list and invoice for a purchase.

## Non-functional Requirement:
-

## SQL tables:

- Inventory Table:
  id, product, quantity, group_id(eg medsbull), …

- invoice table.(stores list of sales)

  id, group_id, customer_id, ,...

sales_product_quantity

Customer table

Product_detail
product_id, name, other details.

ledger table - will be updated when we are changing anything in inventory.

reminder_table.


## APIs:
### INVENTORY

get_inventory - GET
add_inventory - POST
search_product - {keyword} return a list of products.
add_product - POST
get_product_list - GET

### SALES

get_sales - GET
add_sales - POST return a invoice_id
get_invoice - {invoice_id} return a website which is the bill, or we can direct print it in backend and then save the pdf in s3 and return the url of saved bill. or we can generator pdfs using libraries.

### Show ledger

get_ledger - GET
Show Product Details
get_product_details
get_product_list
Reminder to the customer
we need a cron job which will keep on running and reading the reminder table.
add_reminder - POST
Shareable website link
create a shareable website link with a invoice _id


14 apis
Other things to include:
- Login, logout and signup
