import tornado.web
from tornado.options import options

import json
from bson import ObjectId
from bson import BSON
from bson import json_util

import json

import pymongo

from handler.madb import MADB

ssDB = MADB();
ssDB.connectDB("userstudy","localhost",27017)

# class JSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o);
#         return json.JSONEncoder.default(self, o);

class SaveUserInfoHandler(tornado.web.RequestHandler):
    def post(self):
        print("save start")
        userInfo_age = self.get_argument("age")
        userInfo_gender = self.get_argument("gender")
        userInfo_studyinterest = self.get_argument("studyinterest")
        userInfo_academiclevel = self.get_argument("academiclevel")
        userInfo_experience = self.get_argument("experience")

        userid = ssDB.saveUserInfo({
            "userage": userInfo_age,
            "usergender": userInfo_gender,
            "userstudyinterest": userInfo_studyinterest,
            "useracademiclevel": userInfo_academiclevel,
            "userexperience": userInfo_experience,
        });
        print("userid", userid)
        self.set_header("Access-Control-Allow-Origin", "*")
        # self.write({"userid": JSONEncoder().encode(userid)})
        self.write("save ok")

class SaveAnswerInfoHandler(tornado.web.RequestHandler):
    def post(self):
        print("save answer start");
        user_question = self.get_argument("question");
        user_answer = self.get_argument("answer");
        user_answerinterval = self.get_argument("answerinterval");
        # print("answer", json.loads(answerinfo))
        ssDB.saveAnswerInfo({
            # "answerinfo": answerinfo,
            "question": user_question,
            "answer": user_answer,
            "answerinterval": user_answerinterval
        })
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write({"save": "ok"})