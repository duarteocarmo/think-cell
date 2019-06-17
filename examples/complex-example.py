from thinkcell import Thinkcell


chart_1 = {
    "categories": ["Employees", "Revenue", "Other"],
    "chart_name": "Chart1",
    "data": [["Apple", 200, 1.5, 10], ["Amazon", 100, 1.0, 12], ["Slack", 50, 0.5, 16]],
}

chart_2 = {
    "categories": ["Goals", "Headers", "Penalties"],
    "chart_name": "Chart2",
    "data": [
        ["Manchester", 34, 20, 14],
        ["Chelsea", 40, 13, 20],
        ["Arsenal", 34, 30, 4],
    ],
}

chart_3 = {
    "categories": [2017, 2018, 2019],
    "chart_name": "Chart3",
    "data": [["Revenue", 45, 24, 0], ["Employees", 10, 14, 0]],
}

charts = [chart_1, chart_2, chart_3]

template_name = "complex-template.pptx"
filename = "complex-example.ppttc"
tc = Thinkcell()
tc.add_template(template_name)

for chart in charts:
    tc.add_chart(
        template_name=template_name,
        chart_name=chart["chart_name"],
        categories=chart["categories"],
        data=chart["data"],
    )

tc.save_ppttc(filename=filename)
