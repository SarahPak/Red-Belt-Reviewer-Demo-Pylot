from system.core.model import Model

class Book(Model):
	def __init__(self):
		super(Book, self).__init__()

	def create(self, user_id, book_info):
		""" 1/ Check if author already exists in the database by querying by the author's name
			2/ What is returned (stored in the variable named 'author') will be either an empty list or a list with one record
			3/ If the list is empty (meaning that the author doesn't exist in DB yet), we create the author and get the author'id to insert the (new) book and new review
		"""
		author_query = "SELECT * FROM authors WHERE name='{}' LIMIT 1".format(book_info['author'])
		author = self.db.query_db(author_query)
		
		if not author:
			insert_author_query = "INSERT INTO authors (name, created_at, updated_at) VALUES ('{}', NOW(), NOW())".format(book_info['author'])
			self.db.query_db(insert_author_query)

			get_author_query = "SELECT * FROM authors ORDER BY id DESC LIMIT 1"
			author = self.db.query_db(get_author_query)

		insert_book_query = "INSERT INTO books (title, author_id, created_at, updated_at) VALUES ('{}', '{}', NOW(), NOW())".format(book_info['title'], author[0]['id'])

		self.db.query_db(insert_book_query)

		""" Here I retrieved the most recently added book to create a new review
		"""
		get_book_query = "SELECT * FROM books ORDER BY id DESC LIMIT 1"
		book = self.db.query_db(get_book_query)

		insert_review_query = "INSERT INTO reviews (user_id, book_id, content, rating, created_at, updated_at) VALUES ('{}','{}','{}','{}', NOW(), NOW())".format(user_id, book[0]['id'], book_info['content'], book_info['rating'])

		self.db.query_db(insert_review_query)

		""" Return book's id so we can redirect to the book's show page
		"""
		return book[0]['id']

	def get_book_by_id(self, id):
		get_book_query = "SELECT books.title, authors.name FROM books JOIN authors ON books.author_id = authors.id WHERE books.id = '{}'".format(id)
		return self.db.query_db(get_book_query)

	def get_reviews_by_book_id(self, id):
		get_reviews_query = "SELECT reviews.content, reviews.rating, users.name, reviews.created_at FROM reviews JOIN users on users.id = reviews.user_id JOIN books ON books.id = reviews.book_id WHERE books.id = {}".format(id)
		return self.db.query_db(get_reviews_query)

