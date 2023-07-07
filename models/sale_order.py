# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sales_order_inherit(models.Model):
    _inherit = 'sale.order'
    _description = 'Inheritance of Sale Order Models'

    def action_confirm(self):

        print("it is action confirm")
        return super(sales_order_inherit,self).action_confirm()

    def action_test(self):
        print("customer", self.partner_id.display_name)
        print("expiration", self.validity_date)
        print("quotation date", self.date_order)
        print("payment_terms", self.payment_term_id.display_name)
        print("state",self.state)

        print("<!--------------------Orderline--------------------------->")

        products = self.order_line

        for product in products:
            print(product)
            print("product_name |",product.product_template_id.display_name)
            print("description |",product.name)
            print("quantity |", product.product_uom_qty)
            print("Unit Price |", product.price_unit)
            print("taxes |",product.tax_id.display_name)
            print("subtotal |",product.price_subtotal)
            print("-----------------------------------------")
        print("<!--------------------Optionals Products --------------------------->")
        options = self.sale_order_option_ids

        for option in options :
            print(option)
            print("product_name |", option.product_id.name)
            print("description |", option.name)
            print("quantity |", option.quantity)
            print("Unit Price |", option.price_unit)

            print("-----------------------------------------")

        # sale_order_option_ids