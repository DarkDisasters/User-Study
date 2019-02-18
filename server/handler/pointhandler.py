
import tornado.web
from tornado.options import options

import pymongo
from pymongo import MongoClient

import networkx as nx

import setting



from bson import BSON
from bson import json_util


from PIL import Image
import io
import os.path

import json

import subprocess

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("./index.html")












