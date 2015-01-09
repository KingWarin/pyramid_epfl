epfl.paginated_list_goto = function (element, cid, row_offset, row_limit, row_data) {
    if ($(element).hasClass('disabled')) {
        return;
    }
    var event = epfl.make_component_event(
        cid,
        'set_row',
        {
            row_offset: row_offset,
            row_limit: row_limit,
            row_data: row_data
        });
    epfl.send(event);
};


var search_{{ compo.cid }}_timeout;
var search_{{ compo.cid }} = $('#' + '{{ compo.cid }}_search');
search_{{ compo.cid }}
    .keypress(function (e) {
        var elm = this;
        function submit() {
            epfl.paginated_list_goto($(elm),
                                     "{{ compo.cid }}",
                                     parseInt({{ compo.row_offset }}),
                                     parseInt({{ compo.row_limit }}),
                                     {search: $(elm).val()});
        }

        if (e.key == 'Enter') {
            submit();
        }
        if (search_{{ compo.cid }}_timeout) {
            clearTimeout(search_{{ compo.cid }}_timeout);
        }
        search_{{ compo.cid }}_timeout = window.setTimeout(submit, 500);
    })
    .focus()[0]
    .setSelectionRange(search_{{ compo.cid }}.val().length, search_{{ compo.cid }}.val().length);
