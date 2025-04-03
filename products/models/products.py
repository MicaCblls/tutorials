from odoo import models, fields, api
from datetime import datetime, timedelta
import requests
import logging

_logger = logging.getLogger(__name__)

class ProductsTest(models.Model):
    _name = "products.test"
    _description = "products"
    _order = "id desc"

    external_id = fields.Char(required=True)
    title = fields.Char(required=True)
    description = fields.Text()
    category = fields.Char()
    discountPercentage = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    stock = fields.Integer(default=0)
    brand = fields.Char()
    returnPolicy = fields.Char()
    image = fields.Char()
    availabilityStatus = fields.Char()
    sku = fields.Char()
    width = fields.Float()
    height = fields.Float()
    depth = fields.Float()
    weight = fields.Float()
    
    @api.model
    def fetch_and_store_products(self):
        url = "http://localhost:8080/products"
        try:
            response = requests.get(url)
            if response.status_code != 200:
                _logger.warning("API request failed with status: %s", response.status_code)
                return

            data = response.json()  # e.g. {"products": [ {...}, {...} ], ...}
            products_list = data
            
            ProductTemplate = self.env['products.test'].sudo()
            
            allowed_keys = [
                'external_id',
                'title',
                'description',
                'category',
                'discountPercentage',
                'selling_price',
                'stock',
                'brand',
                'returnPolicy',
                'image',
                'availabilityStatus',
                'sku',
                'width',
                'height',
                'depth',
                'weight',
            ]

            for item in products_list:
                values = {
                    key: item.get(key, None)
                    for key in allowed_keys
                }
                values['external_id'] = item.get('_id', None)

                existing = ProductTemplate.search([('external_id', '=', values['external_id'])], limit=1)
                if existing:
                    existing.write(values)
                else:
                    ProductTemplate.create(values)

            _logger.info("Successfully fetched and stored %d products", len(products_list))

        except Exception as e:
            _logger.exception("Error fetching products: %s", e)
