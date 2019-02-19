
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
		self.redirect('./loadQuestion')	


# class TransferPageHandler(tornado.web.RequestHandler):

# 	def post(self, *args, **kwargs):
# 		# ltype = self.get_argument("name")
# 		# print("name", ltype)
# 		# if ltype == "loadQuestion":
# 		# self.render("./template/testpage.html",page_title = "我的博客",)
# 			# print("transferpage ok")
# 		self.redirect('/loadQuestion')
# 	get = post
			

class LoadQuestionHandler(tornado.web.RequestHandler):
	def get(self, *args, **kwargs):
		self.render("./template/testpage.html",page_title = "我的博客",)
	
	def	post(self):
		self.render("./template/imgstudypage.html")
		print("loadimgpage ok")
		# self.redirect("http://localhost:4000/imgstudypage")
		

class ImgStudyPageHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("./template/imgstudypage.html")
		print("loadimgpage ok")












