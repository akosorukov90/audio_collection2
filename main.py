class Album:
    all_albums = []

    def __init__(self, name_album, name_group):
        self.name_album = name_album
        self.name_group = name_group
        self.list_track = []
        self.all_duration = 0
        self.all_albums.append(self)

    def get_tracks(self):
        for track in self.list_track:
            print(track)

    def add_track(self, name_track):
        for track in Track.all_tracks:
            if track.name_track == name_track:
                self.list_track.append(track)

    def get_duration(self):
        for track in self.list_track:
            self.all_duration += track.duration
        print(f'Общая длительность альбома - {self.all_duration}')

    def __str__(self):
        result_track = ''
        for track in self.list_track:
            result_track += 8 * ' ' + str(track) + '\n'
        result = f'Name group: {self.name_group}\nName album: {self.name_album}\nTracks:\n'
        return result + result_track


class Track:
    all_tracks = []

    def __init__(self, name_track, duration):
        self.name_track = name_track
        self.duration = duration
        self.all_tracks.append(self)

    def __str__(self):
        result = f'{self.name_track} - {self.duration} min'
        return result

    def __eq__(self, track):
        return self.duration == track

    def __gt__(self, track):
        return self.duration > track

    def __lt__(self, track):
        return self.duration < track

    def __ge__(self, track):
        return self.duration >= track

    def __le__(self, track):
        return self.duration <= track


album_1 = Album('Группа крови', 'Кино')
album_2 = Album('Ночь', 'Кино')

track_1 = Track('Группа крови', 5)
track_2 = Track('Закрой за мной дверь, я ухожу', 4)
track_3 = Track('Война', 4)
track_4 = Track('Видели ночь', 3)
track_5 = Track('Фильмы', 5)
track_6 = Track('Твой номер', 4)


album_1.add_track('Группа крови')
album_1.add_track('Закрой за мной дверь, я ухожу')
album_1.add_track('Война')

album_2.add_track('Видели ночь')
album_2.add_track('Фильмы')
album_2.add_track('Твой номер')

# album_1.get_tracks()
# album_1.get_duration()
# print()
# album_2.get_tracks()
# album_2.get_duration()
# print()

print(album_1)
print(album_2)

print(track_1)

print(track_1 >= track_5)
print(track_1 <= track_2)
print(track_2 < track_1)
print(track_2 < track_5)