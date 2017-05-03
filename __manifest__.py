{
    'name' : 'Featured Blog Post',
    'version': '1.0',
    'summary': 'Display featured blog post on right column',
    'category': 'Tools',
    'description':
        """
Featured Blog Post module
=================
    A module to display the featured blog post on right column

        """,
    'data': [
        "views/website_blog_view_inherit.xml",
        "views/website_blog_templates_inherit.xml",
    ],
    'depends' : [
        'website_blog'
    ],
    'qweb': [
    ],
    'application': True,
}
