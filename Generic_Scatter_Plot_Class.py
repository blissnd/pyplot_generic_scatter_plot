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
    
    def __init__(self, graph_name, plot_title="Scatter Plot"):
        
        self.plt = None
        
        self.graph_name = graph_name
        
        self.plot_title = plot_title
        self.x_axis_array = []
        self.graph_dict = {}
        self.legend_position = 'upper right'
        self.legend_margin = (1.2, 1)
        self.x_axis_label = 'Value'
        self.y_axis_label = 'Result'
        self.num_legend_columns = 1
    
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
    
    window_index = 0

    def __init__(self):
        
        Graph_Window_Class.window_index = Graph_Window_Class.window_index + 1
        
        self.sub_windows = {}
        
        self.fig = parent_plot.figure(Graph_Window_Class.window_index)
        
        self.gs = None        
    
    # End Function
    
    def add_subplot_to_window(self, graph_name, subplot_name):
    
        if graph_name not in self.sub_windows:
            self.sub_windows[graph_name] = {}
            self.sub_windows[graph_name]['subplots'] = {}
        # End If
        
        self.sub_windows[graph_name]['subplots'][subplot_name] = Generic_Scatter_Plot(graph_name, plot_title="Scatter Plot")
        
    # End Static Function
    
    def render_subplots(self):
    
        for graph_name, graph_object in self.sub_windows.items():
        
            num_subplots = len(graph_object['subplots'])
            num_rows_columns = math.ceil(math.sqrt(num_subplots))
            
            self.gs = self.fig.add_gridspec(num_rows_columns, num_rows_columns)
            
            row_index = 0
            col_index = 0
            
            for subplot_name, subplot_object in graph_object['subplots'].items():
            
                subplot_object.plt = self.fig.add_subplot(self.gs[row_index, col_index])
                
                col_index = col_index + 1
                
                if col_index == num_rows_columns:
                    col_index = 0
                    row_index = row_index + 1
                # End If
                
            # End For
            
        # End For
        
    # End Static Function
    
    def show_plots(self):
        parent_plot.show()
    # End Static Function
    
# End Class
