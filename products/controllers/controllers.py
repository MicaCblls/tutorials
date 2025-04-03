# -*- coding: utf-8 -*-
import requests
from odoo import http
from odoo.http import request

class Product(http.Controller):
    @http.route('/product/product', methods=['POST'], auth='public')
    def upload_products(self, **kw):
        url = 'https://dummyjson.com/products'
        response = requests.get(url)
        output = "<h1>Products</h1><ul>"
        if response.status_code == 200:
            data = response.json()

            for item in data["products"]:
                title = item["title"]
                price = item["price"]
                
                output += f"<li>{title} - ${price}</li>"
            
            output += "</ul>"
            return output
        else:
            print(f"Request failed with status code {response.status_code}")
            return f"Request failed with status code {response.status_code}"



# from odoo import http


# class Products(http.Controller):
#     @http.route('/products/products', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/products/products/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('products.listing', {
#             'root': '/products/products',
#             'objects': http.request.env['products.products'].search([]),
#         })

#     @http.route('/products/products/objects/<model("products.products"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('products.object', {
#             'object': obj
#         })

