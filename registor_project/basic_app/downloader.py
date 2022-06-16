from logging import exception
import requests
from urllib.request import urlopen
import os

def get_response(url):
    print('came here')
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return get_vid_url(r.text)

# video_matches = re.findall('"video_url":"([^"]+)"',response)
def get_vid_url(response):
    strlen = len('"video_url":"')
    val = 0
    val = response.find('"video_url":"')
    print(val)
    if val > 0:
        video_matches = response[val+strlen:response.find('"',val+strlen+1,len(response))]      
        vid_urls = video_matches.replace('\\u0026','&')
        print('Detected Videos:',vid_urls)
        return save_video(vid_urls)  
    else:
        print('not found any')
        return exception('VALUE NOT FOUND')

def save_video(vid_url):
    try:
        vid = urlopen(vid_url).read()
        open(nextnonexistent("downloaded_video.mp4"), "wb").write(vid)
        return print('Successfully Downloaded')
    except:
        return Exception('VIDEONOTFOUNDerror')
        

def nextnonexistent(f):
    fnew = f
    root, ext = os.path.splitext(f)
    i = 0
    while os.path.exists(fnew):
        i += 1
        fnew = '%s_%i%s' % (root, i, ext)
    return fnew

#response = get_response()
#vid_url = get_vid_url(response)

