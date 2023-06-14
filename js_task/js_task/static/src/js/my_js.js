odoo.define('js_task.my_js', function (require) {
"use strict";
console.log("------------------------Js called------------")

var publicWidget = require('web.public.widget');

publicWidget.registry.Test = publicWidget.Widget.extend({
    selector: '#mydiv',
    events: {
        'click .mybutton': '_onClickmybutton',
        'click .mysave': '_onClicksave',
    },

    _onClickmybutton: function () {
        $('#modelWindow').modal('show');
        console.log("MY SAVE", $('.mysave'))
        console.log("----",$('.modal-body input[name=name]').val(name));

    _onClicksave: function () {

        console.log("-----My function called----")
    	var x = document.getElementById("fname").value;
    	console.log("-----------",x)
    }
    },



});    


});