# -*- coding: utf-8 -*-

# Carlos Rafael Soto (CSotoX)
# Odoo.soporte@gmail.com
# Odoo v11

# CRE 28/ABR/2018 (CSOTOX)

from odoo import api, fields, models, _
from datetime import datetime, date, timedelta

class CxP_Calcular_Dias_Vencidos(models.Model):
    _inherit = "account.invoice"
    x_dias_vencido = fields.Integer(compute = '_CalcularDiasVencido',
                                    string = 'Días que tiene vencido el documento', 
                                    store = False)

    @api.one
    def _CalcularDiasVencido(self):
        # Siempre inicio el valor del campo en cero
        self.x_dias_vencido = 0

        #csx_hoy = date.today()
        csx_hoy = datetime.now()

        # Verifico si el documento esta abierto
        if self.state == "open":
            # Pasa si el documento esta con Estatus de Abierto
            csx_fecha_vence = fields.Datetime.from_string(self.date_due)

            csx_dias = (csx_fecha_vence - csx_hoy).days

            self.x_dias_vencido = csx_dias
    
    # FIN : _CalcularDiasVencido