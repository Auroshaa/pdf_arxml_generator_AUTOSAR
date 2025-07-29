from lxml import etree

def generate_arxml(data, selected_names):
    root = etree.Element("AUTOSAR")
    containers = etree.SubElement(root, "CONTAINERS")

    for entry in data:
        if entry["name"] in selected_names:
            container = etree.SubElement(containers, "CONTAINER")
            etree.SubElement(container, "SHORT-NAME").text = entry["name"]
            etree.SubElement(container, "ADDRESS").text = entry["address"]
            etree.SubElement(container, "DESCRIPTION").text = entry["description"]

    return etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8")
