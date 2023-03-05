geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def geo_log():
    new_geo_list = []
    for city in geo_logs:
        for country in city.values():
            if country[1] == 'Россия':
                new_geo_list.append(city)

    return new_geo_list



ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def ids_funk():
    #[213, 15, 54, 119, 98, 35]
    new_list = []
    for id in ids.values():
        for i in id:
            if i not in new_list:
                new_list.append(i)
    return new_list

# print(ids_funk())


stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def max_stats():
    max_val = max(stats.values())
    new_dict = {k:v for k, v in stats.items() if v == max_val}
    return new_dict


from conf import token_ya
import requests
folder_path = 'dz_test'

def create_folder(token_ya, folder_path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'

    headers = {'Content-Type': 'application.json',
                'Authorization': 'OAuth {}'.format(token_ya)}
    res = requests.put(url, headers=headers, params={'path': folder_path})
    return res.status_code
    





    def create_folder(self, folder_path='vk_photos'):
        folder_url = self.url + 'v1/disk/resources'
        headers = self.get_headers()
        res = requests.put(folder_url, headers=headers, params={'path': folder_path})
        return True
    
