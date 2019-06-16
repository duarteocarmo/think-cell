import pytest
from thinkcell import Thinkcell


class TestThinkcell(object):
    def test_init(self):
        tc = Thinkcell()
        assert tc.charts == []

    def test_str(self):
        tc = Thinkcell()
        assert hasattr(tc, "__str__") is True

    def test_verify_template_1(self):
        template_name = "not a file name"
        with pytest.raises(TypeError) as e_info:
            Thinkcell.verify_template(template_name)

    def test_verify_template_2(self):
        template_name = 5
        with pytest.raises(TypeError) as e_info:
            Thinkcell.verify_template(template_name)

    def test_verify_template_3(self):
        template_name = "example.pptx"
        assert Thinkcell.verify_template(template_name) == template_name

    def test_add_page(self):
        tc = Thinkcell()
        template = "example.pptx"
        tc.add_page(template)
        assert tc.charts == [{"template": template, "data": []}]
