var link_bind = function(e) {
    e.preventDefault();
    var anchor = e.target || e.srcElement;
    if (anchor.getAttribute("data-bind") != "true")
        return true;
    var call = anchor.href;
    var params = anchor.getAttribute("data-params");

    if (params !== null)
        eval(call + "('" + params + "')");
    else
        eval(call + "()");
    return false;
};

var form_bind = function (e) {
    e.preventDefault();
    var form = e.target || e.srcElement;
    if (form.getAttribute("data-bind") != "true")
        return true;
    var action = form.action;

    var formdata = {};
    for (var i = 0, ii = form.length; i < ii; ++i) {
        var input = form[i];
        if (input.name && input.type !== "file")
            formdata[input.name] = input.value;
    }

    var params = form.getAttribute("data-params");

    exec = action + "('" + JSON.stringify(formdata);
    exec += params !== null ? ("', '" + params) : "";
    exec += "')";
    console.log(exec);
    eval(exec);
    return false;
};


var bind_all = function () {
    var anchors = document.getElementsByTagName("a");
    var forms = document.getElementsByTagName("form");
    for (var i = anchors.length - 1; i >= 0; i--) {
        if(!anchors[i].classList.contains("htmlpy-activated")){
            anchors[i].onclick = link_bind;
            anchors[i].classList.add("htmlpy-activated");
        }
    }

    for (var fi = forms.length - 1; fi >= 0; fi--) {
        if(!forms[fi].classList.contains("htmlpy-activated")){
            forms[fi].onsubmit = form_bind;
            // elem = forms[fi];
            // for (i = 0, ii = elem.length; i < ii; ++i) {
            //     var input = elem[i];
            //     if (input.type === "file") {
            //         var fileboxname = input.getAttribute("name");
            //         var filter = input.getAttribute("data-filter");
            //         var disabledInput = document.createElement("input");
            //         disabledInput.setAttribute("disabled", "disabled");
            //         disabledInput.setAttribute("name", fileboxname);
            //         disabledInput.setAttribute("id", fileboxname + "_path");
            //         input.parentNode.insertBefore(disabledInput, input.nextSibling);
            //         var button = document.createElement("button");
            //         button.innerHTML = "Choose file";
            //         button.setAttribute("data-display", fileboxname + "_path");
            //         button.setAttribute("data-filter", filter);
            //         button.onclick = file_dialog;
            //         input.parentNode.insertBefore(button, disabledInput.nextSibling);
            //         input.style.display = "none";
            //         elem[i].remove();
            //     }
            // }
            forms[fi].classList.add("htmlpy-activated");
        }
    }
};

bind_all();
document.body.addEventListener("DOMNodeInserted", bind_all);
document.body.classList.add("htmlPy-active");
