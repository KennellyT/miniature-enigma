import numpy as np
def them_k(temp,source):
    """Finds the thermal conductivity of a metal.

    Parameters
    ----------
    temp : int or str
        Temperature of metal
    source : str
        The metal to be studied
    Returns
    -------
    themal_conductivity : float
        thermal conductivity of metal at a certain temperature
    Notes
    ----
    If temperature no found in tables, program will conduct a linear extrapolation
    for the thermal conductivity.
    """

    srcmap = {'copper':'copper.csv' ,'silver': 'silver.csv', 'tungsten': 'tungsten.csv', 'iron': 'iron.csv'}
    if source in srcmap:
         source_name = srcmap[source]
         #filepath = 'Helium'
         with open(source_name, "r") as file:
             full_file_text = file.read()
         file_split = full_file_text.splitlines()
         file.close()
         dic = {}
         conds = []
         temps = []
         for item in file_split:
             tempv = item.split(",")[0]
             cond = item.split(",")[1]
             dic[tempv] = cond
             conds.append(cond)
             temps.append(tempv)
             #dic.append(vals)
         if str(temp) in dic:
             return int(dic[str(temp)])
         else:
             a=float(conds[1])
             b=float(conds[-1])
             c = float(temps[1])
             d = float(temp)
             e = float(temps[-1])
             x=-((((c-d)/(c-e))*(a-b))-a)
             print("Extrapolated:")
             return x
    else:
        raise ValueError('Material not documented')
    