import time
import numpy as np
import matplotlib.pyplot as plt
from Generic_Scatter_Plot_Class import *

x_column = [0.98,1.34,-0.34,-1.45,0.0456]
a_column = [0.14,1.55,-1.05,1.01,-0.4754]
b_column = [1.43,1.11,2.4,-0.432,-1.22]
c_column = [-2.31,1.44,2.1076,-0.0012,-1.972]

###############################################################################################################################
def create_single_graph_window(graph_window_obj, window_name, subplot_name, render_subplots=False):
    
    graph_window_obj.add_subplot_to_window(window_name, subplot_name + '_1', 'Title_1', 'x_label_1', 'y_label_1', (1.2, 1))
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].add_graph('One', colour='red', marker_radius=2, plot_label='Graph One')
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].add_graph('One.1', colour='black', marker_radius=2, marker_shape="o", plot_label='Graph Two')
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].add_graph('One.2', colour='green', marker_radius=2, marker_shape="x", plot_label='Graph Three')
    
    counter = 0
    while counter < len(x_column):
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].append_x_axis_val(x_column[counter])               
        counter = counter + 1
    # End While
    
    counter = 0
    while counter < len(x_column):       
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].append_y_val_to_graph('One', a_column[counter])
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].append_y_val_to_graph('One.1', b_column[counter])
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].append_y_val_to_graph('One.2', c_column[counter])           
        
        counter = counter + 1
    # End While
    
    graph_window_obj.render_subplots(render_subplots)
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].plot_graphs()    
# End Function
###############################################################################################################################
def create_multi_graph_window(graph_window_obj, window_name, subplot_name, render_subplots=False):
    
    graph_window_obj.add_subplot_to_window(window_name, subplot_name + '_1', 'Title_1', 'x_label_1', 'y_label_1', (1.8, 1))
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].add_graph('One', colour='red', marker_radius=2, plot_label='Graph One')
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].add_graph('One.1', colour='black', marker_radius=2, plot_label='Graph Two')
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].add_graph('One.2', colour='green', marker_radius=2, marker_shape="x", plot_label='Graph Three')
    
    graph_window_obj.add_subplot_to_window(window_name, subplot_name + '_2', 'Title_2', 'x_label_2', 'y_label_2', (1.8, 1))
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_2'].add_graph('Two', colour='green', marker_radius=2, marker_shape="^", plot_label='Graph Two')
    
    graph_window_obj.add_subplot_to_window(window_name, subplot_name + '_3', 'Title_3', 'x_label_3', 'y_label_3', (1.8, 1))
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_3'].add_graph('Three', colour='blue', marker_radius=2, marker_shape="x", plot_label='Graph Three')
    
    graph_window_obj.add_subplot_to_window(window_name, subplot_name + '_4', 'Title_4', 'x_label_4', 'y_label_4', (1.8, 1))
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_4'].add_graph('Four', colour='blue', marker_radius=2, marker_shape="x", plot_label='Graph One')
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_4'].add_graph('Four.1', colour='red', marker_radius=2, marker_shape="o", plot_label='Graph Two')
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_4'].add_graph('Four.2', colour='yellow', marker_radius=2, marker_shape="^", plot_label='Graph Three')
    
    graph_window_obj.add_subplot_to_window(window_name, subplot_name + '_5', 'Title_5', 'x_label_5', 'y_label_5', (1.8, 1))
    graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_5'].add_graph('Five', colour='blue', marker_radius=2, marker_shape="x", plot_label='Graph Five') 

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
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_1'].append_y_val_to_graph('One.2', c_column[counter])
        
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_2'].append_y_val_to_graph('Two', b_column[counter])
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_3'].append_y_val_to_graph('Three', c_column[counter])
        
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_4'].append_y_val_to_graph('Four', c_column[counter])
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_4'].append_y_val_to_graph('Four.1', b_column[counter])
        graph_window_obj.sub_windows[window_name]['subplots'][subplot_name + '_4'].append_y_val_to_graph('Four.2', a_column[counter])
        
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
graph_window_obj = Graph_Window_Class((11.5, 6))
create_single_graph_window(graph_window_obj, "One", "1", True)
###############################################################################################################################
graph_window_1_obj = Graph_Window_Class((11.5, 6))
create_multi_graph_window(graph_window_1_obj, "One", "1", True)

graph_window_2_obj = Graph_Window_Class((11.5, 6))
create_multi_graph_window(graph_window_2_obj, "Two", "2")

graph_window_3_obj = Graph_Window_Class((11.5, 6))
create_multi_graph_window(graph_window_3_obj, "Three", "3", True)

graph_window_4_obj = Graph_Window_Class((11.5, 6))
create_multi_graph_window(graph_window_4_obj, "Four", "4")
###############################################################################################################################
Graph_Window_Class.show_plots()
