import json
import warnings
from datetime import datetime
from pprint import pprint


class DataFrameError(Exception):
    pass


class Thinkcell(object):
    """The Thinkcell object base class. 

    Attributes
    ----------
    charts : list
        A list of that contains a dictionnary for every template added. That dictionnary 
        contains two objects, `template` and `data`.
        The `data` object contains itself two keys: `name` (the name of the chart) and 
        `table` (the actual data). 
    """

    def __init__(self):
        """Initializes the Thinkcell object. Takes no arguments.
        """
        self.charts = []

    def __str__(self):
        """Prints the data inside of the Thinkcell object.
        """
        return str(self.charts)

    @staticmethod
    def verify_template(template_name):
        """Function that verifies the validity of a template.

        Parameters
        ----------
        template_name : str
            The name of the template file to be added. 

        Returns
        -------
        template_name: str
            Returns the name of the template if exceptions are not raised.

        Raises
        ------
        TypeError
            Raises if template name is not a string or does not end in ".pptx".
        """
        if not isinstance(template_name, str):
            raise TypeError(f"'{template_name}' is not a valid template file.")

        if not template_name.endswith(".pptx"):
            raise TypeError(
                f"'{template_name}' is not a valid Powerpoint file."
            )

        else:
            return template_name

    @staticmethod
    def transform_input(data_element):
        """Transforms a `data element` into an object like {"type": data element}.

        Parameters
        ----------
        data_element : str, int, float, datetime
            A data element can be a string, int, float or datetime. 

        Returns
        -------
        dict
            Returns an object of type {"type": input}

        Raises
        ------
        ValueError
            Raises if object is not of type int, float, str, or datetime. 

        Examples
        --------
        For a float or int, the dict will have "number" as key. 

        >>> print(Thinkcell.transform_input(5))
        {"number": 5}

        For a str input, the dict will have a "string" as key.

        >>> print(Thinkcell.transform_input("test"))
        {"string": "test"}
        """

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
        """Adds a template to the Thinkcell object.

        Parameters
        ----------
        template_name : str
            The name of the template to be added. 
        """
        self.verify_template(template_name)
        self.charts.append({"template": template_name, "data": []})

    def add_chart(self, template_name, chart_name, categories, data):
        """Adds a chart to the template object. 

        Parameters
        ----------
        template_name : str
            The name of the template where the chart will be added
        chart_name : str
            The name of the chart in the specified template
        categories : list
            A list containing the header of the chart. Headers can 
            be categories, years, companies, etc.
        data : list
            A list of lists. Each list contains the row of data to be added. Be
            aware that the first element of each of these lists should be a 
            category as well.

        Raises
        ------
        ValueError
            If template does not exist, if the length of the categories does not
            make sense reltively to the header data. 
        """
        available_templates = [page["template"] for page in self.charts]

        if template_name not in available_templates:
            raise ValueError(
                f"{template_name} does not exist, please create one first."
            )

        if not isinstance(chart_name, str):
            warnings.warn(
                f"Your chart name is not a string, we will convert it into one. But wanted to make sure you were aware.",
                UserWarning,
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
        if self.charts[-1]["template"] == template_name:
            self.charts[-1]["data"].append(chart_dict)

    def add_chart_from_dataframe(self, template_name, chart_name, dataframe):
        """Adds a chart based on a dataframe to the template object. 

        Parameters
        ----------
        template_name : str
            The name of the template where the chart will be added
        chart_name : str
            The name of the chart in the specified template
        dataframe : pandas.DataFrame
            A dictionary of Pandas dataframes

        Raises
        ------
        DataFrameError
            If an invalid or empty DataFrame is passed
        """
        try:
            categories = dataframe.columns.to_list()[1:]
            assert isinstance(categories, list)
            data = dataframe.values.tolist()
            assert isinstance(data, list)
        except (AttributeError, AssertionError):
            raise DataFrameError("You did not pass a valid Pandas DataFrame")

        try:
            assert len(categories) > 1
            assert len(data)
        except AssertionError:
            raise DataFrameError(
                "The DataFrame you passed does not contain data"
            )

        self.add_chart(template_name, chart_name, categories, data)

    def add_textfield(self, template_name, field_name, text):
        """Adds a text field to the template object.

        Parameters
        ----------
        template_name : str
            The name of the template where the text field will be added
        field_name : str
            The name of the text field in the specified template
        text : str
            A string containing the text

        Raises
        ------
        ValueError
            If template does not exist
        """
        available_templates = [page["template"] for page in self.charts]

        if template_name not in available_templates:
            raise ValueError(
                f"{template_name} does not exist, please create one first."
            )

        if not isinstance(field_name, str):
            warnings.warn(
                f"Your field name is not a string, we will convert it into one. But wanted to make sure you were aware.",
                UserWarning,
            )

        field_dict = {}
        field_dict["name"] = str(field_name)
        field_text = [self.transform_input(text)]
        field_dict["table"] = [field_text]

        if self.charts[-1]["template"] == template_name:
            self.charts[-1]["data"].append(field_dict)

    def save_ppttc(self, filename):
        """Saves the Thinkcell object as a `.ppttc` file.

        Parameters
        ----------
        filename : str
            The name of the file to be saved.

        Raises
        ------
        ValueError
            If the filename specified is not a string or does 
            not end in `.ppttc`.
        """
        if not isinstance(filename, str):
            raise ValueError(f"A filename is normally a string, yours is not.")

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
