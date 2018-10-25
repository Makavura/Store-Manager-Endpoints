
sales = []


class Sales(object):
    def __init__(self, attendant, sale_id):
        self.attendant = attendant
        self.sale_id = sale_id

    def create_sale(self):
        new_sale_info= {}
        new_sale_info['product_id'] = len(sales) + 1
        new_sale_info['attendant'] = self.attendant
        sales.append(new_sale_info)
        return new_sale_info

    def get_sales(self):
        return sales

    def get_sale(self, sale_id):
        sale = [sale for sale in sales if sale['sale_id'] == sale_id]
        return make_response(jsonify({'sale': sale[0]}), 200)

