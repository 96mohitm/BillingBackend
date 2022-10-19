class OrderBuilder:
    def order_meta_data_builder(order_request):
        return {
            "customer_name": order_request["customer_name"],
            "contact_number": order_request["contact_number"],
            "discount_percentage": order_request["discount_percentage"]
        }

    def order_item_list_builder(order_request):
        return order_request["item_list"]