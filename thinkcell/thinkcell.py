import json


class Thinkcell(object):
    def __init__(self):
        self.charts = []
        #self.template_name = self.verify_template(template_name)
        #self.thinkcell_obj = dict()
        #self.thinkcell_obj["template"] = template_name
        #self.thinkcell_obj["data"] = []
        #self.categories = [None]

    def __str__(self):
        return str(self.thinkcell_obj)

    @staticmethod
    def verify_template(template_name):
        if not isinstance(template_name, str):
            raise TypeError(f"'{template_name}' is not a valid template file.")

        if not template_name.endswith(".pptx"):
            raise TypeError(f"'{template_name}' is not a valid Powerpoint file.")

        else:
            return template_name

    def add_chart(self, categories, rows):

        

    

    


template_name = "asdsa.pptx"

a = Thinkcell(template_name=template_name)
print(a)

# def add_chart(self, category_name, dataframe, chart_name, display_name):
#    names = dataframe.index.values
#    values = dataframe[category_name].values
#
#    header = [None] + [{"string": str(name).replace("(", "").replace("]", "").replace(", ", "-")} for name in names]
#    numbers = [{"string": display_name}] + [{"number": value} for value in values]
#
#    chart = dict()
#    chart["name"] = chart_name
#    chart["table"] = [header, [], numbers]
#
#    self.thinkcell_obj["data"].append(chart)
#
# def save_ppttc(self, filename):
#    with open(filename, "w") as outfile:
#        json.dump([self.thinkcell_obj], outfile)
