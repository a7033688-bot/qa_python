import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_existing_genre_of_book_genre_assigned_to_book(self):
        book = BooksCollector()
        book.add_new_book('Астрал')
        book.set_book_genre('Астрал', 'Ужасы')
        assert book.get_books_genre()['Астрал'] == 'Ужасы'

    @pytest.mark.parametrize('names, genre',[
                                            ('Астрал','Ужасы'),
                                            ('Незнайка','Мультфильмы'),
                                            ('Хоббит','Фантастика')])
    def test_get_book_genre_book_title_returns_genre(self,names,genre):
        book = BooksCollector()
        book.add_new_book(names)
        book.set_book_genre(names, genre)
        
        assert book.get_book_genre(names) == genre
        

    def test_get_books_with_specific_genre_return_list_of_films(self):
        book = BooksCollector()
        book.add_new_book('Астрал')
        book.set_book_genre('Астрал', 'Ужасы')
        result = book.get_books_with_specific_genre('Ужасы')
        assert 'Астрал' in result

    def test_get_books_genre_existing_book_will_be_displayed(self):
        book = BooksCollector()
        book.add_new_book('Астрал')
        assert 'Астрал' in book.get_books_genre()

    def test_get_books_for_children_returns_a_list_of_children_books(self):
        book = BooksCollector()
        book.add_new_book('Астрал')
        book.add_new_book('Незнайка')
        book.set_book_genre('Астрал', 'Ужасы')
        book.set_book_genre('Незнайка', 'Мультфильмы')
        assert 'Незнайка' in book.get_books_for_children() 
        assert 'Астрал' not in  book.get_books_for_children()

    def test_add_book_in_favorites_book_title_has_been_added(self):
        book = BooksCollector()
        book.add_new_book('Астрал')
        book.add_book_in_favorites('Астрал')
        assert 'Астрал' in book.get_list_of_favorites_books()

    def test_delete_book_from_favorites_title_of_book_has_been_deleted(self):
        book = BooksCollector()
        book.add_new_book('Астрал')
        book.add_book_in_favorites('Астрал')
        book.delete_book_from_favorites('Астрал')
        assert len(book.get_list_of_favorites_books()) == 0 

    def test_get_list_of_favorites_books_displays_selected_books(self):
        book = BooksCollector()
        book.add_new_book('Астрал')
        book.add_book_in_favorites('Астрал')
        assert 'Астрал' in book.get_list_of_favorites_books() 

        