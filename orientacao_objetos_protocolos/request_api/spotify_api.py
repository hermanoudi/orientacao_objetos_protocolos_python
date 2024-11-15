import httpx
import base64
import json
from pydantic import BaseModel, Field
from decimal import Decimal
from typing import List, Dict, Optional


# Modelo para validar os dados da API
class Track(BaseModel):
    name: str
    artists: List[str]
    preview_url: Optional[str]


class Playlist(BaseModel):
    id: str
    name: str

    def __str__(self):
        return f"{self.id} - {self.name}"
    
class PlaylistTracksResponse(BaseModel):
    playlist_name: str
    tracks: List[Track]


class PlaylistResponse(BaseModel):
    playlists: List[Playlist]


def get_spotify_token(client_id: str, client_secret: str) -> str:
    url = "https://accounts.spotify.com/api/token"
    
    # Codificação Base64 de client_id:client_secret
    auth_str = f"{client_id}:{client_secret}"
    auth_bytes = auth_str.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")
    
    headers = {
       #"Authorization": f"Basic {auth_base64}",
       "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    
    with httpx.Client() as client:
        response = client.post(url, headers=headers, data=data)
        response.raise_for_status()  # Garante que a requisição foi bem-sucedida
    
    token_data = response.json()
    return token_data["access_token"]


def get_playlists_by_users(spotify_token, user_id) -> PlaylistResponse:
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = {"Authorization":f"Bearer {spotify_token}"}

    with httpx.Client() as client:
        response = client.get(url, headers=headers)
        response.raise_for_status()  # Lança um erro para respostas não 2xx
    
    data = response.json()

    # Processar o JSON e validar os dados
    playlists = [
        Playlist(
            id=item["id"],
            name=item["name"]
        )
        for item in data["items"]
    ]
    
    return PlaylistResponse(playlists=playlists)



def get_playlist_tracks(spotify_token, playlist) -> PlaylistTracksResponse:
    """Gets current rate for USD vs Currency"""

    url = f"https://api.spotify.com/v1/playlists/{playlist}"
    headers = {"Authorization":f"Bearer {spotify_token}"}

    with httpx.Client() as client:
        response = client.get(url, headers=headers)
        response.raise_for_status()  # Lança um erro para respostas não 2xx
    
    data = response.json()

    # Processar o JSON e validar os dados
    playlist_name = data["name"]
    tracks = [
        Track(
            name=item["track"]["name"],
            artists=[artist["name"] for artist in item["track"]["artists"]],
            preview_url=item["track"].get("preview_url"),
        )
        for item in data["tracks"]["items"]
    ]
    
    return PlaylistTracksResponse(playlist_name=playlist_name, tracks=tracks)

    

# pegar o token
if __name__ == "__main__":
    #pegar no https://developer.spotify.com/dashboard/2cc6738049724f8a8e6d0fa1f3afd0cd/settings
    client_id = ""
    client_secret = ""

    user_id = "hermanitto"

    playlists=["3RrcblfRDZwejlVkj9CKuP"]

    try:
        spotify_token = get_spotify_token(client_id, client_secret)
        print(f"Token obtido: {spotify_token}")
    except httpx.HTTPStatusError as e:
        print(f"Erro ao pegar o token na requisição: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        print(f"Ocorreu um erro inexperado ao pegar o token: {e}")

    
    try:
        user_playlists = get_playlists_by_users(spotify_token, user_id)
        print(f"Usuário: {user_id}")
        for playlist in user_playlists.playlists:
            print(f"\n PLAYLIST - {playlist.name}XXXX")
            try:
                playlist_data = get_playlist_tracks(spotify_token, playlist.id)
                for track in playlist_data.tracks:
                    print(f"- {track.name} by {', '.join(track.artists)}")
                    if track.preview_url:
                        print(f"  Preview: {track.preview_url}")
            except httpx.HTTPStatusError as e:
                print(f"Erro na requisição: {e.response.status_code} - {e.response.text}")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")

    except httpx.HTTPStatusError as e:
        print(f"Erro ao buscar as playlists do usuário {user_id}: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}") 



