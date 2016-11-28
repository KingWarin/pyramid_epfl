# coding: utf-8
from solute.epfl.components.form.inputbase import FormInputBase


class PlainHtml(FormInputBase):

    # core internals
    template_name = "plain_html/plain_html.html"

    # js settings
    compo_js_auto_parts = False

    # derived attribute overrides
    value = ''  #: The HTML this component displays
    validation_type = 'text'  #: Validate this component as text.

    def __init__(self, page, cid,
                 name=None,
                 default=None,
                 label=None,
                 mandatory=None,
                 value=None,
                 strip_value=None,
                 validation_error=None,
                 fire_change_immediately=None,
                 placeholder=None,
                 readonly=None,
                 submit_form_on_enter=None,
                 input_focus=None,
                 input_style=None,
                 layout_vertical=None,
                 compo_col=None,
                 label_col=None,
                 validation_type=None,
                 label_style=None,
                 **extra_params):
        """ Simple component to display plain html

        Useage:
        .. code-block:: python

            PlainHtml(
                value=u'<h1>Some nice heading</h1><span>With a span</span>'
            )

        :param name: An element without a name cannot have a value
        :param default: Default value that may be pre-set or pre-selected
        :param label: Optional label describing the input field
        :param mandatory: Set to true if value has to be provided for this element in order to yield a valid form
        :param value: The actual value of the input element that is posted upon form submission
        :param strip_value: strip value if True in get value
        :param validation_error: Set during call of :func:`validate` with an error message if validation fails
        :param fire_change_immediately: Set to true if input change events should be fired immediately to the server.
                                        Otherwise, change events are fired upon the next immediate epfl event
        :param placeholder: Placeholder text that can be displayed if supported by the input
        :param readonly: Set to true if input cannot be changed and is displayed in readonly mode
        :param submit_form_on_enter: If true, underlying form is submitted upon enter key in this input
        :param input_focus: Set focus on this input when component is displayed
        :param input_style: Can be used to add additional css styles for the input
        :param validation_type: Set the validation type, default 'text'
        :param label: Label to be used for this text component.
        :param layout_vertical: Set to True if label should be displayed on top of the compo and not on the left before it
        :param label_col: Set the width of the label of the component (default: 2, max: 12)
        :param compo_col: Set the width of the complete component (default: 12, max: 12)
        :param label_style: Can be used to add additional css styles for the label
        """
        pass
