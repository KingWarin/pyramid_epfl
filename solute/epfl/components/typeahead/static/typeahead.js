epfl.TypeAhead = function(cid, params) {
    epfl.PaginatedListLayout.call(this, cid, params);
};
epfl.TypeAhead.inherits_from(epfl.PaginatedListLayout);

epfl.TypeAhead.prototype.handle_local_click = function (event) {
    epfl.PaginatedListLayout.prototype.handle_local_click.call(this, event);
    var btn = this.dropdown_toggle;

    if (btn.is(event.target)) {
        this.list.toggle();
    }
};

Object.defineProperty(epfl.TypeAhead.prototype, 'list', {
    get: function () {
        return this.elm.children('.epfl-list');
    }
});

Object.defineProperty(epfl.TypeAhead.prototype, 'search_input', {
    get: function () {
        return this.elm.find('#' + this.cid + '_search');
    }
});

Object.defineProperty(epfl.TypeAhead.prototype, 'dropdown_toggle', {
    get: function () {
        return this.elm.children('div').children('div.btn.fa.fa-chevron-down');
    }
});

epfl.TypeAhead.prototype.update_visibility = function (event) {
    var available_entries = this.elm.find('[data-parent-epflid=' + this.cid + ']');
    if (available_entries.length == 0 ||
        (!this.search_input.is(':focus') && this.elm.find(':hover').length == 0)) {
        this.list.hide();
    } else {
        this.list.show();
    }
};

epfl.TypeAhead.prototype.after_response = function (data) {
    epfl.PaginatedListLayout.prototype.after_response.call(this, data);

    var obj = this;
    obj.list.hide().css({
        position: 'absolute',
        padding: 0,
        zIndex: 10,
        width: '100%',
        height: 200,
        overflow: 'auto'
    });

    obj.search_input
        .focus(function () {
            update_visibility();
        })
        .focusout(function () {
            update_visibility();
        });
    obj.elm
        .mouseenter(function () {
            update_visibility();
        })
        .mouseout(function () {
            update_visibility();
        });

    this.elm.keypress(function (event) {
        var available_entries = obj.elm.find('[data-parent-epflid=' + obj.cid + ']');
        var active_entry = obj.elm.find('[data-parent-epflid=' + obj.cid + '].active');
        var position = -1;

        available_entries.each(function (i, elm) {
            if (active_entry.is(elm)) {
                position = i;
            }
            $(elm).removeClass('active');
        });

        switch (event.keyCode) {
            case 13: // enter
                active_entry.click();
                break;
            case 38: // arrow up
                position -= 1;
                break;
            case 40: // arrow down
                position += 1;
                break;
        }
        if (position == -2) {position = -1;} // Only happens on key up with no selected entry.

        position %= available_entries.length;
        available_entries.eq(position).addClass('active');
        setTimeout(function () {
            var current_entry = available_entries.eq(position);
            obj.list.scrollTop(
                current_entry.offset().top - obj.list.offset().top + obj.list.scrollTop() - current_entry.outerHeight()
            );
        }, 0);
    });


    function update_visibility() {
        setTimeout(function () {
            obj.update_visibility();
        }, 0);
    }
    update_visibility();

};