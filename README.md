
# Fault Diagnosis in Analog Circuits using Machine Learning

## Overview

This project involves analyzing and visualizing data using various Python libraries. It reads multiple CSV files, processes the data, and generates plots for real and imaginary parts of the Monte Carlo simulation data.

## Introduction

Analog circuits are critical for continuous signal processing, representing natural world phenomena with high fidelity and accuracy. Despite advancements in digital technology, analog circuits remain indispensable for high-frequency signal processing applications. This project focuses on improving fault detection accuracy and efficiency in analog circuits through innovative machine learning techniques.

## Problem Statement

Improving fault detection accuracy and efficiency in analog circuits using machine learning techniques to ensure reliable performance by identifying both catastrophic and parametric faults.


## Objective

- Develop a machine learning-based system for accurate fault detection in analog circuits.
- Enhance the efficiency of fault classification.
- Ensure reliable performance of analog circuits by identifying both catastrophic and parametric faults.
## System Architecture

- **Data Collection:** Gathering data from simulations and experiments.
- **Feature Extraction:** Extracting relevant features from the data.
- **Model Training:** Training machine learning models using extracted features.
- **Fault Classification:** Classifying faults using trained models.
- Validation and Testing: Validating the model's accuracy and efficiency.



## Libraries Used

**numpy:** Used for numerical operations, efficient array handling, and mathematical functions.

**pandas:** Used for data manipulation and analysis. It provides data structures and functions needed to manipulate structured data seamlessly.

**matplotlib:** FUsed for creating static, animated, and interactive visualizations in Python. It helps in plotting the data and visualizing the results.

**scikit-learn:** Used for implementing machine learning algorithms and techniques. It provides simple and efficient tools for data mining and data analysis.



## Getting Started 
Contributions are always welcome! To start contributing on this project read the Prerequisites below. Please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Prerequisites

- **Python 3.12**
- **Required libraries** (pandas, numpy, matplotlib, scikit-learn)
- **Required files** (Faults of the circuit (F0.csv to F8.csv) , Monte Carlo_200.csv)




## Files Description

- **F0.csv to F8.csv:** These files contain data that will be read and printed by the script.
- **Monte Carlo_200.csv:** Contains Monte Carlo simulation data which includes frequency, real, and imaginary parts of the data.
- **fault_anaylis.py:** The main script that processes and visualizes the data.

## Installation

#### 1) Clone the repository:
```bash
 git clone https://github.com/Deveshch710/Fault-Ditection-in-circuits
```
#### 2) Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
#### 3) Install the required libraries/dependencies
```bash
pip install numpy pandas matplotlib scikit-learn
```


    
## Usage/Examples

#### 1) Run the Streamlit app:
```bash
python fault_analysis.py
```



## Acknowledgements

 - Our mentors and professors  and team members for their dedication, hard work, and collaborative spirit.
- The authors of the reference papers whose research provided the foundation and inspiration for this work. [Paper 1](https://www.researchgate.net/publication/2983235_Nanowatt_Sub-nS_OTAs_With_Sub-10-mV_Input_Offset_Using_Series-Parallel_Current_Mirrors), [Paper 2](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=45013), [Paper 3](https://www.sciencedirect.com/science/article/abs/pii/S0026269214002274), [Paper 4](https://www.sciencedirect.com/science/article/abs/pii/S0026269214002274) ,[Paper 5](https://link.springer.com/chapter/10.1007/978-981-15-0426-6_7), [Paper 6](http://pep.ijieee.org.in/journal_pdf/11-110-142294318851-55.pdf), [Paper 7](https://www.academia.edu/33776003/DESIGN_OF_LOW_POWER_OPERATIONAL_TRANSCONDUCTANCE_AMPLIFIER_FOR_BIOMEDICAL_APPLICATIONS), 
 - Developers of  [numpy](https://numpy.org/doc/stable/user/absolute_beginners.html), [pandas](https://pandas.pydata.org/docs/getting_started/overview.html), [matplotlib](https://matplotlib.org/), [scikit-learn](https://scikit-learn.org/stable/), and other libraries used in this project.



## License

This project is licensed under the MIT License. See the LICENSE file for details. [MIT](https://choosealicense.com/licenses/mit/)

