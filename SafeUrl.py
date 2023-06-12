import urllib.parse

def is_safe_url(url):
    safe_schemes = ['http', 'https']
    url_parts = urllib.parse.urlparse(url)
    return url_parts.scheme in safe_schemes
