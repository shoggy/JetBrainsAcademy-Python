def tracklist(**kwargs):
    for artist, data in kwargs.items():
        print(artist)
        for album, track in data.items():
            print(f"ALBUM: {album} TRACK: {track}")
