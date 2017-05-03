# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import werkzeug
import itertools
import pytz
import babel.dates
from collections import OrderedDict

from odoo import http, fields, _
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.website.models.website import slug, unslug
from odoo.exceptions import UserError
from odoo.http import request
from odoo.tools import html2plaintext
from odoo.addons.website_blog.controllers.main import WebsiteBlog

class FeaturedBlogPostController(WebsiteBlog):
    @http.route([
        '/blog/<model("blog.blog"):blog>',
        '/blog/<model("blog.blog"):blog>/page/<int:page>',
        '/blog/<model("blog.blog"):blog>/tag/<string:tag>',
        '/blog/<model("blog.blog"):blog>/tag/<string:tag>/page/<int:page>',
    ], type='http', auth="public", website=True)
    def blog(self, blog=None, tag=None, page=1, **opt):
        BlogPost = request.env['blog.post']
        featured_posts = None
        featured_post_number = 0
        if blog.id:
            featured_posts = BlogPost.search(
                [('blog_id', '=', blog.id), ("website_published", "=", True), ("is_featured", "=", True)], limit=3,
                order="create_date desc")
            featured_post_number = len(featured_posts)

        res = super(FeaturedBlogPostController, self).blog(blog, tag, page, **opt)
        res.qcontext.update({"featured_posts": featured_posts})
        res.qcontext.update({"featured_post_number": featured_post_number})
        return res