import time
import numpy as np
import matplotlib.pyplot as plt
from Generic_Scatter_Plot_Class import *

x_column = [10,20,30,40,50]
a_column = [60,70,80,90,100]
b_column = [110,120,130,140,150]
c_column = [210,220,230,240,250]

generic_scatter_plot_obj = Generic_Scatter_Plot()

generic_scatter_plot_obj.add_graph('One', colour='red', marker_radius=2, plot_label='Graph One')
generic_scatter_plot_obj.add_graph('Two', colour='green', marker_radius=2, plot_label='Graph Two')
generic_scatter_plot_obj.add_graph('Three', colour='blue', marker_radius=2, plot_label='Graph Three')

generic_scatter_plot_obj.legend_margin = (1.3, 1)

counter = 0
while counter < len(x_column):
    generic_scatter_plot_obj.append_x_axis_val(x_column[counter])
    
    generic_scatter_plot_obj.append_y_val_to_graph('One', a_column[counter])
    generic_scatter_plot_obj.append_y_val_to_graph('Two', b_column[counter])    
    generic_scatter_plot_obj.append_y_val_to_graph('Three', c_column[counter])
    
    counter = counter + 1
# End While

generic_scatter_plot_obj.plot_graphs()
