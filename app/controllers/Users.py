from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)
		self.load_model('User')

	def index(self): # shows log in/registration forms
		return self.load_view('users/index.html')

	def create(self): # or sign_up
		user_info = request.form
		result = self.models['User'].create(user_info)
		if result['status']:
			session['id'] = result['user']['id']
			session['name'] = result['user']['name']
			return redirect('/books')
		else:
			for msg in result['errors']:
				flash(msg)
			return redirect('/')

	def sign_in(self): # does what you think it does
		user_info = request.form
		result = self.models['User'].sign_in(user_info)
		if result['status'] is True:
			session['id'] = result['user']['id']
			session['name'] = result['user']['name']
			return redirect('/books')
		else:
			flash('Invalid email or password')
			return redirect('/')
