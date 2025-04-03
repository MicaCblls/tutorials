# -*- coding: utf-8 -*-
from odoo import http
import requests


import requests
from odoo import http
from odoo.http import request

class Estate(http.Controller):
    @http.route('/estate/estate', auth='public')
    def index(self, **kw):
        url = 'https://dummyjson.com/products'
        response = requests.get(url)
        output = "<h1>Products</h1><ul>"
        if response.status_code == 200:
            data = response.json()

            for item in data["products"]:
                # The key is "title", not "name"
                title = item["title"]
                price = item["price"]
                
                output += f"<li>{title} - ${price}</li>"
            
            output += "</ul>"
            return output
        else:
            print(f"Request failed with status code {response.status_code}")
            return f"Request failed with status code {response.status_code}"

#     @http.route('/estate/estate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('estate.listing', {
#             'root': '/estate/estate',
#             'objects': http.request.env['estate.estate'].search([]),
#         })

#     @http.route('/estate/estate/objects/<model("estate.estate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estate.object', {
#             'object': obj
#         })

