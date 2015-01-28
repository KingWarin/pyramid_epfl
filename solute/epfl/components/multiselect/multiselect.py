from solute.epfl.core import epflcomponentbase
import json


class MultiSelectEntry(epflcomponentbase.ComponentBase):
    template_name = "multiselect/multiselect_entry.html"
    asset_spec = "solute.epfl.components:multiselect/static"


class MultiSelect(epflcomponentbase.ComponentContainerBase):

    """

    A container component that renders the components as a multi-select list

    The nested components can be of arbitrary type, but they must have the epfl id attribute
    set in their outmost html element

    """

    template_name = "multiselect/multiselect.html"
    js_parts = epflcomponentbase.ComponentContainerBase.js_parts + ["multiselect/multiselect.js"]
    asset_spec = "solute.epfl.components:multiselect/static"

    css_name = ["multiselect.css", "bootstrap.min.css",
                "css/font-awesome/css/font-awesome.min.css"]
    js_name = ["multiselect.js"]

    compo_config = epflcomponentbase.ComponentContainerBase.compo_config + \
        ["show_search", "grouped"]

    compo_state = epflcomponentbase.ComponentContainerBase.compo_state + \
        ["selected_child_cids", "hidden_child_cids", "selected_child_ids", "scroll_position",
            "search_string", "default_out_multiselect_transfer_cid"]

    default_child_cls = MultiSelectEntry
    selected_child_cids = set()
    # : smart components may re-generate cids for its child components. In this case, this list can be used to remember the selected components by its id. It will be automatically moved into cids of the selected_child_cids
    selected_child_ids = set()
    hidden_child_cids = set()
    scroll_position = 0
    show_search = False
    search_string = ""
    default_out_multiselect_transfer_cid = None

    grouped = False

    def handle_selected(self, child_cid):
        if not child_cid in self.selected_child_cids:
            self.selected_child_cids.add(child_cid)
        self.redraw()

    def handle_unselected(self, child_cid):
        self.selected_child_cids.discard(child_cid)
        self.redraw()

    def handle_double_click(self, child_cid):
        if not self.default_out_multiselect_transfer_cid is None:
            transfer = self.page.components[self.default_out_multiselect_transfer_cid]
            transfer.transfer_single_element(child_cid)
        self.redraw()

    def handle_scrolled(self, scroll_position):
        self.scroll_position = scroll_position

    def _handle_search_simple(self):
        searchstring = self.search_string.lower()
        for compo in self.components:
            try:
                if not searchstring in compo.data["value"].lower():
                    self.hidden_child_cids.add(compo.cid)
                    # this component is also not selected anymore
                    self.selected_child_cids.discard(compo.cid)
            except KeyError:
                pass

    def _handle_search_grouped(self):
        number_of_matched_entries_for_group = 0
        current_group_cid = None
        current_group_matched = False
        searchstring = self.search_string.lower()
        for compo in self.components:
            if "multiselect_group" in compo.data:
                if (not current_group_cid is None) and (current_group_matched == False) and (number_of_matched_entries_for_group == 0):
                    self.hidden_child_cids.add(current_group_cid)
                try:
                    if not searchstring in compo.data["value"].lower():
                        current_group_matched = False
                    else:
                        current_group_matched = True
                except KeyError:
                    current_group_matched = False

                current_group_cid = compo.cid
                number_of_matched_entries_for_group = 0
            else:
                if (current_group_matched == True):
                    # if the group matches, we don't hide this group member
                    number_of_matched_entries_for_group += 1
                    continue
                try:
                    if not searchstring in compo.data["value"].lower():
                        self.hidden_child_cids.add(compo.cid)
                        # this component is also not selected anymore
                        self.selected_child_cids.discard(compo.cid)
                    else:
                        number_of_matched_entries_for_group += 1
                except KeyError as e:
                    pass
        # check for the last group
        if (not current_group_cid is None) and (current_group_matched == False) and (number_of_matched_entries_for_group == 0):
            self.hidden_child_cids.add(current_group_cid)

    def handle_search(self, search_string):
        self.search_string = search_string.strip()
        self.hidden_child_cids.clear()
        if self.grouped == False:
            self._handle_search_simple()
        else:
            self._handle_search_grouped()
        self.redraw()

    def update_children(self, force=False):
        result = epflcomponentbase.ComponentContainerBase.update_children(self, force=force)
        if (len(self.selected_child_ids) > 0):
            for compo in self.components:
                if compo.id in self.selected_child_ids:
                    self.selected_child_cids.add(compo.cid)
            self.selected_child_ids.clear()
        return result


class MultiSelectTransfer(epflcomponentbase.ComponentBase):

    """
    Provides functionality to move items from one multi select to another.


    """

    template_name = "multiselect/multiselecttransfer.html"
    js_parts = epflcomponentbase.ComponentBase.js_parts[:]
    js_parts.append("multiselect/multiselecttransfer.js")
    asset_spec = "solute.epfl.components:multiselect/static"

    css_name = ["bootstrap.min.css",
                "css/font-awesome/css/font-awesome.min.css"]
    js_name = ["multiselecttransfer.js"]
    source_multi_select_cid = None
    target_multi_select_cid = None

    def handle_transfer(self):
        """
        Called when transfer button is clicked.
        Overwrite this method if source or target component is a smart component!
        """

        source_multiselect = self.page.components[self.source_multi_select_cid]
        target_multiselect = self.page.components[self.target_multi_select_cid]
        if source_multiselect.is_smart() or target_multiselect.is_smart():
            # do nothing, source/target component is smart. This method has to be overwritten.
            return
        for cid in source_multiselect.selected_child_cids:
            source_multiselect.send(self.page.components[cid].id)
            target_multiselect.switch_component(target_multiselect.cid, cid)
            target_multiselect.selected_child_cids.add(cid)
        source_multiselect.selected_child_cids.clear()
        source_multiselect.redraw()
        target_multiselect.redraw()

    def transfer_single_element(self, cid):
        """
        Can be used to transfer a simple element (e.g. to directly handle double-clicks on multiselects).
        Overwrite this method if source or target component is a smart component!
        """

        source_multiselect = self.page.components[self.source_multi_select_cid]
        target_multiselect = self.page.components[self.target_multi_select_cid]
        if source_multiselect.is_smart() or target_multiselect.is_smart():
            # do nothing, source/target component is smart. This method has to be overwritten.
            return

        source_multiselect.send(self.page.components[cid].id)
        target_multiselect.switch_component(target_multiselect.cid, cid)
        target_multiselect.selected_child_cids.add(cid)
        source_multiselect.selected_child_cids.discard(cid)
        source_multiselect.redraw()
        target_multiselect.redraw()
