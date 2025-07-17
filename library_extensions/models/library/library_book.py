# -*- coding: utf-8 -*-
# Native Python modules

# Local python modules

# Custom python modules

# Odoo modules
from odoo import models, fields, api


class LibraryBook(models.Model):
    ######################
    # Private attributes #
    ######################
    _inherit = "library.book"

    ###################
    # Default methods #
    ###################

    ######################
    # Fields declaration #
    ######################
    author_id = fields.Many2one(
        comodel_name="res.partner",
        string="Author",
        required=True,
    )
    category_id = fields.Many2many(
        comodel_name="library.book.category",
        string="Book Category",
        required=True,
    )

    ##############################
    # Compute and search methods #
    ##############################

    ############################
    # Constrains and onchanges #
    ############################

    #########################
    # CRUD method overrides #
    #########################

    ##################
    # Action methods #
    ##################

    ####################
    # Business methods #
    ####################
