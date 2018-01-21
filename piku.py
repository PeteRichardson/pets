""" api.py - Pets Falcon API definition """
import falcon
import json

import rethinkdb as r
from pets import Pet

def raise_error(status_code, title, failed_action, reason):
    description = "Failed to {0!s} because: {1!s}".format(failed_action, reason)
    falcon_method = getattr(falcon, "HTTP_{0!s}".format(status_code))

    raise falcon.HTTPError(status=falcon_method,
                           title=("{0!s} {1!s}".format(status_code, title)),
                           description=description)

class RandomPetResource:
    def on_get(self, req, resp):
        resp.body = Pet.random().json

class PetResource:
    def on_get(self, req, resp, pet_id):
        print "petid = {}".format(pet_id)
        if int(pet_id) == 47:
            resp.body = Pet.random().json
        else:
            raise_error(status_code=404,
                     title="Can't find Pet with id {}".format(id),
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
           


api = falcon.API()
api.add_route('/pet/random',   RandomPetResource())
api.add_route('/pet/',         PetResource())
api.add_route('/pet/{pet_id}', PetResource())