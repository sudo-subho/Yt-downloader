from django.shortcuts import render, redirect
from django.http import HttpResponse
import yt_dlp
from django.http import HttpResponse



def fetch_video_info(url):
    ydl_opts = {'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return info
        except Exception as e:
            print(f"Failed to fetch video info: {e}")
            raise

def parse_resolution(res):
    """Extracts integer part from resolution string like '720p', '48x2', etc."""
    import re
    match = re.match(r'(\d+)', res)
    return int(match.group(1)) if match else 0

def home(request):
    video_data = {}
    video_url = 0

    if request.method == 'POST':
        video_url = request.POST.get('url-input')

        if video_url:
            video_url = clean_youtube_url(video_url)  # Clean URL
            try:
                info = fetch_video_info(video_url)
                all_formats = info.get('formats', [])
                
                # Filter and parse resolutions
                resolutions = [format['resolution'] for format in all_formats if 'resolution' in format and parse_resolution(format['resolution']) >= 360]
                highest_resolution = max(resolutions, key=parse_resolution) if resolutions else 'No resolutions available'
                
                # Ensure resolutions are sorted
                resolutions = sorted(resolutions, key=parse_resolution)
                
                video_data = {
                    'title': info.get('title', ''),
                    'thumbnail_url': info.get('thumbnail', ''),
                    'resolutions': resolutions,
                    'highest_resolution': highest_resolution
                }
            except Exception as e:
                video_data['error'] = str(e)
                print(f"Error fetching video data: {e}")
        else:
            video_data['error'] = "Invalid or missing YouTube URL."

    return render(request, 'home.html', {'video_data': video_data, 'video_url':video_url})



def clean_youtube_url(url):

    import re
    return re.sub(r'\?si=.*$', '', url)


def fetch_video_info2(url):
    ydl_opts = {'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info


def download_video(request):
    video_url = request.POST.get('url-input')
    resolution = request.POST.get('resolution')

    if not video_url or not resolution:
        return HttpResponse('Invalid request', status=400)

    try:
        resolution_height = resolution.split('x')[-1]  # Extract height from resolution (e.g., 720 from '1280x720')

        ydl_opts = {
            'format': f'bestvideo[height<={resolution_height}]+bestaudio/best[height<={resolution_height}]',
            'noplaylist': True,
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)

            # Check if video is a combination of video+audio or a single stream
            if 'requested_formats' in info_dict:
                video_url = info_dict['requested_formats'][0]['url']
            else:
                video_url = info_dict['url']

            # Redirect the user to the direct video URL
            return redirect(video_url)

    except Exception as e:
        return HttpResponse(f'Error: {str(e)}', status=500)


def features(request):

    return render(request, 'features.html', {})

def pricing(request):

    return render(request, 'pricing.html', {})

def about(request):

    return render(request, 'about.html', {})

def contact(request):

    return render(request, 'contact.html', {})

def user_login(request):

    return render(request, 'login.html', {})

def user_register(request):

    return render(request, 'register.html', {})

def user_logout(request):

    return render(request, 'contact.html', {})


def yt_audio(request):

    return render(request, 'yt_audio.html', {})

def yt_shorts(request):

    return render(request, 'yt_shorts.html', {})
def yt_playlist(request):

    return render(request, 'yt_playlist.html', {})

def yt_subtitle(request):

    return render(request, 'yt_subtitle.html', {})

def yt_thumbnail(request):

    return render(request, 'yt_thumbnail.html', {})