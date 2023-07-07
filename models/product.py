from odoo import models, fields, api


class product_template_inherit(models.Model):
    _inherit = 'product.template'
    _description = 'Inheritance of Product Template Models'

    def action_test(self):
        print("<!----------General Information ------------!>")
        print("Product Type |",self.detailed_type)
        print("Invoicing Policy |",self.invoice_policy)
        print("Re invoice Expenses |",self.expense_policy)
        print("Product Tooltip |", self.product_tooltip)

        print("Sales price |", self.list_price)
        # taxes = self.taxes_id
        # for taxe in taxes :
        #     print("taxes |", taxe.display_name)
        print("Standard Price |", self.standard_price)
        print("Product Category |", self.categ_id.display_name)
        print("Internal Reference |", self.default_code)
        print("Barcode |", self.barcode)

        #print("Product Tags |")