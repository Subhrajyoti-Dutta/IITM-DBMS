select title from book_authors,book_catalogue where book_authors.isbn_no=book_catalogue.isbn_no and author_fname = 'Joh Paul' and author_lname = 'Mueller'