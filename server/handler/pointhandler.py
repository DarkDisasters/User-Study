
import tornado.web
from tornado.options import options
import url 

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
		self.render("./template/index.html")
	def post(self):
		ltype = self.get_argument("name")
		print("name", ltype)
		if ltype == "loadQuestion":
			self.redirect('./loadQuestion')	


class TransferPageHandler(tornado.web.RequestHandler):
	def post(self):
		ltype = self.get_argument("name")
		print("name", ltype)
		if ltype == "loadQuestion":
			# self.render("./template/index.html",page_title = "我的博客",)
			# print("transferpage ok")
			self.redirect('http://localhost:4000/loadQuestion')
			

class LoadQuestionHandler(tornado.web.RequestHandler):
	def get(self):
		print("getok")
		self.render("./template/testpage.html",page_title = "我的博客",)
		print("ok")
		












