import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import requests
import streamlit as st
import time
from random import randrange
import __init__
import cred
scope = 'playlist-read-private playlist-modify playlist-modify-private playlist-read-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID, client_secret= cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))

base="light"
primaryColor="blue"


def convertMillis(millis):
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes = (millis/(1000*60))%60
    minutes = int(minutes)

    st.write(minutes, ":", seconds)
    return

col1, col2, col3 = st.beta_columns(3)
tester = False

with col1:
    results = sp.current_user_playlists()
    st.subheader("Your list of Playlists:")
    for idx, item in enumerate(results['items']):
        playlist = item['name']
        playlist_id = item['id']
        st.write(idx, playlist)

with col2:
    st.subheader("Please select the playlist ID you want for your shower!")
    selected_playlist = st.number_input('Playlist ID', value=0, step=1)
    st.button("Submit")

    
    results = sp.playlist_tracks(results['items'][selected_playlist]['id'], fields=None, limit=100, offset=0, market=None, additional_types=('track', ))
    for idx, item in enumerate(results['items']):
        tracks = item['track']
        track_id = tracks['id']
        track_name = tracks['name']
        track_length_millis = tracks['duration_ms']
        # st.write(idx, track_name)
        # track_length = convertMillis(tracks['duration_ms'])


    less_than_seven = True
    track1 = randrange(len(results['items']))
    track_id1 = results['items'][track1]['track']['id']
    track_name1 = results['items'][track1]['track']['name']
    track_length1 = results['items'][track1]['track']['duration_ms']
    if track_length1 < 420000:
        while less_than_seven == True:
            track2 = randrange(len(results['items']))
            track_id2 = results['items'][track2]['track']['id']
            track_name2 = results['items'][track2]['track']['name']
            track_length2 = results['items'][track2]['track']['duration_ms']
            sum_of_tracks = track_length1 + track_length2
            if sum_of_tracks > 420000:
                track2 = randrange(len(results['items']))
            else:
                less_than_seven = False
        st.subheader("Length of your songs")
        (convertMillis(sum_of_tracks))
        st.write(track_name1)
        st.write(track_name2)
        button_to_replace = st.button("Add to playlist")
    else:
        st.subheader("Length of your songs")
        st.write(convertMillis(track_length1))
        button_to_replace = st.button("Add to playlist")

    if button_to_replace:
        items_to_add = [track_id1, track_id2]
        sp.playlist_replace_items('2el4FUXtWLtVcQTo1GC1R3', items_to_add)


with col3:    
    st.subheader("Countdown Timer")
    st.write("Once the songs have been added to your playlist, please go back to your spotify app and start playing your music. Once the music has started playing, please click the button below")
    st.write("When the timer runs out, your music and shower will stop. Think about the environment! ")
    if st.button("Started Playing"):
        start = int(sum_of_tracks/1000)
        print(start)
        st.subheader("Time Remaining:")
        t = st.empty()
        while start > 0:
            t.markdown(start)
            start = start-1
            time.sleep(1)
        if start == 0:
            response = requests.get('http://192.168.1.103/Python')

