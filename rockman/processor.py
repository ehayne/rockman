def default(request):
    return {
        'css_file': ['base/css/bootstrap/bootstrap.min.css',
                     'base/css/bootstrap/bootstrap-theme.min.css',
                     'base/css/base.css',
                     ],
        'js_file': ['base/js/bootstrap/bootstrap.min.js',
                    'base/js/base.js',
                    'base/js/jquery-1.11.2.min.js',
                    # 'base/js/tabs.js',
                    ],

        'page_title': 'emily & kyle rockman.life',
        'window_title': 'rockman.life',  #use full names for search engine optimization
        'footer_email': 'support@rockman.life',
    }
