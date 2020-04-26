import numpy as np
import matplotlib.pyplot as parent_plot
import math

class Graph:

    def __init__(self, colour='black', marker_radius=1, marker_shape='.', plot_label=None):
        self.y_value_array = []
        self.colour = []
        self.marker_size = np.pi * marker_radius ** 2
        self.marker_shape = marker_shape
        
        self.colour.append(colour)
        self.plot_label = plot_label
    # End Function
    
    def append_y_axis_val(self, value):
        self.y_value_array.append(value)
    # End Function
    
# End Class

class Generic_Scatter_Plot:
    graph_index = 0
    
    def __init__(self, graph_name, plot_title="Scatter Plot"):
        self.graph_index = Generic_Scatter_Plot.graph_index
        self.graph_name = graph_name
        
        self.plot_title = plot_title
        self.x_axis_array = []
        self.graph_dict = {}
        self.legend_position = 'upper right'
        self.legend_margin = (1.2, 1)
        self.x_axis_label = 'Value'
        self.y_axis_label = 'Result'
        self.num_legend_columns = 1
        
        self.fig = parent_plot.figure(self.graph_index)
        
        self.subplot_index = 0
        
        self.gs = None
        self.plt = None
        
        Generic_Scatter_Plot.graph_index = Generic_Scatter_Plot.graph_index + 1
    # End Function
    
    def add_graph(self, graph_name, colour='black', marker_radius=1, marker_shape='.', plot_label=None):
        self.graph_dict[graph_name] = Graph(colour, marker_radius, marker_shape, plot_label)
    # End Function
    
    def append_x_axis_val(self, value):
        self.x_axis_array.append(value)
    # End Function
    
    def append_y_val_to_graph(self, graph_name, value):
        self.graph_dict[graph_name].append_y_axis_val(value)
    # End Function
    
    def plot_graphs(self):
        
        #self.plt.title(self.plot_title)
        
        self.plt.set(xlabel=self.x_axis_label, ylabel=self.y_axis_label)
        
        for current_graph in self.graph_dict:
        
            self.plt.scatter(self.x_axis_array, self.graph_dict[current_graph].y_value_array, s=self.graph_dict[current_graph].marker_size, c=self.graph_dict[current_graph].colour, marker=self.graph_dict[current_graph].marker_shape, label= self.graph_dict[current_graph].plot_label)
          
        # End For
        
        self.plt.grid(b=True, which='major', color='#444444', linestyle='-', alpha=0.2)
        self.plt.minorticks_on()
        self.plt.grid(b=True, which='minor', color='#AAAAAA', linestyle='-', alpha=0.2)

        self.plt.legend(loc=self.legend_position, bbox_to_anchor=self.legend_margin, fontsize='small', ncol=self.num_legend_columns)
        parent_plot.tight_layout()
        
    # End Function
    
# End Class

class Graph_Window_Class():
    
    graphs = {}
    
    def add_subplot(graph_name, subplot_name):
    
        if graph_name not in Graph_Window_Class.graphs:
             Graph_Window_Class.graphs[graph_name] = {}
        # End If
        
        Graph_Window_Class.graphs[graph_name][subplot_name] = Generic_Scatter_Plot(graph_name, plot_title="Scatter Plot")
        
        Graph_Window_Class.graphs[graph_name][subplot_name].gs = Graph_Window_Class.graphs[graph_name][subplot_name].fig.add_gridspec(1, 1)
        Graph_Window_Class.graphs[graph_name][subplot_name].plt = Graph_Window_Class.graphs[graph_name][subplot_name].fig.add_subplot(Graph_Window_Class.graphs[graph_name][subplot_name].gs[0, 0])
        
        #gs = self.fig.add_gridspec(2, 2)        
        #self.plt2 = self.fig.add_subplot(gs[1, 0])
        #self.plt3 = self.fig.add_subplot(gs[0, 1])
        #self.plt4 = self.fig.add_subplot(gs[1, 1])
        
    # End Static Function
    
    def render_subplots():
    
        for graph_name, graph_object in Graph_Window_Class.graphs.items():
            print(len(graph_object))
        # End For
        
    # End Static Function
    
    def show_plots():
        parent_plot.show()
    # End Static Function
    
# End Class
