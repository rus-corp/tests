import pytest
from main import geo_log, ids_funk, max_stats, create_folder, folder_path, token_ya


class TestClass:
    def test_geo(self):
        total_list = [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]
        res = geo_log()
        assert res == total_list

    def test_ids(self):
        tot_list = [213, 15, 54, 119, 98, 35]
        res = ids_funk()
        assert res == tot_list

    def test_max_stat(self):
        total_val = {'yandex': 120}
        res = max_stats()
        assert res == total_val

    def test_folder_create(self):
        total_code = 201
        res = create_folder(token_ya, folder_path)
        assert res == total_code







