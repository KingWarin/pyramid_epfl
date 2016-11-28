from solute.epfl.components.form.inputbase import FormInputBase


class Toggle(FormInputBase):
    """
    A form checkbox styled as toggle.

    Typically, this component is used in a form:

    .. code:: python

        form = Form(node_list=[Toggle(label="Enable/Disable user:", name="user_enable_toggle")])

    """

    # core internals
    template_name = "toggle/toggle.html"
    js_name = FormInputBase.js_name + [("solute.epfl.components:toggle/static", "bootstrap-switch.min.js"),
                                       ("solute.epfl.components:toggle/static", "toggle.js")]
    css_name = FormInputBase.css_name + [("solute.epfl.components:toggle/static", "bootstrap-switch.min.css"),
                                         ("solute.epfl.components:toggle/static", "toggle.css")]

    # js settings
    compo_js_name = 'Toggle'

    # derived attribute overrides
    validation_type = 'bool'  #: Validate this component as a boolean.
    default = False  #: The default value of the toggle.

    # custom compo attributes
    on_text = "on"  #: The text to be displayed if toggle is set to on.
    off_text = "off"  #: The text to be displayed if toggle is set to off.

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
                 label_style=None,
                 input_style=None,
                 layout_vertical=None,
                 compo_col=None,
                 label_col=None,
                 validation_type=None,
                 on_text=None,
                 off_text=None,
                 **extra_params):
        """A toggling form input.

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
        :param label_style: Can be used to add additional css styles for the label
        :param input_style: Can be used to add additional css styles for the input
        :param layout_vertical: Set to true if label should be displayed on top of the input and not on the left before
                                it
        :param compo_col: Set the width of the complete input component (default: max: 12)
        :param label_col: Set the width of the complete input component (default: 2)
        :param validation_type: Set the validation type, default 'text'
        :param on_text: Text shown for the "on" state evaluating to a value of True.
        :param off_text: Text shown for the "off" state evaluating to a value of False.
        """
        pass
