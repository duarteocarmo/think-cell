import pandas as pd

from thinkcell import Thinkcell


chart_1 = {
    "chart_name": "Chart1",
    "dataframe": pd.DataFrame(
        columns=["Company", "Ads", "Revenue", "Losses"],
        data=[["Amazon", 1, 11, 14], ["Slack", 8, 2, 15], ["Ford", 1, 2, 12]],
    )
}

chart_2 = {
    "chart_name": "Chart2",
    "dataframe": pd.DataFrame(
        columns=["Team", "Goals", "Headers", "Penalties"],
        data=[
            ["Manchester", 34, 20, 14],
            ["Chelsea", 40, 13, 20],
            ["Arsenal", 34, 30, 4],
        ],
    )
}

chart_3 = {
    "chart_name": "Chart3",
    "dataframe": pd.DataFrame(
        columns=["Metric", 2017, 2018, 2019],
        data=[["Revenue", 45, 24, 0], ["Employees", 10, 14, 0]],
    )
}

chart_4 = {
    "chart_name": "Chart4",
    "dataframe": pd.DataFrame(
        columns=["Metric", 2017, 2018, 2019],
        data=[["Expenses", 10, 10, 50], ["Revenues", 1, 1, 40]],
    )
}

chart_5 = {
    "chart_name": "Chart5",
    "dataframe": pd.DataFrame(
        columns=["Metric", 2017, 2018, 2019],
        data=[["Expenses", 10, 10, 50], ["Revenues", 1, 1, 40]],
    )
}

charts = [chart_1, chart_2, chart_3]

template_name = "complex-template.pptx"
filename = "complex-example-with-multiple-slides.ppttc"
tc = Thinkcell()
tc.add_template(template_name)

for chart in charts:
    tc.add_chart_from_dataframe(
        template_name=template_name,
        chart_name=chart["chart_name"],
        dataframe=chart["dataframe"],
    )
tc.add_textfield(template_name=template_name, field_name="chart_caption", text="First instance")

charts = [chart_1, chart_2, chart_4]
tc.add_template(template_name)

for chart in charts:
    tc.add_chart_from_dataframe(
        template_name=template_name,
        chart_name=chart["chart_name"],
        dataframe=chart["dataframe"],
    )
tc.add_textfield(template_name=template_name, field_name="chart_caption", text="Second instance")

tc.save_ppttc(filename=filename)