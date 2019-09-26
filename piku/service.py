""" api.py - Pets Falcon API definition """
import falcon
import json
from pets import Pet, Cat
from apikeystore import APIKeystore

from falcon.http_status import HTTPStatus

class HandleCORS(object):
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', '*')
        resp.set_header('Access-Control-Allow-Headers', '*')
        resp.set_header('Access-Control-Max-Age', 1728000)  # 20 days
        if req.method == 'OPTIONS':
            raise HTTPStatus(falcon.HTTP_200, body='\n')

def raise_error(status_code, title, failed_action, reason):
    description = "Failed to {0!s} because: {1!s}".format(failed_action, reason)
    falcon_method = getattr(falcon, "HTTP_{0!s}".format(status_code))

    raise falcon.HTTPError(status=falcon_method,
                           title=("{0!s} {1!s}".format(status_code, title)),
                           description=description)


class RandomPetResource(object):
    def on_get(self, req, resp, count=1):
        count=int(count)
        if count == 1:
            resp.body = Pet.random().json
        else:
            petlist = [Pet.random().json for p in xrange(int(count))]
            resp.body = '{ "pets": [' + ",".join(petlist) + "]}"

def check_api_key(req, resp, resource, params):
    authkey = None
    if req.headers.has_key('AUTHORIZATION'):
        authkey = req.headers['AUTHORIZATION']
    if not APIKeystore.is_valid(authkey):
        raise_error(status_code=401,
                    title="Unauthorized",
                    failed_action=req.method,
                    reason="Did not supply a valid API key")

@falcon.before(check_api_key)
class PetResource(object):
    def on_get(self, req, resp, pet_id):
        if int(pet_id) == 1:
            resp.body = Cat("Bella", 3, "American Shorthair").json
        else:
            raise_error(status_code=404,
                        title="Can't find Pet with id {}".format(pet_id),
                        failed_action="GET",
                        reason="No such id in DB")

    def on_post(self, req, resp):
        try:
            doc = json.loads(req.stream.read(req.content_length or 0))
            doc['id'] = 32
            resp.body = json.dumps(doc)
        except Exception as e:
            print e
            raise_error(status_code=400,
                        title="Failed to create pet",
                        failed_action="Create",
                        reason="Invalid data provided")

def create():
    api = falcon.API(middleware=[HandleCORS() ])
    api.add_route('/pet/random',           RandomPetResource())
    api.add_route('/pet/random/{count}',   RandomPetResource())
    api.add_route('/pet/',                 PetResource())
    api.add_route('/pet/{pet_id}',         PetResource())
    return api

api = create()
