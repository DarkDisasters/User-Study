function FunctionHub(){
    var _this = this;
    var userid ;

    this._init = function(){
        var timestart,timeend, interval, iid
        userid = userid;
        this._age = ""
        this._gender = ""
        this._studyinterest = ""
        this._academiclevel = ""
        this._experience = ""
    }

    this.loadPageTime = function(){
        timestart = new Date()
    }

    this.nextButtonTime = function(){
        console.log("timestart", timestart)
        timeend = new Date();
        var intervalms = (timeend - timestart);
        var days = Math.floor(intervalms/(24*3600*1000))
        
        var level1 = intervalms%(24*3600*1000)
        var hours = Math.floor(level1/(3600*1000))

        var level2 = intervalms%(3600*1000)
        var minutes = Math.floor(level2/(60*1000))

        var level3 = intervalms%(60*1000)
        var seconds = Math.round(level3/1000)

        interval = hours * 3600 + minutes*60 + seconds
        console.log("timeend", timeend)
        console.log("interval",interval)
        timestart = timeend
    }

    this.nextButton = function(){
        this.nextButtonTime();
        var self = this;
        id = idHandler("*")
        this._answer = $('input:radio[name="answer"]:checked').val();
        this._question = $('#question').text()
        var resultinfo = {"question": this._question, "answer": this._answer, "answerinterval": interval}
        var answerinfo = {"question": this._question, "resultinfo": resultinfo}
        console.log("resultinfo", resultinfo)
        console.log("userid", id)
        var formData = new FormData()
        // formData.append('answerinfo', resultinfo)
        formData.append('question',this._question)
        formData.append('answer',this._answer)
        formData.append('answerinterval',interval)
        var url = "http://localhost:4000/saveanswerinfo"
        lSendUrl("POST", url, formData, self.successSaveAnswer)
    }

    this.successSaveAnswer = function(response, self){
        console.log("save answer ok")
    }

    this.saveUserInfo = function(){
        var self = this;
        var formData = new FormData();
        formData.append("age", this._age)
        formData.append("gender", this._gender)
        formData.append("studyinterest", this._studyinterest)
        formData.append("academiclevel", this._academiclevel)
        formData.append("experience", this._experience);
        var url = "http://localhost:4000/saveUserInfo";
        lSendUrl("POST", url, formData, self.successSave)
    }

    this.successSave = function(response, self){
        console.log("response", response)
        userid = response;
        idHandler(userid);
    }

    this.loadQuestion = function(){
        var self = this;
        var formData = new FormData();
        formData.append('name', "loadQuestion")
        var url = "http://localhost:4000/transferpage";
        lSendUrl("POST", url, formData, self.successLoad)
    }

    this.successLoad = function(response, self){
        console.log("Load OK!")
    }

    this.submit = function(){
        this._age = $('input[name="age"]').val();
        this._gender = $('input:radio[name="gender"]:checked').val();
        this._studyinterest = $('input:radio[name="studyinterest"]:checked').val();
        this._academiclevel = $('input:radio[name="academiclevel"]:checked').val();
        this._experience = $('input:radio[name="experience"]:checked').val();
        if(this._age == ""){
            window.alert("empty age")
        }
        else{
            this.saveUserInfo()
            // this.loadQuestion()
        }
        console.log("age", this._age)
        console.log("age", this._gender)
        console.log("age", this._studyinterest)
        console.log("age", this._academiclevel)
        console.log("experience", this._experience)

    }

    this.loadimgpage = function(){
        var self = this;
        var formData = new FormData();
        formData.append("name", "loadimgpage")
        var url = "http://localhost:4000/loadQuestion";
        lSendUrl("POST", url, formData, self.successLoad)
    }

    this._init()
}