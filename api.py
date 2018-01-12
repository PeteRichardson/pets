import falcon

import rethinkdb as r
import json
from pets import Cat

class PetResource:
	def on_get(self, req, resp):

		bella = Cat("Bella", 3, "American Shorthair")

		pet_record = json.dumps(bella.__dict__)

		resp.media = pet_record


api = falcon.API()
api.add_route('/pet', PetResource())
