from system.core.controller import *

class Books(Controller):
	def __init__(self, action):
		super(Books, self).__init__(action)
		self.load_model('Book')
	
	def index(self): # serves as landing page after users sign in or register successfully
		return self.load_view('books/index.html')

	def new(self): # shows the form to add a new book review
		return self.load_view('books/new.html')

	def create(self): # create a new book review
		book_info = request.form
		user_id = session['id']
		book_id = self.models['Book'].create(user_id, book_info)
		return redirect('/books/' + str(book_id))

	def show_book_and_reviews(self, id):
		book = self.models['Book'].get_book_by_id(id)

		retrieved_reviews = self.models['Book'].get_reviews_by_book_id(id)

		return self.load_view('books/show.html', book=book[0], reviews=retrieved_reviews)
