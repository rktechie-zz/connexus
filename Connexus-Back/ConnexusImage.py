from google.appengine.ext import ndb

import logging

class Image(ndb.Model):

	imageId = ndb.IntegerProperty()
	streamId = ndb.IntegerProperty()
	blobKey = ndb.BlobKeyProperty()
	creationDate = ndb.DateProperty(auto_now_add=True)
	comment = ndb.StringProperty()
	lat = ndb.FloatProperty(default=30.267153)
	lon = ndb.FloatProperty(default=-97.743061)

	@staticmethod
	def addImage(streamId, imageId, blobKey, loc):
		image = Image()
		image.streamId = streamId
		image.imageId = imageId
		image.blobKey = blobKey
		image.lat = loc[0]
		image.lon = loc[1]
		image.put()