# -*- coding: utf-8 -*-

# Carlos Rafael Soto (CSotoX)
# Odoo.soporte@gmail.com
# Odoo v11

# CRE 28/ABR/2018 (CSOTOX)

from odoo import api, fields, models, _
from datetime import datetime, timedelta, date

class CxP_Calcular_Dias_Vencidos(models.Model):
    _inherit = "account.invoice"
    x_dias_vencido = fields.Integer(compute = '_CalcularDiasVencido',
                                    string = 'Días que tiene vencido el documento', 
                                    store = False)

    @api.one
    def _CalcularDiasVencido(self):
        # Siempre inicio el valor del campo en cero
        self.x_dias_vencido = 0

        #csx_hoy = datetime.now().date

        # Verifico si el documento esta abierto
        if self.state == "open":
            # Pasa si el documento esta con Estatus de Abierto
            # self.x_dias_vencido = -1
            #csx_fecha_vence = self.date_due
            #csx_dias = csx_hoy - csx_fecha_vence
            #csx_dias = 10
            #self.x_dias_vencido = csx_dias

            #csx_dias.days




