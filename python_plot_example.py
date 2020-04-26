import time
import numpy as np
import matplotlib.pyplot as plt
from Generic_Scatter_Plot_Class import *

x_column = [10,20,30,40,50]
a_column = [60,70,80,90,100]
b_column = [110,120,130,140,150]
c_column = [210,220,230,240,250]

###############################################################################################################################
def plot_standalone_graph(graph_name, subplot_name):
    generic_scatter_plot_obj = Graph_Window_Class.add_subplot(graph_name, subplot_name)

    Graph_Window_Class.graphs[graph_name][subplot_name].add_graph('One', colour='red', marker_radius=2, plot_label='Graph One')
    Graph_Window_Class.graphs[graph_name][subplot_name].add_graph('Two', colour='green', marker_radius=2, marker_shape="^", plot_label='Graph Two')
    Graph_Window_Class.graphs[graph_name][subplot_name].add_graph('Three', colour='blue', marker_radius=2, marker_shape="x", plot_label='Graph Three')

    Graph_Window_Class.graphs[graph_name][subplot_name].legend_margin = (1.4, 1)

    counter = 0
    while counter < len(x_column):
        Graph_Window_Class.graphs[graph_name][subplot_name].append_x_axis_val(x_column[counter])
        
        Graph_Window_Class.graphs[graph_name][subplot_name].append_y_val_to_graph('One', a_column[counter])
        Graph_Window_Class.graphs[graph_name][subplot_name].append_y_val_to_graph('Two', b_column[counter])    
        Graph_Window_Class.graphs[graph_name][subplot_name].append_y_val_to_graph('Three', c_column[counter])
        
        counter = counter + 1
    # End While

    Graph_Window_Class.render_subplots()
    Graph_Window_Class.graphs[graph_name][subplot_name].plot_graphs()
    
# End Function
###############################################################################################################################

plot_standalone_graph("One", ".1")
plot_standalone_graph("Two", ".2")
plot_standalone_graph("Three", ".3")
plot_standalone_graph("Four", ".4")

###############################################################################################################################

Graph_Window_Class.show_plots() 

###############################################################################################################################
