$(document).ready(function() {
    var sources = $("#sources a").each(function () {
            var href = $(this).attr("href");
            $("<option></option>").text(href).appendTo("#documentselect");
        }).map(function () { return $(this).attr("href") }).get(),
        docsrc = undefined,
        curdocsrc;

    function set_document(src) {
        // var href = $(sources[i]).attr("href");
        var editing = $("#toolbar #edit").hasClass("active");
        $("#documentselect").val(src);
        if (docsrc !== src) {
            if (editing) {
                if (confirm("Save current document?")) {
                    save(src);
                    return;
                }
            }
            edit_end();
            docsrc = src;
            $("iframe").attr("src", src + "?t="+(new Date().toISOString()));
        }
        // $("#toolbar .status").text(index+1+"/"+sources.length+" "+href);
    }
    set_document(sources[0]);
    alert("foo");
    $("iframe").load(function () {
        console.log("iframe load");
    })

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
            $("#toolbar #save").show();
            $("#toolbar #revert").show();
        } else {
            edit_end();
        }
    });

    function edit_end () {
        $("#toolbar #save").show();
        $("#toolbar #revert").show();
        $("iframe").contents().find("body").removeAttr("contenteditable");
        $("#toolbar #edit").removeClass("active");
    }

    function get_doc_html() {
        var iframedoc = $("iframe").contents().get(0).documentElement,
            src = iframedoc.innerHTML;
        return "<!DOCTYPE html>\n<html>"+src+"</html>";
    }


    function set_doc_html (html) {
        var start = /<html>/i,
            end = /<\/html>/ig,
            iframedoc = $("iframe").contents().get(0).documentElement,
            startm,
            endm,
            m,
            startpos,
            ret;

        startm = start.exec(html);
        while (true) {
            m = end.exec(html);
            if (m) { endm = m; } else { break; }
        }
        startpos = startm.index + startm[0].length;
        ret = html.substr(startpos, (endm.index - startpos));
        iframedoc.innerHTML = ret;
        // console.log("set_doc_html", startm.index, startm[0], endm.index, endm[0], ret);
    }

    function save(nextsrc) {
        // implement some basic save + git commit ?!
        $.ajax("/cgi-bin/saveas.cgi", {
            data: {
                path: docsrc,
                data: src
            },
            method: 'POST',
            dataType: 'json',
            success: function (data) {
                if (data.result) {
                    edit_end();
                    if (nextsrc !== undefined) {
                        set_document(nextsrc);
                    } else {
                        alert("saved");
                    }
                } else {
                    alert("Error: " + result.message);
                }
            },
            error: function (e) {
                alert("Error: " + e)
            }
        })
    }
    $("#toolbar #save")
        .hide()
        .click(save);

    $("#toolbar #revert")
        .hide()
        .click(function () {
            // var src = get_doc_html();
            // set_doc_html("<!DOCTYPE>\n<html>FOO</html><p></p></html>\n\n");
            return;
            // implement some basic save + git commit ?!
            var iframedoc = $("iframe").contents().get(0).documentElement,
                src = iframedoc.innerHTML;
            src = "<!DOCTYPE html>\n<html>"+src+"</html>";
            $.ajax("/cgi-bin/load.cgi", {
                data: {
                    path: docsrc
                },
                method: 'POST',
                dataType: 'json',
                success: function (data) {
                    if (data.result) {
                        edit_end();
                        iframedoc.innerHTML = data.data;
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
