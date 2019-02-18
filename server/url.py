#!/usr/bin/env python
#coding:utf-8

import sys
# from imp import reload
# reload(sys)
# sys.setdefaultencoding('utf-8')

from handler.pointhandler import IndexHandler
from handler.pointhandler import LoadQuestionHandler
from handler.pointhandler import TransferPageHandler
from handler.dbHandler import SaveUserInfoHandler

# from handler.pointhandler import MAMinardHandler
# from handler.pointhandler import MAPlayfairHandler
# from handler.pointhandler import MABoxplotHandler
# from handler.pointhandler import GACirclepackingHandler
# from handler.pointhandler import GATreemapHandler
# from handler.pointhandler import GDRectHandler
# from handler.pointhandler import GDScatterplotHandler
# from handler.pointhandler import GDPathHandler

url=[
	(r'/', IndexHandler),
    (r'/saveUserInfo', SaveUserInfoHandler),
    (r'/transferpage', TransferPageHandler),
    (r'/loadQuestion', LoadQuestionHandler),
]