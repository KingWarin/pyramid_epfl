# * encoding: utf-8

from lxml import etree

from solute.epfl import components


def test_render_with_no_options(page):
    page.root_node = components.DatetimeInput(
    )
    page.handle_transaction()

    compo = page.root_node
    compo_html = etree.fromstring(compo.render())
    assert compo_html.attrib.get('epflid', None) == "%s" % compo.cid, "epflid not found"
    assert compo_html.attrib.get('id', None) == "%s" % compo.cid, "id not found"
    assert "epfl-datetimepicker" in compo_html.attrib.get('class', None), "class not found"

    input = compo_html.find("div").find("input")
    assert input is not None, "Could not find input"



def test_render_with_options(page):
    page.root_node = components.DatetimeInput(
        label="datetime_input",
        name="datetime_input",
        placeholder="datetime",
        compo_col=8,
        label_col=4,
        value= "2015.07.10",
    )
    page.handle_transaction()

    compo = page.root_node
    compo_html = etree.fromstring(compo.render())
    assert compo_html.attrib.get('epflid', None) == "%s" % compo.cid, "epflid not found"
    assert compo_html.attrib.get('id', None) == "%s" % compo.cid, "id not found"
    assert "epfl-datetimepicker" in compo_html.attrib.get('class', None), "class not found"

    label = compo_html.find("label")
    assert label is not None,"no label found"
    assert label.text == "datetime_input","wrong label text"
    assert "col-sm-4" in label.attrib.get("class",None),"wrong label col"

    input = compo_html.find("div").find("input")
    assert input is not None, "Could not find input"
    assert input.attrib.get("placeholder",None) is not None, "No Placeholder"
    assert input.attrib.get("value",None) == "2015.07.10", "wrong value"
    assert input.attrib.get("data-initial-value",None) == "2015.07.10", "wrong value"

    print compo.render()
    assert False

