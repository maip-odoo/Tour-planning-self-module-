from odoo import models,fields

class tour_booking(models.Model):
    _name='tour.booking'
    _description='this is for booking the tour'

    name=fields.Char(required=True)
    adress=fields.Char(required=True)
    contact_no=fields.Integer(required=True)
    # package_ids=fields.One2many('tour.package','booking_id')
    booking_id=fields.Many2one('tour.package')
