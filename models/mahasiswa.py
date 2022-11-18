# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mahasiswa(models.Model):
    _name = 'ekinerja.mahasiswa'
    _description = 'Menyimpan data mahasiswa'

    name = fields.Char()
