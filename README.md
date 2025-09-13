# GroundWaterLevelDetection
Detecting Ground Water level using MLR

# Groundwater Level Prediction with Multiple Linear Regression

## Project Overview

This project analyzes groundwater depletion patterns and develops predictive models for groundwater levels across three critical regions in India using multiple linear regression techniques. The analysis is conducted for the Central Groundwater Board of India to support evidence-based policy making.

**Course**: MDS 302 | AI/ML & Applications | 2025-26  
**Assignment**: Assignment I (100 marks)  
**Due Date**: 8th September, 2025

## Study Regions

1. **Delhi NCR** - National Capital Region
2. **Western Uttar Pradesh Sugarcane Belt** - Districts: Muzaffarnagar, Meerut, Baghpat, Bulandshahar, Hapur, Gautam Buddha Nagar, Ghaziabad
3. **Vindhyan Region in UP** - Districts: Jhansi, Jalaun, Lalitpur, Mahoba, Hamirpur, Banda, Chitrakoot

## Objectives

- Understand the key drivers of groundwater depletion in the target regions
- Develop predictive models for groundwater levels at unsampled locations
- Provide confidence intervals for predictions to support policy decisions
- Identify significant factors influencing groundwater resources

## Project Structure

```
groundwater-prediction/
├── README.md
├── data/
│   ├── raw/              # Original downloaded datasets
│   ├── processed/        # Cleaned and merged datasets
│   └── metadata/         # Data source documentation
├── notebooks/
│   ├── 01_data_acquisition.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_exploratory_analysis.ipynb
│   ├── 04_model_development.ipynb
│   └── 05_prediction_evaluation.ipynb
├── src/
│   ├── data_processing.py
│   ├── model_utils.py
│   └── visualization.py
├── results/
│   ├── figures/          # EDA plots and visualizations
│   ├── models/           # Saved model objects
│   └── predictions/      # Model outputs and predictions
├── docs/
│   └── final_report.pdf  # 4-page project report
└── requirements.txt
```

## Methodology

### 1. Domain Knowledge Research
- Literature review on groundwater level determinants
- Identification of key environmental and anthropogenic factors

### 2. Model Specification
- **Dependent Variable**: Groundwater level (meters below ground level)
- **Independent Variables**: Precipitation, temperature, land use, irrigation intensity, population density, etc.
- **Spatial Unit**: District level analysis
- **Temporal Unit**: Annual/seasonal data
- **Model**: Multiple Linear Regression

### 3. Data Sources

| Source | Description | URL |
|--------|-------------|-----|
| India WRIS | Water Resources Information System | https://indiawris.gov.in/wris/ |
| Bhuvan ISRO | Earth observation data | https://bhuvan-app1.nrsc.gov.in/2dresources/bhuvanstore2.php |
| Copernicus CDS | Climate data | https://cds.climate.copernicus.eu/#!/home |
| NICES Portal | Natural resource data | https://nices.nrsc.gov.in/ |
| SHRUG Atlas | Socioeconomic data | https://www.devdatalab.org/atlas |

### 4. Analysis Pipeline

1. **Data Acquisition** - Download and collect relevant datasets
2. **Data Preprocessing** - Clean, merge, and handle missing values
3. **Exploratory Data Analysis** - Visualize patterns and relationships
4. **Model Assumptions Testing** - Validate Gauss-Markov assumptions
5. **Model Selection** - Use AIC/BIC criteria for best model
6. **Model Estimation** - Train final model and generate diagnostics
7. **Prediction & Evaluation** - Test model performance on holdout data
8. **Interpretation** - Analyze results and policy implications

## Key Features

### Model Assumptions Validation
- ✅ Linearity testing
- ✅ Multicollinearity assessment (VIF analysis)
- ✅ Exogeneity verification (zero conditional mean)
- ✅ Homoscedasticity testing (constant variance)

### Model Selection Criteria
- Akaike Information Criterion (AIC)
- Bayesian Information Criterion (BIC)
- Cross-validation performance

### Evaluation Metrics
- **Regression Metrics**: R², Adjusted R², RMSE, MAE
- **Statistical Tests**: F-statistic, t-tests for coefficients
- **Model Diagnostics**: Residual analysis, normality tests

## Installation & Usage

### Prerequisites
```bash
pip install -r requirements.txt
```

### Required Libraries
- pandas
- numpy
- scikit-learn
- statsmodels
- matplotlib
- seaborn
- geopandas (for spatial analysis)
- scipy

### Running the Analysis
```bash
# Step 1: Data acquisition
jupyter notebook notebooks/01_data_acquisition.ipynb

# Step 2: Data preprocessing
jupyter notebook notebooks/02_data_preprocessing.ipynb

# Step 3: Exploratory analysis
jupyter notebook notebooks/03_exploratory_analysis.ipynb

# Step 4: Model development
jupyter notebook notebooks/04_model_development.ipynb

# Step 5: Prediction and evaluation
jupyter notebook notebooks/05_prediction_evaluation.ipynb
```

## Expected Deliverables

### 1. Technical Outputs
- Trained multiple linear regression models for each region
- Model diagnostics and assumption validation results
- Prediction accuracy metrics on test data
- Feature importance and coefficient interpretations

### 2. Visualizations
- Spatial distribution maps of groundwater levels
- Time series plots showing temporal trends
- Correlation matrices and scatter plots
- Residual diagnostic plots

### 3. Final Report
A comprehensive 4-page report (Times New Roman, 12pt, single-spaced) covering:
- Literature review and domain knowledge
- Methodology and model specification
- Data sources and preprocessing steps
- Exploratory data analysis findings
- Model estimation results and diagnostics
- Prediction performance evaluation
- Policy recommendations and interpretations

## Key Research Questions

1. **What are the significant factors influencing groundwater resources?**
   - Climatic variables (precipitation, temperature)
   - Land use patterns and changes
   - Agricultural practices and irrigation intensity
   - Population density and urbanization

2. **How are these factors quantitatively related to groundwater levels?**
   - Coefficient magnitudes and directions
   - Statistical significance of relationships
   - Regional variations in factor importance

3. **How reliable are our predictions?**
   - Model accuracy metrics
   - Confidence intervals for predictions
   - Spatial and temporal validation results

## References

1. Sahoo, S., & Jha, M. (2013). Groundwater-level prediction using multiple linear regression and artificial neural network techniques: A comparative assessment. *Hydrogeology Journal*, 21, 1865-1887.

2. James, G., Witten, D., Hastie, T., Tibshirani, R., & Taylor, J. (2023). *An Introduction to Statistical Learning with Applications in Python*. Springer. Chapter 3.

## Contact Information

**Student**: [Your Name]  
**Course**: MDS 302 - AI/ML & Applications  
**Institution**: [Your Institution]  
**Email**: [Your Email]

---

*This project contributes to understanding groundwater sustainability in India's most water-stressed regions and supports data-driven policy interventions for groundwater management.*