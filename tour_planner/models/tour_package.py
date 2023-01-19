from datetime import date,datetime
from dateutil.relativedelta import relativedelta
from odoo import models,fields,api

class tour_package(models.Model):
      _name = "tour.package"
      _description = "tour packages for all the customers"

      name=fields.Char(required=True)
      price=fields.Integer(required=True)
      tour_id=fields.Many2one('tour.admin')
      destination_ids=fields.Many2many('destination.list')
      from_date=fields.Date(string="Register date",default=fields.Datetime.now())
      final_date=fields.Date(string="Last date",default=fields.Datetime.now()+relativedelta(days=+1))
      total_days=fields.Integer(compute="_compute_total_days",default=0)
      @api.depends('from_date', 'final_date')
      
      def _compute_total_days(self):
            for record in self:
                  x=record.final_date-record.from_date
                  record.total_days=x.days
      # booking_id=fields.Many2one('tour.booking')
      package_ids=fields.One2many('tour.booking','booking_id')
                 
      
      

    
