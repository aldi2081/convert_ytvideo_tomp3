import pafy

data = input("Masukan Link Youtube : ")
url = pafy.new(data)
print(url.title)

hasil = url.getbestaudio()
hasil.download(f'{url.title}.mp3')