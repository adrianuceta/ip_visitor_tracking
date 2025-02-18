from odoo import models, fields
from odoo.exceptions import UserError
import requests
import logging

_logger = logging.getLogger(__name__)

class IpGeo(models.Model):
    __name = 'ip.visitor.tracking'
    _description = 'IP Visitor Tracking'
    _rec_name = 'Direccion_IP'

    Direccion_IP = fields.Char(string='Dirección IP', required=True)
    Pais = fields.Char(string='País', readonly=True)
    Ciudad = fields.Char(string='Ciudad', readonly=True)
    Longitud = fields.Float(string='Longitud', readonly=True)
    Latitud = fields.Float(string='Latitud', readonly=True)
    Proveedor = fields.Char(string='Proveedor', readonly=True)
    Organizacion = fields.Char(string='Organización', readonly=True)
    Hora = fields.Datetime(string='Hora', readonly=True)

    def get_ip_data(self):
        for rec in self:
            url = 'https://api.ipgeolocation.io/ipgeo
            params = {'apiKey': 'YOUR_API_KEY', 'ip': rec.Direccion_IP}
            response = requests.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                rec.Pais = data['country_name']
                rec.Ciudad = data['city']
                rec.Longitud = data['longitude']
                rec.Latitud = data['latitude']
                rec.Proveedor = data['isp']
                rec.Organizacion = data['organization']
                rec.Hora = fields.Datetime.now()
            else:
                raise UserError('Error al obtener datos de la IP')
                _logger.error('Error al obtener datos de la IP')

                