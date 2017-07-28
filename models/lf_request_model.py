# -*- coding: utf-8 -*-

from odoo import  models,fields,api
from odoo.exceptions import ValidationError


class LfRequest(models.Model):
    _name = 'lf.request'
    
    
    req_num = fields.Char(string='Request ID',readonly=True, store=True)
    reg_ids = fields.Many2one('lf.register', string='Select Drug')
    
    #drug_description = fields.One2many('rf.claimdocument', 'claim_ids', 'Claim Document')
    date_request = fields.Date('Request Date',required=True)
    quantity_available = fields.Float(string='Quantity Available', related='reg_ids.quantity',readonly=True)
    #company_id = fields.Char(string='company', related='reg_ids.company_id',readonly=True)
    quantity = fields.Float('Quantity Required',required=True)
    state = fields.Selection([('pend', 'Pending'), ('aprv', 'Approved')],
                             default='pend')
    
    
   
    ''''
     TODO:test security access rule xml file,
     setup email routine,
    ''''
  
    
    @api.model
    def create(self, vals):
        #print self.env['res.company'].name
        # print 'u reach here?'
    
        vals['req_num'] = self.env['ir.sequence'].next_by_code('lf.req.id')
        result = super(LfRequest, self).create(vals)
        return result

    @api.one
    @api.constrains('quantity_available','quantity')
    def validate_dates(self):
        if self.quantity>self.quantity_available:
            raise ValidationError('Not enough stock available')
        
                
    #function to call when button to approve  is clicked
    @api.one
    def send_approve(self):
        #import pdb; pdb.set_trace()
        self.write({
            'state':'aprv'
            
        })
        
        #update stock balance in register after request has been approved
        stock_balance = self.quantity_available - self.quantity
        #register_rec  = self.env['lf.register'].browse(self.reg_ids)
        self.reg_ids.quantity = stock_balance
        
        