import os
import numpy as np
import pandas as pd

from jinja2 import Environment, FileSystemLoader

template_name = "PrecipFile_Template"
out_path = r"C:\Users\hatch\Desktop\python\C2VSimFG_Precip.dat"
project_name = "Fine-Grid California Central Valley Groundwater-Surface Water Simulation Model (C2VSimFG)"
file_name = os.path.basename(out_path)
conversion_factor = 1 / 12
n_ts_update = 1
ts_frequency = 0
dss_file = ""
# dss_file = "precip.dss"

# get sample data
# data = [
#    "/SAMPLE_PROBLEM/GAGE1/PRECIP//1MON/PRECIPITATION/",
#    "/SAMPLE_PROBLEM/GAGE2/PRECIP//1MON/PRECIPITATION/",
# ]
values = np.random.random((1000, 2)) * 100
columns = np.arange(1, 1001)
data_df = pd.DataFrame({k: v for k, v in zip(columns, values)})
data_df["Date"] = ["09/30/2011_24:00", "10/31/2011_24:00"]
n_rain = len(data_df.columns) - 1
# n_rain = len(data)
data = (
    data_df[["Date"] + [col for col in data_df.columns if col != "Date"]]
    .to_numpy()
    .tolist()
)


env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template(template_name)

# render the template with the data
rendered_text = template.render(
    project_name=project_name,
    file_name=file_name,
    n_rain=n_rain,
    conversion_factor=conversion_factor,
    n_ts_update=n_ts_update,
    ts_frequency=ts_frequency,
    dss_file=dss_file,
    data=data,
)

with open(out_path, "w") as output_file:
    output_file.write(rendered_text)

print(f"Template rendered and saved to '{out_path}'.")
