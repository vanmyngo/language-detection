# Language Detection
Detect spoken language using input from the device's microphone. The main purpose is to determine language with no knowledge of what language is the speaker speaking in. There are language translation API that input the original language but finding an API to determine what language is someone speaking in is not easy.  
Created for Natural Language Processing class at UTSA during spring of 2023.

# Replication
Follow the following steps to set up the virtual environment.
### 1. Install requirements
Clone git repo: `git clone https://github.com/vanmyngo/language-detection.git`  

To install anaconda, follow the instruction on [here](https://docs.anaconda.com/free/anaconda/install/index.html).  
Anaconda: `conda env create -f ./language-detection/requirements.yml`  

If you prefer python venv then follow [this](https://docs.python.org/3/library/venv.html) link to add a venv.  
Python: `pip install -r ./language-detection/requirements.txt`  
### 2.1 Anaconda environment
You can use Jupyer Lab or Notebook but I'm more familiar with Jupyter Lab.  
Install Jupyter Lab into base environment, if not already by: `conda install -c conda-forge jupyterlab`  

Add conda environment into Jupyter:   
```
(base)$ conda activate cenv
(cenv)$ conda install ipykernel
(cenv)$ ipython kernel install --user --name=<any_name_for_kernel>
(cenv)$ conda deactivate
```

If ipykernel is already installed, add conda environment to Jupyter in the next step.  
Open Jupyer Lab: `(base)$ jupyter lab`  
Open notebook in Jupyter Lab and select "Run All Cells" in the upper "Run" tab.
### 2.2 Python script
`(venv)$ python ./language-detection/EE4953-LanguageDetection.py`
### 3. Enjoy!
There might be some issue with connecting to your local microphone so adjust it as you see best.

# Licenses
Licenses for third-party libraries used in this project are stored in "Licenses" folder and are named accordingly.
