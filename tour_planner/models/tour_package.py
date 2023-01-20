from datetime import date,datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo import models,fields,api

class tour_package(models.Model):
      _name = "tour.package"
      _description = "tour packages for all the customers"

      name=fields.Char(required=True)
      price=fields.Integer(required=True)
      tour_id=fields.Many2one('tour.admin')
      destination_ids=fields.Many2many('destination.list')
      # from_date=fields.Date(string="Register date",default=fields.Datetime.now(),inverse="_inverse_date_deadline")
      # final_date=fields.Date(string="Last date",default=fields.Datetime.now()+relativedelta(days=+1))
      # total_days=fields.Integer(compute="_compute_total_days",default=0)
      # @api.depends('from_date', 'final_date')
      
      # def _compute_total_days(self):
      #       for record in self:
      #             x=record.final_date-record.from_date
      #             record.total_days=x.days

      package_ids=fields.One2many('tour.booking','booking_id')
      
      # from_date = fields.Date(default=fields.Datetime.now())
      # final_date=fields.Date(string="Last date", compute="_compute_date_deadline",inverse="_inverse_date_deadline")
      
      # @api.depends('from_date', 'final_date')
      # def _compute_date_deadline(self): 
      #       for record in self:
      #             record.from_date = fields.Datetime.now()

      # def _inverse_date_deadline(self):
      #      for record in self:
      #            record.final_date = (record.from_date + fields.Datetime.now()+relativedelta(days=+3))

     
      start_date=fields.Date()
      end_date = fields.Date(
                            default=fields.datetime.now(),
                           compute="_compute_end_date",
                           inverse="_inverse_end_date")
      total_days=fields.Integer()

      @api.depends('start_date')
      def _compute_end_date(self):
            if self.check_in_date:
                  self.end_date = self.start_date + timedelta(
                  days=self.total_days)
      def _inverse_end_date(self):
            if self.check_out_date:
                   self.total_days = (self.end_date - self.start_date).days
            pass
                 
      
      

    
