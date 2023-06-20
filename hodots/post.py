from . import api_url, req

class PostNotFound(Exception):
    pass

class CommunityGuidelinesViolation(Exception):
    pass

class TermsOfServicesViolation(Exception):
    pass

class UnknownOrPrivatedPost(Exception):
    pass

class TakedownRequested(Exception):
    pass

class Post(object):
    def __init__(self, postlink):
        self.postlink = postlink

    @staticmethod
    def getfromlink(postlink):
        res = req.get('{}/posts/postpage?link={}'.format(api_url, postlink))

        output = res.json()
    
        if res.status_code == 404:
            raise PostNotFound("Post not found")
        elif 'takedownuser' in output and output['takedownuser'] != "":
            raise TakedownRequested("Post unavailable due to a takedown requested by {}".format(res.json()['takedownuser']))
        elif output['options']['status'] not in ["public", "link"]:
            match output['options']['status']:
                case 'cgviolation':
                    raise CommunityGuidelinesViolation("Post unavailable because the post violates the Guidelines")
                case 'tosviolation':
                    raise TermsOfServicesViolation("Post unavailable because the post violates the Terms of Services")
                case 'private':
                    raise UnknownOrPrivatedPost("Post unavailable because the post is private")
                case _:
                    raise UnknownOrPrivatedPost("Post unavailable, Error occurred reading or the post is private.")
        else:
            return output