from odoo import models, fields
from datetime import datetime, timedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    _order = "id desc"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=fields.Date.today() + timedelta(days=90))
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    last_seen = fields.Datetime(default=fields.Date.today())
    active = fields.Boolean(default=False)
    state= fields.Selection(
        selection=[
            ('new', 'New'),
            ('offerReceived', 'Offer Received'),
            ('offerAccepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled'),
        ],
        string='State',
        default='New',
        required=True,
        help="Select the current state of this record."
    )