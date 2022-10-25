from filestack import Client

class FileSharer:

    def __init__(self, filepath, api_key="A1cGdfaMGQZuze08wm1CDz"):
        self.filepath=filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        # upload and create link
        new_file_link = client.upload(filepath=self.filepath)
        #return and create a URL (clickable)
        return new_file_link.url
