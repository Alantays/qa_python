import pytest
from main import BooksCollector
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize(
        'book_name, expected_length',
        [
            ['', 0],
            ['a', 1],
            ['a' * 41, 0],
            ['a' * 40, 1],
        ]
    )
    def test_add_new_book_with_different_name_length(self, book_name, expected_length):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == expected_length

    def test_set_book_genre_existing_book_has_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert 'Гордость и предубеждение и зомби' in collector.books_genre
        assert collector.books_genre['Гордость и предубеждение и зомби'] == 'Фантастика'

    def test_set_book_genre_non_existing_book_has_no_genre(self):
        collector = BooksCollector()
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert 'Гордость и предубеждение и зомби' not in collector.books_genre

    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_book_genre_returns_none_for_non_existing_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Гордость и предубеждение и зомби') is None

    def test_get_books_with_specific_genre_returns_correct_books_for_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    def test_get_books_with_specific_genre_returns_empty_list_for_non_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Триллеры')
        assert collector.get_books_with_specific_genre('Триллеры') == []

    def test_get_books_genre_returns_empty_dictionary_when_no_books_added(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    def test_get_books_genre_returns_dictionary_with_books_and_genres_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Ужасы', 'Что делать, если ваш кот хочет вас убить': 'Детективы'}

    def test_get_books_for_children_returns_empty_list_if_books_genre_is_restricted(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_returns_correct_list_with_mixed_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Винни-Пух')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Винни-Пух', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Гордость и предубеждение и зомби', 'Винни-Пух']

    def test_add_book_in_favorites_already_in_favorites_do_not_added_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_book_not_in_list(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Винни-Пух')
        assert 'Винни-Пух' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_successful(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_not_in_list(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Винни-Пух')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    def test_get_list_of_favorites_books_returns_empty_list_if_no_books_in_favorites(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
