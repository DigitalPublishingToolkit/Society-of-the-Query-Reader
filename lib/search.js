$(function () {
    function delayedaction (action, time) {
        if (time === undefined) { time = 1000; }
        var timeout_id = null,
            that = {};
        function cancel () {
            if (timeout_id !== null) {
                window.clearTimeout(timeout_id);
                timeout_id = null;
            }
        }
        that.cancel = cancel;
        function performAction () {
            action();
            timeout_id = null;
        }
        that.do_soon = function () {
            cancel();
            timeout_id = window.setTimeout(performAction, time);
        };
        that.do_now = function () {
            performAction();
        };
        return that;
    }

    var results = {},
        waiting = false,
        tid = null,
        show = function (data) {
            $("#resultsraw").text(JSON.stringify(data, null, 4));
            $("#results").text("");
            if (data.correctedh) {
                var cdiv = $("<div></div>")
                  .addClass("corrected")
                  .appendTo("#results"),
                clink = $("<a></a>")
                  .attr("href", "?q="+encodeURI(data.corrected))
                  .html(data.correctedh)
                  .click(function () {
                    $('#q').val(data.corrected);
                    search.do_soon();
                    return false;
                  })

                  $("<span>Did you mean? <span>").appendTo(cdiv);
                  clink.appendTo(cdiv);
            }
            $(data.results).each(function (i, d) {
                var div = $("<div></div>").addClass("results").appendTo("#results"),
                    title = $("<div></div>").addClass("title").appendTo(div),
                    titlelink = $("<a></a>").attr("href", d.path).text(d.title).appendTo(title);
                // console.log("d", d);
                $("<div></div>").addClass("highlights").html(d.highlights).appendTo(div);
            });
        },
        search = delayedaction(function () {
            // console.log("search", q);
            var q = $("#q").val();
            if (results[q] !== undefined) {
                show(results[q]);
                return;
            }
            $.ajax('/cgi-bin/searchj.cgi', {
                data: {'q': q},
                dataType: 'json',
                success: function (data) {
                    results[q] = data;
                    show(data);;
                }
            });
        }, 500);

    $('#q')
      .focus()
      .bind("keyup", function () {
        search.do_soon();
      });


})