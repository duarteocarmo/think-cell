import json
import warnings
from datetime import datetime
from pprint import pprint

# TODO handle duplicate template names


class Thinkcell(object):
    def __init__(self):
        self.charts = []

    def __str__(self):
        return str(self.charts)

    @staticmethod
    def verify_template(template_name):
        if not isinstance(template_name, str):
            raise TypeError(
                f"'{template_name}' is not a valid template file."
            )

        if not template_name.endswith(".pptx"):
            raise TypeError(
                f"'{template_name}' is not a valid Powerpoint file."
            )

        else:
            return template_name

    @staticmethod
    def transform_input(data_element):

        if isinstance(data_element, datetime):
            return {"date": data_element.strftime("%Y-%m-%d")}

        if isinstance(data_element, str):
            return {"string": data_element}

        if isinstance(data_element, (int, float)):
            return {"number": data_element}

        else:
            raise ValueError(
                f"{data_element} of type {type(data_element)} is not acceptable."
            )

    def add_template(self, template_name):
        self.verify_template(template_name)
        self.charts.append({"template": template_name, "data": []})

    def add_chart(self, template_name, chart_name, categories, data):
        available_templates = [page["template"] for page in self.charts]

        if template_name not in available_templates:
            raise ValueError(
                f"{template_name} does not exist, please create one first."
            )

        if not isinstance(chart_name, str):
            warnings.warn(
                f"Your chart name is not a string, we will convert it into one. But wanted to make sure you were aware."
            )

        for data_list in data:
            if len(data_list) != len(categories) + 1:
                raise ValueError(
                    f"Your categories should be the equal to the length of your data lists - 1. Your data element {data_list} is of size {len(data_list)} but should be of size {len(categories) + 1}."
                )

        chart_dict = {}
        chart_dict["name"] = str(chart_name)
        chart_categories = [None] + [
            self.transform_input(element) for element in categories
        ]
        chart_dict["table"] = [chart_categories, []]

        for data_list in data:
            chart_dict["table"].append(
                [self.transform_input(el) for el in data_list]
            )

        for page in self.charts:
            if page["template"] == template_name:
                page["data"].append(chart_dict)

    def save_ppttc(self, filename):
        if not isinstance(filename, str):
            raise ValueError(
                f"A filename is normally a string, yours is not."
            )

        if not filename.endswith(".ppttc"):
            raise ValueError(
                f"You want to save your file as a '.ppttc' file, not a '{filename}'. Visit https://www.think-cell.com/en/support/manual/jsondataautomation.shtml for more information."
            )

        if not self.charts:
            raise ValueError(
                f"Please add data before saving to a template file by using 'add_template' and then 'add_chart'."
            )

        else:
            with open(filename, "w") as outfile:
                json.dump(self.charts, outfile)
                return True
