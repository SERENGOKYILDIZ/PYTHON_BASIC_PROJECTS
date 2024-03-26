import pprint

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"

SPO_USERNAME = "Jaybicov"
SPO_ID = "0da8d8f366b349188d9af780e880fe86"
SPO_SEC = "e123ff5133be4817b7725aca470db2c3"
SPO_RES_URL = "https://example.com/"

want_date = input("Please write the date you want (YYYY-MM-DD): ")

response = requests.get(url=f"{URL}/{want_date}/")
response.raise_for_status()
site_html = response.text
# print(site_html)

soup = BeautifulSoup(site_html, "html.parser")
musics = soup.select(selector="li #title-of-a-story")
all_musics = [" ".join(music.getText().split()) for music in musics]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPO_RES_URL,
        client_id=SPO_ID,
        client_secret=SPO_SEC,
        show_dialog=True,
        cache_path="token.txt",
        username=SPO_USERNAME,
    )
)
user_id = sp.current_user()["id"]
song_uris = []
year = want_date.split("-")[0]
for song in all_musics:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    # pprint.pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{want_date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
