$(document).ready(function() {
    var sources = $("#sources a").each(function () {
            var href = $(this).attr("href");
            $("<option></option>").text(href).appendTo("#documentselect");
        }).map(function () { return $(this).attr("href") }).get(),
        docsrc = undefined;

    function set_document(src) {
        // var href = $(sources[i]).attr("href");
        $("#documentselect").val(src);
        if (docsrc !== src) {
            docsrc = src;
            $("iframe").attr("src", src)
        }
        // $("#toolbar .status").text(index+1+"/"+sources.length+" "+href);
    }
    set_document(sources[0]);

    $("#documentselect").on("change", function () {
        var src = $("#documentselect").val();
        console.log("change", src);
        if (docsrc !== src) { set_document(src); }
    });

    $("#toolbar #next").click(function () {
        var val = $("#documentselect").val(),
            index = sources.indexOf(val);
        if ((index + 1) < sources.length) {
            set_document(sources[index+1]);
        }
    });

    $("#toolbar #prev").click(function () {
        var val = $("#documentselect").val(),
            index = sources.indexOf(val);
        if (index > 0) {
            set_document(sources[index-1]);
        }
    });

    $("#toolbar #edit").click(function () {
        // enter the edit
        $("#toolbar #edit").toggleClass("active");
        if ($("#edit").hasClass("active")) {
            $("iframe").contents().find("body").attr("contenteditable", true);
        } else {
            $("iframe").contents().find("body").removeAttr("contenteditable");
        }
    });

    $("#toolbar #save").click(function () {
        // implement some basic save + git commit ?!
        var iframedoc = $("iframe").contents().get(0).documentElement,
            src = iframedoc.innerHTML;
        src = "<!DOCTYPE html><html>"+src+"</html>";
        $.ajax("/cgi-bin/saveas.cgi", {
            data: {
                path: docsrc,
                data: src
            },
            method: 'POST',
            dataType: 'json',
            success: function (data) {
                if (data.result) {
                    alert("saved");
                } else {
                    alert("Error: " + result.message);
                }
            },
            error: function (e) {
                alert("Error: " + e)
            }
        })

    });

});
