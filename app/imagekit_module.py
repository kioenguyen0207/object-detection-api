from imagekitio import ImageKit
from settings import *

imagekit = ImageKit(
    private_key=imagekit_settings.PRIVATE_KEY,
    public_key=imagekit_settings.PUBLIC_KEY,
    url_endpoint=imagekit_settings.URL_ENDPOINT
)

def uploadimg(filename):
    with open(filename, 'rb') as f:
        upload = imagekit.upload_file(
            file= f, # required
            file_name = filename, # required
            options= {
            "folder" : "/detect/",
            "is_private_file": False,
            "use_unique_file_name": True
            }
        )
    return upload['response']['url']

if __name__ == "__main__":
    print(uploadimg('pistol.png'))