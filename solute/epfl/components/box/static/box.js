epfl.Box = function(cid, params) {
    epfl.ComponentBase.call(this, cid, params);
};
epfl.Box.inherits_from(epfl.ComponentBase);


epfl.Box.prototype.handle_local_click = function (event) {
    epfl.ComponentBase.prototype.handle_local_click.call(this, event);

    if (!$(event.target).parent().hasClass('epfl_box_remove_button')) {
        return;
    }
    event.stopImmediatePropagation();
    event.preventDefault();

    if (this.elm.hasClass('epfl_hover_box') && !this.params.hover_box_remove_on_close) {
        this.send_event("hide", {});
    } else {
        this.send_event("removed", {});
    }
};
