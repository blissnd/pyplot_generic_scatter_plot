import numpy as np
import matplotlib.pyplot as plt

class Graph:

    def __init__(self, colour='black', marker_radius=1, plot_label=None):
        self.y_value_array = []
        self.colour = []
        self.marker_size = np.pi * marker_radius ** 2
        
        self.colour.append(colour)
        self.plot_label = plot_label
    # End Function
    
    def append_y_axis_val(self, value):
        self.y_value_array.append(value)
    # End Function
    
# End Class

class Generic_Scatter_Plot:

    def __init__(self, plot_title="Scatter Plot"):
        self.plot_title = plot_title
        self.x_axis_array = []
        self.graph_dict = {}
        self.legend_position = 'upper right'
        self.legend_margin = (1.2, 1)
        self.x_axis_label = 'Value'
        self.y_axis_label = 'Result'
        self.num_legend_columns = 1
         
        self.fig = plt.figure(figsize=(8,6))
        self.ax = self.fig.add_subplot(1, 1, 1)
    # End Function
    
    def add_graph(self, graph_name, colour='black', marker_radius=1, plot_label=None):
        self.graph_dict[graph_name] = Graph(colour, marker_radius, plot_label)
    # End Function
    
    def append_x_axis_val(self, value):
        self.x_axis_array.append(value)
    # End Function
    
    def append_y_val_to_graph(self, graph_name, value):
        self.graph_dict[graph_name].append_y_axis_val(value)
    # End Function
    
    def plot_graphs(self):
        
        plt.title(self.plot_title)
        plt.xlabel(self.x_axis_label)
        plt.ylabel(self.y_axis_label)

        for current_graph in self.graph_dict:
        
            plt.scatter(self.x_axis_array, self.graph_dict[current_graph].y_value_array, s=self.graph_dict[current_graph].marker_size, c= self.graph_dict[current_graph].colour, label= self.graph_dict[current_graph].plot_label)
          
        # End For
        
        plt.legend(loc=self.legend_position, bbox_to_anchor=self.legend_margin, fontsize='small', ncol=self.num_legend_columns)
        plt.tight_layout()
        plt.show()
        
    # End Function
    
# End Class