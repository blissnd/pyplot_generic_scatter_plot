import time
import numpy as np
import matplotlib.pyplot as plt
from Generic_Scatter_Plot_Class import *

x_column = [10,20,30,40,50]
a_column = [60,70,80,90,100]
b_column = [110,120,130,140,150]
c_column = [210,220,230,240,250]

###############################################################################################################################
def plot_standalone_graph(graph_window_1_obj, window_name, subplot_name):
    
    graph_window_1_obj.add_subplot_to_window(window_name, subplot_name + '_1')
    graph_window_1_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].add_graph('One', colour='red', marker_radius=2, plot_label='Graph One')
    
    graph_window_1_obj.add_subplot_to_window(window_name, subplot_name + '_2')
    graph_window_1_obj.sub_windows[window_name]['subplots'][subplot_name + '_2'].add_graph('Two', colour='green', marker_radius=2, marker_shape="^", plot_label='Graph Two')
    
    graph_window_1_obj.add_subplot_to_window(window_name, subplot_name + '_3')
    graph_window_1_obj.sub_windows[window_name]['subplots'][subplot_name + '_3'].add_graph('Three', colour='blue', marker_radius=2, marker_shape="x", plot_label='Graph Three')

    graph_window_1_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].legend_margin = (1.4, 1)

    counter = 0
    while counter < len(x_column):
        graph_window_1_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].append_x_axis_val(x_column[counter])
        graph_window_1_obj.sub_windows[window_name]['subplots'][subplot_name + '_2'].append_x_axis_val(x_column[counter])
        graph_window_1_obj.sub_windows[window_name]['subplots'][subplot_name + '_3'].append_x_axis_val(x_column[counter])
        
        graph_window_1_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].append_y_val_to_graph('One', a_column[counter])
        graph_window_1_obj.sub_windows[window_name]['subplots'][subplot_name + '_2'].append_y_val_to_graph('Two', b_column[counter])    
        graph_window_1_obj.sub_windows[window_name]['subplots'][subplot_name + '_3'].append_y_val_to_graph('Three', c_column[counter])
        
        counter = counter + 1
    # End While

    graph_window_1_obj.render_subplots()
    graph_window_1_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].plot_graphs()
    graph_window_1_obj.sub_windows[window_name]['subplots'][subplot_name + '_2'].plot_graphs()
    
# End Function
###############################################################################################################################

graph_window_1_obj = Graph_Window_Class()

plot_standalone_graph(graph_window_1_obj, "One", ".1")
#plot_standalone_graph(graph_window_1_obj, "Two", ".2")
#plot_standalone_graph(graph_window_1_obj, "Three", ".3")
#plot_standalone_graph(graph_window_1_obj, "Four", ".4")

###############################################################################################################################

graph_window_1_obj.show_plots()
