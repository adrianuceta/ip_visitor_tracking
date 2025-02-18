from odoo import models, fields
from odoo.exceptions import UserError
import requests
import logging

_logger = logging.getLogger(__name__)

class IpGeo(models.Model):
    _name = 'ip.visitor.tracking'  # Corregido de __name a _name
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
            try:
                url = 'https://api.ipgeolocation.io/ipgeo'
                params = {
                    'apiKey': '8e4eaba9600e436a957c654489b26663',  # Reemplazar con la API key real
                    'ip': rec.Direccion_IP
                }
                response = requests.get(url, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    rec.write({
                        'Pais': data.get('country_name'),
                        'Ciudad': data.get('city'),
                        'Longitud': float(data.get('longitude', 0)),
                        'Latitud': float(data.get('latitude', 0)),
                        'Proveedor': data.get('isp'),
                        'Organizacion': data.get('organization'),
                        'Hora': fields.Datetime.now()
                    })
                else:
                    raise UserError(f'Error al obtener datos de la IP: {response.status_code}')
            except Exception as e:
                _logger.error('Error al obtener datos de la IP: %s', str(e))
                raise UserError(f'Error al obtener datos de la IP: {str(e)}')