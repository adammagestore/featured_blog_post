# -*- coding: utf-8 -*-
# Created by Adam from Magestore
from odoo import api, fields, models


class FeaturedBlogPost(models.Model):
    _inherit = "blog.post"

    is_featured = fields.Boolean(String="Featured Post", default=False)