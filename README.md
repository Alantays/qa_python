# qa_python

## Описание тестов

### test_add_new_book_add_two_books

Этот тест проверяет, что можно добавить две книги в коллекцию.

### test_add_new_book_with_different_name_length

Этот тест проверяет, что нельзя добавить книгу с пустым названием или названием длиннее 40 символов, проверяя граничные значения.

### test_set_book_genre_existing_book_has_valid_genre

Этот тест проверяет, что можно установить жанр для существующей книги.

### test_set_book_genre_non_existing_book_has_no_genre

Этот тест проверяет, что нельзя установить жанр для несуществующей книги.

### test_get_book_genre_returns_correct_genre

Этот тест проверяет, что метод возвращает правильный жанр для существующей книги.

### test_get_book_genre_returns_none_for_non_existing_book

Этот тест проверяет, что метод возвращает `None` для несуществующей книги.

### test_get_books_with_specific_genre_returns_correct_books_for_existing_genre

Этот тест проверяет, что метод возвращает правильный список книг для существующего жанра.

### test_get_books_with_specific_genre_returns_empty_list_for_non_existing_genre

Этот тест проверяет, что метод возвращает пустой список для несуществующего жанра.

### test_get_books_genre_returns_empty_dictionary_when_no_books_added

Этот тест проверяет, что метод возвращает пустой словарь, если не добавлено ни одной книги.

### test_get_books_genre_returns_dictionary_with_books_and_genres_added

Этот тест проверяет, что метод возвращает словарь с книгами и их жанрами.

### test_get_books_for_children_returns_empty_list_if_books_genre_is_restricted

Этот тест проверяет, что метод возвращает пустой список, если все книги имеют запрещенные жанры.

### test_get_books_for_children_returns_correct_list_with_mixed_books_added

Этот тест проверяет, что метод возвращает правильный список книг для детей, если добавлены книги разных жанров.

### test_add_book_in_favorites_already_in_favorites_do_not_added_twice

Этот тест проверяет, что книга не добавляется в избранное дважды.

### test_add_book_in_favorites_book_not_in_list

Этот тест проверяет, что нельзя добавить в избранное книгу, которой нет в списке.

### test_delete_book_from_favorites_successful

Этот тест проверяет, что книга успешно удаляется из избранного.

### test_delete_book_from_favorites_book_not_in_list

Этот тест проверяет, что нельзя удалить из избранного книгу, которой нет в списке.

### test_get_list_of_favorites_books_returns_correct_books

Этот тест проверяет, что метод возвращает правильный список избранных книг.

### test_get_list_of_favorites_books_returns_empty_list_if_no_books_in_favorites

Этот тест проверяет, что метод возвращает пустой список, если нет избранных книг.
