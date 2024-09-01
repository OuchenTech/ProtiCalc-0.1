from kivymd.uix.boxlayout import MDBoxLayout
from Bio.SeqUtils import seq3
from app.components.kivychart.barchart import BarChart
from app.customwidgets.customlayouts.customlayouts import GradientSeparator
from app.customwidgets.customlabels.customlabels import CustomRegularLabel

class ProteinAnalysisResult(MDBoxLayout):
    """
    The `ProteinAnalysisResult` class is responsible for displaying the results of the protein analysis.
    It updates different sections of the UI with the analyzed data such as amino acid counts, 
    physico-chemical parameters, secondary structure, molecular descriptors, and atomic composition.
    """
    
    def __init__(self, **kwargs):
        """
        Initializes the `ProteinAnalysisResult` class.
        
        Args:
            **kwargs: Additional keyword arguments passed to the MDBoxLayout class.
        """
        super(ProteinAnalysisResult, self).__init__(**kwargs)
        
    def update_results(self, results):
        """
        Updates all sections of the UI with the provided analysis results.
        
        Args:
            results (dict): A dictionary containing the computed analysis results.
        """
        self.update_amino_acids_count(results)
        self.update_physico_chemical_params(results)
        self.update_secondary_structure(results)
        self.update_molecular_descriptors(results)
        self.update_atomic_composition(results)

    def update_amino_acids_count(self, results):
        """
        Updates the UI section displaying the amino acid counts using the custom bar chart.
        
        Args:
            results (dict): A dictionary containing the computed analysis results.
        """
        aa_count = {seq3(k): v for k, v in results['amino_acids_count'].items() if v != 0}
        chart = BarChart(
            data=aa_count,
            title="Amino Acids Count",
            size_hint=(1, 1),
            label_color='gray',
            label_font_name='assets/fonts/Poppins-Regular.ttf',
            grid=True, 
            gradient_colors=['#25aae1','#eb72ac'], 
            bar_radius=12,
            color_style='gradient',
            x_axis_label_rotation='left-down'
        )
        self.ids.bar_chart_section.clear_widgets()
        self.ids.bar_chart_section.add_widget(chart)
        
    def update_atomic_composition(self, results):
        """
        Updates the UI section displaying the atomic composition of the protein.
        
        Args:
            results (dict): A dictionary containing the computed atomic composition.
        """
        atom_full_names = {
            'C': 'Carbon',
            'H': 'Hydrogen',
            'O': 'Oxygen',
            'N': 'Nitrogen',
            'S': 'Sulfur'
        }
        protein_atomic_composition = {atom_full_names.get(k, k): v for k, v in results['atom_composition'].items()}
        self.update_boxlayout_with_params(self.ids.atomic_composition, protein_atomic_composition)
            
    def update_physico_chemical_params(self, results):
        """
        Updates the UI section displaying the physico-chemical parameters.
        
        Args:
            results (dict): A dictionary containing the computed analysis results.
        """
        params_dict = {
            "Protein Length (aa)": results['protein_length'],
            "Molecular Weight (KDa)": results['molecular_weight'],
            "Isoelectric Point": results['isoelectric_point'],
            "Charge at pH=7": results['charge'],
            "Aromaticity": results['aromaticity'],
            "Aliphatic Index": results['aliphatic_index'],
            "Instability Index": results['instability_index'],
            "Boman Index": results['boman_index'],
            "Gravy": results['gravy']
        }
        self.update_boxlayout_with_params(self.ids.phy_che_params, params_dict)

    def update_secondary_structure(self, results):
        """
        Updates the UI section displaying the secondary structure percentages.
        
        Args:
            results (dict): A dictionary containing the computed analysis results.
        """
        structure_dict = {
            "Helix": results['helix'],
            "Turn": results['turn'],
            "Sheet": results['sheet'],
        }
        self.update_boxlayout_with_params(self.ids.secondary_structure, structure_dict)

    def update_molecular_descriptors(self, results):
        """
        Updates the UI section displaying the molecular descriptors.
        
        Args:
            results (dict): A dictionary containing the computed analysis results.
        """
        # Round descriptor values to 4 decimal places
        rounded_descriptors = {k: round(v, 4) for k, v in results['descriptors'].items()}
        self.update_boxlayout_with_params(self.ids.molecular_descriptors, rounded_descriptors)

    def update_boxlayout_with_params(self, boxlayout, params_dict):
        """
        Updates the given BoxLayout with widgets based on key-value pairs in the provided dictionary.

        This method clears all existing widgets in the BoxLayout and adds a series of new widgets 
        based on the key-value pairs from `params_dict`. Each key-value pair is displayed as a row 
        in the BoxLayout, with the key on the left and the value on the right. A separator is added 
        between each row, except after the last one.

        Args:
            boxlayout (BoxLayout): The BoxLayout to update with new widgets.
            params_dict (dict): A dictionary containing key-value pairs to be displayed in the layout.
        """
        boxlayout.clear_widgets()
        total_items = len(params_dict)
        for index, (k, v) in enumerate(params_dict.items(), start=1):
            boxlayout.add_widget(
                MDBoxLayout(
                    CustomRegularLabel(text=f"{k}", halign='left'),
                    CustomRegularLabel(text=f"{v}", halign='right'),
                    size_hint=(1, None),
                    height='50dp',
                )
            )
            if index < total_items:
                boxlayout.add_widget(GradientSeparator())
                