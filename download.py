import urllib.request
url = "https://github.com/z-mahmud22/Dlib_Windows_Python3.x/raw/refs/heads/main/dlib-19.22.99-cp310-cp310-win_amd64.whl"
filename = "dlib-19.22.99-cp310-cp310-win_amd64.whl"
print(f"Downloading {url} to {filename}...")
urllib.request.urlretrieve(url, filename)
print("Done.")
