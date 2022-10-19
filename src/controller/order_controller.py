from exception.out_of_stock import OutOfStockException
from models.inventory_model import InventoryModel
from models.order_item_model import OrderItemModel
from models.order_model import OrderModel


class OrderController():

    def _update_inventory(self, item_list):
        for item in item_list:
            # get the inventory row.
            inventory = InventoryModel.find_by_product_id_batch_id(item["product_id"], item["batch_id"])
            # check if the stock is available.
            if inventory.quantity < item["quantity"]:
                raise OutOfStockException("In inventory the quantity is less.", {"item": item})
            inventory.quantity -= item["quantity"]
            inventory.update_to_db()

        return None

    def place_order(self, order_meta_data, item_list):
        # update the quantity in inventory.
        try:
            self._update_inventory(item_list)
        except OutOfStockException as ex:
            raise ex
        # add a entry in the order table.
        order = OrderModel(
                customer_name=order_meta_data["customer_name"],
                contact=order_meta_data["contact_number"],
                discount_percentage=order_meta_data["discount_percentage"]
                )
        order_item_list = []
        for item in item_list:
            curr_item = OrderItemModel(
                item["product_id"], 
                item["batch_id"],
                )
            order_item_list.append(curr_item)
        if len(order_item_list) == 0:
            raise Exception("item list is empty")
        order.order_item_list = order_item_list
        order.save_to_db()
        return order
