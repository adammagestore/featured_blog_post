{
    'name' : 'OpenERP Pet Store',
    'version': '1.0',
    'summary': 'Sell pet toys',
    'category': 'Tools',
    'description':
        """
OpenERP Pet Store
=================

A wonderful application to sell pet toys.
        """,
    'data': [
        # "petstore.xml",
        # "petstore_data.xml",
        "views/snippet/snippet_template.xml",
        "views/newest_blog_post.xml",
        "views/thesameblogpost.xml",
        "views/latest_blog_post_x.xml",
        "views/website_blog_view_inherit.xml",
        "views/website_blog_templates_inherit.xml",
        # "oepetstore.message_of_the_day.csv",
    ],
    'depends' : [
        'website_blog',
        'sale_stock'
    ],
    'qweb': [
        # 'static/src/xml/petstore.xml',
    ],
    'application': True,
}
