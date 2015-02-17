# coding: utf-8

"""

"""

from solute.epfl.core import epflcomponentbase
from solute.epfl.components import PaginatedListLayout
from solute.epfl.core.epflutil import has_permission_for_route


class LinkListLayout(PaginatedListLayout):
    default_child_cls = epflcomponentbase.ComponentBase
    data_interface = {'id': None,
                      'text': None,
                      'url': None}
    
    theme_path = PaginatedListLayout.theme_path + ['link_list_layout/theme']
        
    js_parts = PaginatedListLayout.js_parts + ['link_list_layout/link_list_layout.js']

    compo_state = PaginatedListLayout.compo_state + ['links']
    
    links = []

    auto_update_children = False

    def get_data(self, row_offset=None, row_limit=None, row_data=None):
        links = []
        for i, link in enumerate(self.links):
            if not has_permission_for_route(self.request, link['url']):
                continue
            links.append({'id': i,
                          'text': link['text'],
                          'url': link['url']})
            try:
                links[-1]['url'] = self.page.get_route_path(links[-1]['url']) or links[-1]['url']
            except KeyError:
                pass
        return links