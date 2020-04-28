import time
import numpy as np
import matplotlib.pyplot as plt
from Generic_Scatter_Plot_Class import *

x_column = [10,20,30,40,50]
a_column = [60,70,80,90,100]
b_column = [110,120,130,140,150]
c_column = [210,220,230,240,250]

###############################################################################################################################
def create_graph_window(graph_window_obj, window_name, subplot_name, render_subplots=False):
    
    graph_window_obj.add_subplot_to_window(window_name, subplot_name + '_1', 'Title_1', 'x_label_1', 'y_label_1')
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].add_graph('One', colour='red', marker_radius=2, plot_label='Graph One')
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].add_graph('One.1', colour='black', marker_radius=2, plot_label='Graph One')
    
    graph_window_obj.add_subplot_to_window(window_name, subplot_name + '_2')
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_2'].add_graph('Two', colour='green', marker_radius=2, marker_shape="^", plot_label='Graph Two')
    
    graph_window_obj.add_subplot_to_window(window_name, subplot_name + '_3')
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_3'].add_graph('Three', colour='blue', marker_radius=2, marker_shape="x", plot_label='Graph Three')
    
    graph_window_obj.add_subplot_to_window(window_name, subplot_name + '_4')
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_4'].add_graph('Four', colour='blue', marker_radius=2, marker_shape="x", plot_label='Graph Four')
    
    graph_window_obj.add_subplot_to_window(window_name, subplot_name + '_5')
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_5'].add_graph('Five', colour='blue', marker_radius=2, marker_shape="x", plot_label='Graph Five')

    for subplot_key, subplot_obj in graph_window_obj.sub_windows[window_name]['subplots'].items():
        subplot_obj.legend_margin = (1.8, 1)
    # End For

    counter = 0
    while counter < len(x_column):
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].append_x_axis_val(x_column[counter])
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_2'].append_x_axis_val(x_column[counter])
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_3'].append_x_axis_val(x_column[counter])
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_4'].append_x_axis_val(x_column[counter])
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_5'].append_x_axis_val(x_column[counter])
        
        counter = counter + 1
    # End While
    
    counter = 0
    while counter < len(x_column):       
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].append_y_val_to_graph('One', a_column[counter])
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].append_y_val_to_graph('One.1', b_column[counter])
        
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_2'].append_y_val_to_graph('Two', b_column[counter])
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_3'].append_y_val_to_graph('Three', c_column[counter])
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_4'].append_y_val_to_graph('Four', c_column[counter])
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_5'].append_y_val_to_graph('Five', c_column[counter])
        
        counter = counter + 1
    # End While
    
    graph_window_obj.render_subplots(render_subplots)
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].plot_graphs()
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_2'].plot_graphs()
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_3'].plot_graphs()
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_4'].plot_graphs()
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_5'].plot_graphs()
    
# End Function
###############################################################################################################################

graph_window_1_obj = Graph_Window_Class((11.5, 6))
create_graph_window(graph_window_1_obj, "One", "1", True)

graph_window_2_obj = Graph_Window_Class((11.5, 6))
create_graph_window(graph_window_2_obj, "Two", "2")

graph_window_3_obj = Graph_Window_Class((11.5, 6))
create_graph_window(graph_window_3_obj, "Three", "3", True)

graph_window_4_obj = Graph_Window_Class((11.5, 6))
create_graph_window(graph_window_4_obj, "Four", "4")

###############################################################################################################################

Graph_Window_Class.show_plots()
