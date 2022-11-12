"""
Project for Week 4 of "Python Data Visualization".
Unify data via common country codes.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Nested list consisting of the fields in the CSV file
    """
    table = {}
    with open(filename, "rt", newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=separator, quotechar=quote)
        for row in csv_reader:
            table[row[keyfield]] = row
    return table


def build_country_code_converter(codeinfo):
    """
    Inputs:
      codeinfo      - A country code information dictionary

    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """
    dat = read_csv_as_nested_dict(codeinfo['codefile'], codeinfo['plot_codes'], codeinfo['separator'],
                                  codeinfo['quote'])

    table = {}

    for dit in dat:
        table[dit] = dat[dit][codeinfo['data_codes']]
        # print(dat[dit]['Code2'])
    return table


def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country codes used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country codes from
      gdp_countries.  The set contains the country codes from
      plot_countries that did not have a country with a corresponding
      code in gdp_countries.

      Note that all codes should be compared in a case-insensitive
      way.  However, the returned dictionary and set should include
      the codes with the exact same case as they have in
      plot_countries and gdp_countries.
    """
    table = {}

    no_appear = set()

    # for key in plot_countries:
    #     table[key] = None

    for key, val in plot_countries.items():

        for key2, val2 in gdp_countries.items():

            if val == val2['Country Name']:
                table[key] = val2['Country Code']

    if len(plot_countries) == len(table):
        no_appear = set()
    else:
        for key in plot_countries:
            if not key in table:
                no_appear.add(key)
    return table, no_appear

def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year for which to create GDP mapping

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    gdpdat = read_csv_as_nested_dict(gdpinfo['gdpfile'], year, gdpinfo['separator'],
                                     gdpinfo['quote'])

    codedat = build_country_code_converter(codeinfo)

    # print('codedat is ',codedat)
    table = {}
    no_gdp = set()
    no_appear = set()
    v2 = {v: k for k, v in plot_countries.items()}

    for key, val in codedat.items():
        for key2, val2 in gdpdat.items():
            if val.lower() == gdpdat[key2]['Code'].lower():
                try:
                    table[v2[key]] = math.log(float(key2), 10)
                    del v2[key]
                except ValueError:
                    if key in v2:
                        no_gdp.add(v2[key])
                        del v2[key]
                    else:
                        pass
    no_appear = set(v2.values())
    return table, no_appear, no_gdp
# def render_world_map(gdpinfo, codeinfo, plot_countries, year, map_file):
#     """
#     Inputs:
#       gdpinfo        - A GDP information dictionary
#       codeinfo       - A country code information dictionary
#       plot_countries - Dictionary mapping plot library country codes to country names
#       year           - String year of data
#       map_file       - String that is the output map file name
#
#     Output:
#       Returns None.
#
#     Action:
#       Creates a world map plot of the GDP data in gdp_mapping and outputs
#       it to a file named by svg_filename.
#     """
#     worldmap_chart = pygal.maps.world.World()
#     worldmap_chart.title = 'GDP by country for ' + year + ' (log scale), unified by common' + \
#                            ' country Code'
#
#     gdp_datas = build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year)
#
#     worldmap_chart.add('GDP For ' + year, gdp_datas[0])
#     worldmap_chart.add('Missing from World Bank Data', gdp_datas[1])
#     worldmap_chart.add('No GDP Data', gdp_datas[2])
#
#     worldmap_chart.render_to_file(map_file)
#
#
# def test_render_world_map():
#     """
#     Test the project code for several years
#     """
#     gdpinfo = {
#         "gdpfile": "isp_gdp.csv",
#         "separator": ",",
#         "quote": '"',
#         "min_year": 1960,
#         "max_year": 2015,
#         "country_name": "Country Name",
#         "country_code": "Country Code"
#     }
#
#     codeinfo = {
#         "codefile": "isp_country_codes.csv",
#         "separator": ",",
#         "quote": '"',
#         "plot_codes": "ISO3166-1-Alpha-2",
#         "data_codes": "ISO3166-1-Alpha-3"
#     }
#
#     # Get pygal country code map
#     pygal_countries = pygal.maps.world.COUNTRIES
#
#     # 1960
#     render_world_map(gdpinfo, codeinfo, pygal_countries, "1960", "isp_gdp_world_code_1960.svg")
#
#     # 1980
#     render_world_map(gdpinfo, codeinfo, pygal_countries, "1980", "isp_gdp_world_code_1980.svg")
#
#     # 2000
#     render_world_map(gdpinfo, codeinfo, pygal_countries, "2000", "isp_gdp_world_code_2000.svg")
#
#     # 2010
#     render_world_map(gdpinfo, codeinfo, pygal_countries, "2010", "isp_gdp_world_code_2010.svg")
#
#
# # Make sure the following call to test_render_world_map is commented
# # out when submitting to OwlTest/CourseraTest.
#
# test_render_world_map()