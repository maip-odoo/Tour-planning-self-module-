from odoo import models,fields

class destination_list(models.Model):
      _name = "destination.list"
      _description = "this is for the destination package"
      _order="name"

      _sql_constraints =[                                                                                      
    
        ('name', 'unique(name)', "A tag name must be unique...!"),
      ]

      name = fields.Char(required=True)
      color=fields.Integer('color')