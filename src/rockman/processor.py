def default(request):
    return {
        'css_file': ['base/css/theme.css',
                     'base/css/base.css',
                     ],
        'js_file': ['base/js/bootstrap.js',
                    'base/js/jquery-1.11.2.min.js',
                    'base/js/base.js',
                    ],

        'page_title': 'emily & kyle rockman.life',
        'window_title': 'rockman.life',  #use full names for search engine optimization
        'footer_email': 'support@rockman.life',
    }
