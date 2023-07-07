from odoo import models, fields, api


class res_partner_inherit(models.Model):
    _inherit = 'res.partner'
    _description = 'Inheritance of Res Partner Models'

    def action_test(self):
        print("<!------------GENERAL-------------!>")
        # print("address",self.address)
        print("vat",self.vat)
        print("phone",self.phone)
        print("mobile",self.mobile)
        print("email",self.email)
        print("website",self.website)
        for x in self.category_id :
            print("tags",x.display_name)

        print("<!----------Sales & Purchase ------------!>")
        print("salesperson", self.user_id.display_name)
        print("sales team",self.team_id.display_name)
        print("payment terms",self.property_payment_term_id.display_name)
        print("pricelist",self.property_product_pricelist.display_name)

        print("<!------------- Purchase ------------!>")
        print("payment term",self.property_supplier_payment_term_id.display_name)

        print("<!------------- Fiscal Information  ------------!>")
        print("fiscal position", self.property_account_position_id.display_name)