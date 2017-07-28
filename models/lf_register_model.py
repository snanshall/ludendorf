# -*- coding: utf-8 -*-

from odoo import  models,fields,api
from odoo.fields import Many2many
#from odoo.exceptions import ValidationError


class LfRegister(models.Model):
    _name = 'lf.register'
    _rec_name = 'description'
    
    
    batch_num = fields.Char(string='Batch ID',readonly=True, store=True)
    #drug_description = fields.One2many('rf.claimdocument', 'claim_ids', 'Claim Document')
    description = fields.Text(string='Name',required=True)
    date_expiry = fields.Date('Expiry Date',required=True)
    date_delivery = fields.Date('Delivery Date',required=True)
    quantity = fields.Float('Quantity',required=True)
    related_companies = Many2many('res.company',string='Select all allowed companies')
    state = fields.Selection([('is', 'In Stock'), ('os', 'Out Of Stock')],
                             compute='_compute_state')
    #claim_status = fields.Many2one("rf.claim.status", string="Claim Status")
    
   
    
        
    
    @api.model
    def create(self, vals):
        
    
        vals['batch_num'] = self.env['ir.sequence'].next_by_code('lf.batch.id')
        result = super(LfRegister, self).create(vals)
        return result
        
        
    @api.one
    @api.depends('quantity')
    def _compute_state(self):
        """
        Update the state  based on the quantity available orderlines
        """
        if self.quantity>0:
            self.state = 'is'
        else:
            self.state = 'os'
        return        
    '''
    @api.one
    @api.constrains('expiry_date')
    def validate_dates(self):
        if self.expiry_date<today:
            raise ValidationError('expiry Date cannot be before today')
        

    '''
        