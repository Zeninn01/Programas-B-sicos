import yt_dlp

# URL do vídeo
video_url = 'url do video'

# Configuração de opções
ydl_opts = {
    'format': 'best',  # Melhor qualidade de vídeo disponível
    'outtmpl': 'Diretório de download do seu video no computador',  # Nome e diretório personalizados
}

# Baixar o vídeo
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
