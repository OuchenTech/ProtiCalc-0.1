from kivy.uix.screenmanager import Screen
from kivy.factory import Factory
import threading
from kivy.clock import Clock
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import peptides
from app.components.constants import atomic_composition
from app.components.proteinanalysis.proteinanalysis import ProteinAnalysisResult
from app.customwidgets.custombuttons.custombuttons import GradientButton
from app.customwidgets.customlayouts.customlayouts import CustomFloatLayout

class ProteinScreen(Screen):
    """
    The `ProteinScreen` class is responsible for managing the UI and logic related to protein analysis.
    It handles the input of protein sequences, initiates the analysis process, and updates the UI with the results.
    """
    def __init__(self, **kwargs):
        """
        Initializes the `ProteinScreen` class.
        
        Sets up the atomic composition data needed for the protein analysis.
        
        Args:
            **kwargs: Additional keyword arguments passed to the Screen class.
        """
        super(ProteinScreen, self).__init__(**kwargs)
        self.aa_atomic_composition = atomic_composition
        
    def on_leave(self):
        """
        Clears the text input and analysis results when leaving the screen.
        """
        self.reset()
        
    def reset(self):
        """
        Clears the text input and analysis results.
        """
        self.ids.protein_seq_input.text = ''
        self.ids.protein_analysis_result.clear_widgets()

    def show_error_popup(self, error):
        """
        Displays an error popup with the provided error message.
        
        Args:
            error (str): The error message to be displayed.
        """
        model_inst = Factory.ErrorPopup()
        error_label = model_inst.ids.error_label
        error_label.text = error
        model_inst.open()

    def compute_protein_params(self):
        """
        Initiates the computation of protein parameters based on the input sequence.
        
        If no sequence is entered, an error popup is shown. Otherwise, 
        it starts the analysis process on a separate thread.
        """
        protein_seq = self.ids.protein_seq_input.text
        self.ids.protein_analysis_result.clear_widgets()  # Clear existing widgets before computation
        if not protein_seq:
            self.show_error_popup("Please enter a protein sequence.")
        else:
            Clock.schedule_once(lambda dt: self.start_analysis(protein_seq), 0)

    def start_analysis(self, protein_seq):
        """
        Starts the analysis process by disabling inputs and running the analysis on a separate thread.
        
        Args:
            protein_seq (str): The protein sequence to be analyzed.
        """
        self.disable_inputs()  # Disable inputs before starting the thread
        threading.Thread(target=self.analyze_protein_thread, args=(protein_seq,)).start()

    def analyze_protein_thread(self, protein_seq):
        """
        Runs the protein analysis in a separate thread and handles any errors encountered.
        
        This method performs the heavy computations and schedules UI updates on the main thread.
        
        Args:
            protein_seq (str): The protein sequence to be analyzed.
        """
        try:
            seq = protein_seq.upper()
            # Perform the heavy computation
            results = self.calculate_protein_params(seq)
            # Schedule the UI update back on the main thread
            Clock.schedule_once(lambda dt: self.update_ui(results), 0)
        except ValueError as ve:
            err = str(ve)
            Clock.schedule_once(lambda dt: self.show_error_popup(err), 0)
        except KeyError as ke:
            err = str(ke)
            Clock.schedule_once(lambda dt: self.show_error_popup(f"{err} is not a valid unambiguous letter for protein"), 0)
        finally:
            # Re-enable inputs after all is done
            Clock.schedule_once(lambda dt: self.enable_inputs(), 0)

    def calculate_protein_params(self, seq):
        """
        Performs the actual computation of protein parameters.
        
        This method calculates various properties such as amino acid counts, 
        molecular weight, isoelectric point, and atomic composition.
        
        Args:
            seq (str): The protein sequence to be analyzed.
        
        Returns:
            dict: A dictionary containing the computed parameters.
        """
        # Perform the actual computation here
        protein = ProteinAnalysis(seq)
        peptide = peptides.Peptide(seq)

        # Heavy computation
        amino_acids_count = protein.count_amino_acids()
        protein_length = len(seq)
        protein_mw = round(float("%0.2f" % protein.molecular_weight()) / 1000, 2)
        isoelectric_point = float("%0.2f" % protein.isoelectric_point())
        gravy = float("%0.2f" % protein.gravy())
        aromaticity = float("%0.2f" % protein.aromaticity())
        charge = round(peptide.charge(pKscale="Murray"), 2)
        instability_index = float("%0.2f" % protein.instability_index())
        aliph_index = round(peptide.aliphatic_index(), 2)
        boman = round(peptide.boman(), 2)
        SSF = protein.secondary_structure_fraction()
        helix = round(float("%0.2f" % SSF[0]), 2)
        turn = round(float("%0.2f" % SSF[1]), 2)
        sheet = round(float("%0.2f" % SSF[2]), 2)
        descriptors = peptide.descriptors()
        atom_composition = self.calculate_atomic_composition(seq)

        return {
            'amino_acids_count': amino_acids_count,
            'protein_length': protein_length,
            'molecular_weight': protein_mw,
            'isoelectric_point': isoelectric_point,
            'gravy': gravy,
            'aromaticity': aromaticity,
            'charge': charge,
            'instability_index': instability_index,
            'aliphatic_index': aliph_index,
            'boman_index': boman,
            'helix': helix,
            'turn': turn,
            'sheet': sheet,
            'descriptors': descriptors,
            'atom_composition': atom_composition
        }
    
    def calculate_atomic_composition(self, seq):
        """
        Calculates the atomic composition of the protein sequence.
        
        This method counts the number of each type of atom (C, H, O, N, S) in the sequence.
        
        Args:
            seq (str): The protein sequence.
        
        Returns:
            dict: A dictionary containing the atomic counts.
        """
        atom_counts = {
            'C': 0,
            'H': 0,
            'O': 0,
            'N': 0,
            'S': 0
        }
        
        atomic_weights = self.aa_atomic_composition
        
        for aa in seq:
            if aa in atomic_weights:
                for atom, count in atomic_weights[aa].items():
                    atom_counts[atom] += count

        return atom_counts

    def update_ui(self, results):
        """
        Updates the UI with the computed protein analysis results.
        
        Args:
            results (dict): The computed protein analysis results.
        """
        results_box = ProteinAnalysisResult()
        results_box.update_results(results)
        self.ids.protein_analysis_result.add_widget(results_box)
        
    def disable_inputs(self):
        """
        Disables input fields and buttons during the analysis process.
        """
        self.ids.protein_seq_input.disabled = True
        self.ids.analysis_btn.disabled = True
        self.ids.analysis_btn.text = 'Wait ...'
        
    def enable_inputs(self):
        """
        Re-enables input fields and buttons after the analysis process is complete.
        """
        self.ids.protein_seq_input.disabled = False
        self.ids.analysis_btn.disabled = False
        self.ids.analysis_btn.text = 'Compute Parameters'        