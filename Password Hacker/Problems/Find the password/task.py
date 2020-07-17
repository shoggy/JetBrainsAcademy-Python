from lxml import etree


def find_password(xml_string):
    root = etree.fromstring(xml_string)

    def rec(elem):
        t = elem.get("password")
        if t is not None:
            return t
        res = None
        for i in elem:
            res = rec(i)
            if res is not None:
                return res
        return res

    return rec(root)
