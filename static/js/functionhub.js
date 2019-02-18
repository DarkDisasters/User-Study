function FunctionHub(){
    var _this = this;

    this.init = function(){
    }

    this.submit = function(){
        this._age = $('input[name="age"]').val();
        this._gender = $('input:radio[name="gender"]:checked').val();
        console.log("age", this._age)
    }
}