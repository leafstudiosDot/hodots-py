from . import api_url, req

class PostNotFound(Exception):
    pass

class Post(object):
    def __init__(self, postlink):
        self.postlink = postlink

    @staticmethod
    def getfromlink(postlink):
        res = req.get('{}/posts/postpage?link={}'.format(api_url, postlink))

        return res.json()