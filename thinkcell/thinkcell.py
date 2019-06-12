import json

class Thinkcell(object):
    def __init__(self, template_name):
        self.template_name = template_name
        self.thinkcell_obj = dict()
        self.thinkcell_obj["template"] = template_name
        self.thinkcell_obj["data"] = []
    
    def __str__(self):
        return str(self.thinkcell_obj)
    
    def add_chart(self, category_name, dataframe, chart_name, display_name):
        names = dataframe.index.values
        values = dataframe[category_name].values
        
        header = [None] + [{"string": str(name).replace("(", "").replace("]", "").replace(", ", "-")} for name in names]
        numbers = [{"string": display_name}] + [{"number": value} for value in values]
        
        chart = dict()
        chart["name"] = chart_name
        chart["table"] = [header, [], numbers]
        
        self.thinkcell_obj["data"].append(chart)
        
    def save_ppttc(self, filename):
        with open(filename, "w") as outfile:
            json.dump([self.thinkcell_obj], outfile)

