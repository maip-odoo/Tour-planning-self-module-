from odoo import models,fields,api

class tour_hotel(models.Model):
      _name = "tour.hotel"
      _description = "this is for the book the hotel for the tourism"
      _order="name"
    
      name=fields.Char(required=True)
      image=fields.Image()
      adress=fields.Char(required=True)
      city=fields.Char(required=True)
      state=fields.Char()
      avl_suitroom=fields.Integer(default=3)
      avl_guestroom=fields.Integer(default=10)
      total_rooms=fields.Integer(compute="_compute_total_room")
      suit_images=fields.Image()
      guest_images=fields.Image()

      @api.depends('avl_suitroom','avl_guestroom')
      def _compute_total_room(self):
       for record in self:
        record.total_rooms=record.avl_suitroom + record.avl_guestroom


