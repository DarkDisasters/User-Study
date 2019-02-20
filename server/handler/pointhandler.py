
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

class GetImgListHandler(tornado.web.RequestHandler):
	def post(self):
		imgList = glob.glob("./img/*.jpg");
		
		x = {}

		for img in imgList:
			imgName = basename(img).split(".")[0]
			x[imgName] = img;
		print('img list', imgList[0: 7], len(imgList))

		self.set_header('Access-Control-Allow-Origin', "*")
		self.write({'img', x})









