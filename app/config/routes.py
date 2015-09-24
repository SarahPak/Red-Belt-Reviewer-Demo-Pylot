from system.core.router import routes

routes['default_controller'] = 'Users'
routes['POST']['/users'] = 'Users#create'
routes['GET']['/books'] = 'Books#index'
routes['POST']['/sign_in'] = 'Users#sign_in'
routes['GET']['/books/new'] = 'Books#new'
routes['POST']['/books'] = 'Books#create'
routes['GET']['/books/<id>'] = 'Books#show_book_and_reviews'