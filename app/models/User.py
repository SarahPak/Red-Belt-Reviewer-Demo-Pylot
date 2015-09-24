from system.core.model import Model
import re

class User(Model):
	def __init__(self):
		super(User, self).__init__()

	def create(self, user_info):
		errors = []
		EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

		if not user_info['name']:
			errors.append('Name cannot be blank')
		elif len(user_info['name']) < 2:
			errors.append('Name must be at least 2 charaters long')

		if not user_info['alias']:
			errors.append('Alias cannot be blank')
		elif len(user_info['alias']) < 2:
			errors.append('Alias must be at least 2 charaters long')

		if not user_info['email']:
			errors.append('Email cannot be blank')
		elif len(user_info['email']) < 2:
			errors.append('Email must be at least 2 charaters long')
		elif not EMAIL_REGEX.match(user_info['email']):
			errors.append('Email is not valid')

		if not user_info['password']:
			errors.append('Password cannot be blank')
		elif not user_info['password_confirm']:
			errors.append('Password confirmation cannot be blank')
		elif len(user_info['password']) < 5:
			errors.append('Password must be at least 5 charaters long')
		elif user_info['password'] != user_info['password_confirm']:
			errors.append('Passwords do not match')

		if errors:
			return {'status': False, 'errors': errors}
		
		pw_hash = self.bcrypt.generate_password_hash(user_info['password'])
		insert_query = "INSERT INTO users (name, alias, email, password, created_at, updated_at) VALUES ('{}', '{}', '{}', '{}', NOW(), NOW())".format(user_info['name'], user_info['alias'], user_info['email'], pw_hash)
		self.db.query_db(insert_query)
		get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
		user = self.db.query_db(get_user_query)
		return {'status': True, 'user': user[0]}

	def sign_in(self, user_info):
		sign_in_query = "SELECT * FROM users WHERE email = '{}'".format(user_info['email'])
		user = self.db.query_db(sign_in_query)
		if user and self.bcrypt.check_password_hash(user[0]['password'], user_info['password']):
			return {'status': True, 'user': user[0]}
		else:
			return {'status': False}




















