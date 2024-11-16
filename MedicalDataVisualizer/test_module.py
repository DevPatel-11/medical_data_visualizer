# Import necessary libraries
import unittest  # To define and run the test cases
import medical_data_visualizer  # Custom module containing visualization functions
import matplotlib as mpl  # For working with matplotlib objects like axes and rectangles

# Test case for the categorical plot
class CatPlotTestCase(unittest.TestCase):
    def setUp(self):
        """
        Setup method that runs before each test in this class.
        It generates the categorical plot and accesses the first set of axes.
        """
        self.fig = medical_data_visualizer.draw_cat_plot()  # Generate the categorical plot
        self.ax = self.fig.axes[0]  # Access the first axes in the figure
    
    def test_line_plot_labels(self):
        """
        Test to check the correctness of x-axis and y-axis labels in the categorical plot.
        """
        # Check the x-axis label
        actual = self.ax.get_xlabel()
        expected = "variable"
        self.assertEqual(actual, expected, "Expected line plot xlabel to be 'variable'")
        
        # Check the y-axis label
        actual = self.ax.get_ylabel()
        expected = "total"
        self.assertEqual(actual, expected, "Expected line plot ylabel to be 'total'")
        
        # Check the secondary x-axis labels
        actual = []
        for label in self.ax.get_xaxis().get_majorticklabels():
            actual.append(label.get_text())
        expected = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
        self.assertEqual(actual, expected, "Expected bar plot secondary x labels to be 'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'")

    def test_bar_plot_number_of_bars(self):
        """
        Test to check the number of bars in the categorical plot.
        """
        # Count the number of rectangles (bars) in the plot
        actual = len([rect for rect in self.ax.get_children() if isinstance(rect, mpl.patches.Rectangle)])
        expected = 13
        self.assertEqual(actual, expected, "Expected a different number of bars chart.")
# Test case for the heatmap
class HeatMapTestCase(unittest.TestCase):
    def setUp(self):
        """
        Setup method that runs before each test in this class.
        It generates the heatmap and accesses the first set of axes.
        """
        self.fig = medical_data_visualizer.draw_heat_map()  # Generate the heatmap
        self.ax = self.fig.axes[0]  # Access the first axes in the figure

    def test_heat_map_labels(self):
        """
        Test to check the correctness of x-axis labels in the heatmap.
        """
        # Extract the x-axis labels
        actual = []
        for label in self.ax.get_xticklabels():
            actual.append(label.get_text())
        expected = ['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']
        self.assertEqual(actual, expected, "Expected heat map labels to be 'id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight'.")
    
    def test_heat_map_values(self):
        """
        Test to verify the values displayed on the heatmap.
        """
        # Extract the text values displayed on the heatmap
        actual = [text.get_text() for text in self.ax.get_default_bbox_extra_artists() if isinstance(text, mpl.text.Text)]
        print(actual)  # Print actual values for debugging purposes
        # Expected values for the heatmap
        expected = ['0.0', '0.0', '-0.0', '0.0', '-0.1', '0.5', '0.0', '0.1', '0.1', '0.3', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.2', '0.1', '0.0', '0.2', '0.1', '0.0', '0.1', '-0.0', '-0.1', '0.1', '0.0', '0.2', '0.0', '0.1', '-0.0', '-0.0', '0.1', '0.0', '0.1', '0.4', '-0.0', '-0.0', '0.3', '0.2', '0.1', '-0.0', '0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.2', '0.1', '0.1', '0.0', '0.0', '0.0', '0.0', '0.3', '0.0', '-0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.0', '0.0', '-0.0', '0.0', '0.0', '0.0', '0.2', '0.0', '-0.0', '0.2', '0.1', '0.3', '0.2', '0.1', '-0.0', '-0.0', '-0.0', '-0.0', '0.1', '-0.1', '-0.1', '0.7', '0.0', '0.2', '0.1', '0.1', '-0.0', '0.0', '-0.0', '0.1']
        self.assertEqual(actual, expected, "Expected different values in heat map.")
# Run the tests
if __name__ == "__main__":
    # Use unittest to automatically discover and run all test cases
    unittest.main()
