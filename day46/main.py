import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Enter the date for the top 100 songs you want to listen to. Input in YYYY-MM-DD format.\n")
#date = "2000-10-14"
year = date[0:4]
url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url)
response.raise_for_status()
content = response.text
soup = BeautifulSoup(content, "html.parser")
authorboxspanclass = "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"

top100names = [tag.getText().strip() for tag in soup.select("div.o-chart-results-list-row-container li h3#title-of-a-story")]
top100artists = [tag.getText().strip() for tag in soup.select(f"div.o-chart-results-list-row-container li span.a-no-trucate")]

scopes="playlist-modify-private playlist-modify-public"
spotifyOAuth = SpotifyOAuth(client_id = os.environ["SPOTIPY_CLIENT_ID"],
                            client_secret = os.environ["SPOTIPY_CLIENT_SECRET"],
                            redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"],
                            username="Bukloulou",
                            scope=scopes)
sp = spotipy.Spotify(auth_manager=spotifyOAuth)


songids = []
for num in range(0,len(top100artists)):
    track = top100names[num]
    artist = top100artists[num]
    query = f"artist:{artist} track:{track}"
    try:
        songspotify = sp.search(q=query,market = "US", limit = 1)['tracks']['items'][0]['external_urls']['spotify']
        songid = sp.search(q=query,market = "US", limit = 1)['tracks']['items'][0]['id']
        songids.append(songid)

    except IndexError:
        pass

sp.user_playlist_create(user=os.environ["SPOTIPY_USER_ID"], name=date, description="Throwback to " +date)
playlists = sp.current_user_playlists()
playlistid = None
for playlist in playlists['items']:
    if playlist['name'] == date:
        playlistid = playlist['id']

sp.playlist_add_items(playlist_id=playlistid, items=songids, position = 0)