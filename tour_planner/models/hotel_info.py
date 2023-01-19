from odoo import models,fields,api

class hotel_info(models.Model):
      _name = "hotel.info"
      _description = "this is for the book the hotel for the tourism"
      _order="name"
    
name=fields.Char(required=True)
adress=fields.char(required=True)
city=fields.Char(required=True)
state=fields.char()
avl_suitroom=fields.Integer()
avl_guestroom=fields.Integer()
total_rooms=fields.Integer(compute="_compute_total_room")

@api.depends('avl_suitroom','avl_guestroom')
def _compute_total_room(self):
    for record in self:
        record.total_rooms=record.avl_suitroom+record.avl_guestroom


