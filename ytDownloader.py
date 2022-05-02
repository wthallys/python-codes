import webbrowser
url = input("Insira a url do vídeo: ")
url = url[:12] + "ss" + url[12:]
webbrowser.open(url)