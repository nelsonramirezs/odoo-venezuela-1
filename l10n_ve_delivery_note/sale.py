#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
###############Credits######################################################
#    Coded by: Maria Gabriela Quilarque  <gabrielaquilarque97@gmail.com>
#    Planified by: Nhomar Hernandez
#    Finance by: Helados Gilda, C.A. http://heladosgilda.com.ve
#    Audited by: Humberto Arocha humberto@openerp.com.ve
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################
from osv import osv
from osv import fields
from tools.translate import _
from tools import config
import time
import datetime

class sale_order(osv.osv):
    _inherit = "sale.order"

    _columns = {
        'note_ids': fields.many2many('delivery.note', 'sale_order_delivery_note_rel', 'saleorder_id', 'note_id', 'Delivery Notes', help="This is the list of invoices that have been generated for this sale order. The same sale order may have been invoiced in several times (by line for example)."),
    }
    
    def copy(self, cr, uid, id, default=None, context={}):
        if not default:
            default = {}
        default = default.copy()
        default.update({
            'note_ids': [],
        })
        return super(sale_order, self).copy(cr, uid, id, default, context)

sale_order()




