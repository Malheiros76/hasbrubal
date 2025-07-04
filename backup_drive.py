from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file = drive.CreateFile({'title': 'ocorrencias.db'})
file.SetContentFile('ocorrencias.db')
file.Upload()

print("✅ Banco de dados enviado para seu Google Drive!")
