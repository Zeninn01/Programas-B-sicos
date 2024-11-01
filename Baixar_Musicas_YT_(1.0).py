import yt_dlp

#URL do vídeo que deseja baixar como MP3
video_url = "video_url"

#configurações para baixar apenas o áudio e converter para MP3
ydl_opts = {
    "format": 'bestaudio/best', #Seleciona o melhor áudio disponível
    "outtmpl": 'Destinatario da musica.%(ext)s', #Diretório e nome do arquivo
    "postprocessors": [{
        "key": 'FFmpegExtractAudio', #Extrai o áudio usando FFmpeg
        "preferredcodec": 'mp3', #Define o codec para mp3
        "preferredquality": '192', #Qualidade do áudio em kbps
    }],
    "ffmpeg_location": r'Destinatario do ffmpeg.exe' #Caminho completo para o executável ffmpeg
}

#Baixar o áudio
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
