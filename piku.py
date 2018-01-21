""" api.py - Pets Falcon API definition """
import falcon

import rethinkdb as r
from pets import Pet

class PetResource:

	def on_get(self, req, resp):
		resp.body = Pet.random().json

api = falcon.API()
api.add_route('/pet/random', PetResource())