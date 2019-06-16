from thinkcell import Thinkcell

template_name = "simple-template.pptx"
categories = ["Ads", "iPhones", "Other"]
chart_name = "Chart1"

data = [["Apple", 1, 11, 14], ["Google", 8, 2, 15], ["Microsoft", 1, 2, 12]]

tc = Thinkcell()
tc.add_template(template_name)
tc.add_chart(
    template_name=template_name,
    chart_name=chart_name,
    categories=categories,
    data=data,
)

tc.save_ppttc()
