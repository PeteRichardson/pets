import pets
import rethinkdb as r
import json
import datetime
import time
import random


if __name__ == '__main__':

	conn = r.connect(host='192.168.1.207', db='petsdb', password='')

	for _ in xrange(1,5):
		pet = pets.Pet.random()
		ts = datetime.datetime.now()
		print "{} - Inserting: {}".format(ts, pet)
		row = pet.__dict__
		row["created"] = str(ts)

		r.table('pets').insert(row).run(conn)
		time.sleep(random.randint(1,3))
	