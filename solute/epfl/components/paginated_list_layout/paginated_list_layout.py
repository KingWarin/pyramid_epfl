# coding: utf-8

"""

"""

from solute.epfl.components import PrettyListLayout


class PaginatedListLayout(PrettyListLayout):
    """
    A searchable list layout. Its content is configured using get_data()
    example

    .. code-block:: python

        data = []
        for i in range(0, 100):
            data.append({'id': i, "data": "test" + str(i)})

    """
    new_style_compo = True
    show_pagination = True  #: Set to true to show the pagination bar.
    show_search = True  #: Set to true to enable the search field.
    search_placeholder = "Search..."  #: Placeholder text for the search input.

    search_focus = False  #: Set to true if the search field should receive focus on load.

    theme_path = ['pretty_list_layout/theme', '<paginated_list_layout/theme']

    js_parts = []
    js_name = PrettyListLayout.js_name + [(
                                              'solute.epfl.components:paginated_list_layout/static',
                                              'paginated_list_layout.js'
                                          )]

    compo_js_params = ['row_offset', 'row_limit', 'row_count', 'row_data', 'show_pagination', 'show_search',
                       'search_focus']
    compo_js_name = 'PaginatedListLayout'
    #: Add the specific list type for the paginated list layout. see :attr:`ListLayout.list_type`
    list_type = PrettyListLayout.list_type + ['paginated']

    def __init__(self, page, cid, show_search=None, show_pagination=None, search_placeholder=None,
                 search_focus=None, height=None, **kwargs):
        """Paginated list using the PrettyListLayout based on bootstrap. Offers searchbar above and pagination below
        using the EPFL theming mechanism.

        :param show_search: Toggle weather the search field is shown or not.
        :param show_pagination: Toggle weather the pagination is shown or not.
        :param search_placeholder: The placeholder text for the search input.
        :param search_focus: Toggle weather the search field receives focus on load or not.
        :param height: Set the list to the given height in pixels.
        """
        super(PaginatedListLayout, self).__init__(page, cid, show_search=show_search,
                                                  show_pagination=show_pagination,
                                                  search_placeholder=search_placeholder,
                                                  search_focus=search_focus,
                                                  height=height, **kwargs)
