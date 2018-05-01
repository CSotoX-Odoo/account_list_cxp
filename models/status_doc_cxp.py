# -*- coding: utf-8 -*-

# Carlos Rafael Soto (CSotoX)
# Odoo.soporte@gmail.com
# Odoo v11

# CRE 01/MAY/2018 (CSOTOX)

from odoo import api, fields, models, _

class CxP_Calcular_Status_Vencidos(models.Model):
    _inherit = "account.invoice"

    x_status_vencido = fields.Integer(compute = '_CalcularStatusVencido',
                                    string = 'Status del documento en CXP.', 
                                    help = '0 = Bien, 1 = Vence ese día, 2 = Vencido, 9 = No definido',
                                    store = False)

    @api.one
    def _CalcularStatusVencido(self):
        # Siempre inicio el valor del campo en cero
        self.x_status_vencido = 9

        # Verifico si el documento esta abierto
        if self.state == "open":
            # Pasa si el documento esta con Estatus de Abierto
            if self.x_dias_vencido == 0:
                self.x_status_vencido = 1
            elif self.x_dias_vencido > 0:
                self.x_status_vencido = 0
            elif self.x_dias_vencido < 0:
                self.x_status_vencido = 2
    
    # FIN : _CalcularStatusVencido



