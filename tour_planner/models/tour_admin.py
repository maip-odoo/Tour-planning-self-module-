from odoo import models,fields
class tour_admin(models.Model):
      _name = "tour.admin"
      _description = "Real estate based advertisedment module"

      name = fields.Char(required=True)  
      description = fields.Text()
      office_name = fields.Char(required=True)
      office_adress = fields.Char(required=True)
      total_tour = fields.Char()
      

