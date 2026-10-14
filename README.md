# RoboSapiensANNVerification

This is a repository for storing all artefacts related to running neural network verification tools on the RoboSapiens case studies.

The directory may be used directly by neural network verification tools to run all required proofs for the RoboSapiens case studies, in one place, so it is easy to invoke the tools
from here. The repository contains all properties, defined in VNNLIB format, that are tool independent, the networks in a tool-independent ONNX file, and tool configuration files, which are tool-specific files that contain parameter, method instations, or just ways of running the tool 


For each case study (DTI, PAL, Fraunhofer, and NTNU) we have a directory with the following sub-directories
- Networks: this contains files, in ONNX preferably, storing the networks for each case study.
- Properties: this contains files in VNNLIB, of properties to be proved for each case study. 
- ToolConfig: For alpha-beta CROWN (ABCRown) in yaml format, then other tools will be added as necessary. 
