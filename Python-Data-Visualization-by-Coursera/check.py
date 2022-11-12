import pygal

# pygal.Bar()(1,3,3,7)(1,6,6,4).render_to_file("pygal_test.svg")

pygal.Bar()(1,3,3,7)(1,6,6,4).render_in_browser()

# from xml.dom import minidom
#
#
# def get_county_attributes(svg_file_name):
#     """
#     Given SVG file associate with string svg_file_name, extract county attributes from associated XML
#     Return a list of tuples consisting of FIPS codes (strings) and county boundaries (strings)
#     """
#
#     svg_doc = minidom.parse(svg_file_name)
#     county_attribute_list = []
#     for path in svg_doc.getElementsByTagName('path'):
#         FIPS_code = path.getAttribute('id')
#         county_boundary_data = path.getAttribute('d')
#         county_attribute_list.append((FIPS_code, county_boundary_data))
#     svg_doc.unlink()
#     return county_attribute_list
#
#
# def get_boundary_coordinates(boundary_data):
#     boundary_data = boundary_data.replace('z','')
#     boundary_data = boundary_data.replace('M','L')
#     boundary_list = boundary_data.split('L')[1:]
#
#     boundary_coordinates = []
#     for entry in boundary_list:
#         temp = entry.split(',')
#         if len(temp) == 2:
#             (xcoord, ycoord) = temp
#         else:
#             print(len(temp))
#             print(temp)
#         boundary_coordinates.append((float(xcoord),float(ycoord)))
#     return boundary_coordinates
#
# # test_get_attributes("USA_Counties_2014.svg")
# x = get_county_attributes("USA_Counties_2014.svg")
# print(get_boundary_coordinates(x))
# #
# # svg_doc = minidom.parse("USA_Counties_2014.svg")
# # print(svg_doc)