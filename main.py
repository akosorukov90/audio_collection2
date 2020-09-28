class Album:
    name_album = ''
    name_group = ''
    list_track = {}
    all_duration = 0

    def __init__(self, name_album, name_group):
        self.name_album = name_album
        self.name_group = name_group
        self.list_track = {}
        self.all_duration = 0

    def get_tracks(self):
        for key, value in self.list_track.items():
            value.show()

    def add_track(self, value, duration):
        track = Track(value, duration)
        self.list_track[len(self.list_track) + 1] = track

    def get_duration(self):
        for key, value in self.list_track.items():
            self.all_duration += value.duration
        print(f'Общая длительность альбома - {self.all_duration}')


class Track:
    name_track = ''
    duration = 0

    def __init__(self, name_track, duration):
        self.name_track = name_track
        self.duration = duration

    def show(self):
        print(f'{self.name_track} - {self.duration}')


album_1 = Album('Группа крови', 'Кино')
album_1.add_track('Группа крови', 5)
album_1.add_track('Закрой за мной дверь, я ухожу', 4)
album_1.add_track('Война', 4)

album_2 = Album('Ночь', 'Кино')
album_2.add_track('Видели ночь', 3)
album_2.add_track('Фильмы', 5)
album_2.add_track('Твой номер', 4)

album_1.get_tracks()
album_1.get_duration()
print()
album_2.get_tracks()
album_2.get_duration()