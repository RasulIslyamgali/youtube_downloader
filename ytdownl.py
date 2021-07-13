from pytube import YouTube

# получаем ссылку на видео
link = input('Вставьте ссылку для скачивания:\n')
yt = YouTube(link)

# выводим информацию о видео
print('Название: ', yt.title)
print('Просмотры: ', yt.views)
print('Продолжительность: ', yt.length, 'сек\n')

# выбираем поток с максимальным значением
ys = yt.streams.get_highest_resolution()

# загрузка
print('Видео загружается...')
ys.download(r'C:\Users\Admin\Downloads')
print('Поздравляем. Загрузка завершена.')

