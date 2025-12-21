### Title: Ocean Climate & Marine Life
### Student: Pavan Kumar
### Course: AIT-620

# About Data and Problem
As climate change accelerates, the world's oceans are experiencing significant transformations. This dataset compiles synthetic-yet-realistic measurements of sea surface temperature (SST), pH levels, coral bleaching severity, and species observations from ecologically critical marine zones. It spans from 2015 to 2023 and simulates how marine environments are responding to global warming, acidification, and heatwaves.

Data Types:

Column-Name 	            Description
Date	                    Date of observation
Location	                Marine location name (e.g., Great Barrier Reef, Maldives)
Latitude	                Latitude of the observation site
Longitude	                Longitude of the observation site
SST (°C)	                Sea Surface Temperature in degrees Celsius
pH Level	                Acidity level of seawater (lower means more acidic, a sign of acidification)
Bleaching Severity	        Categorical variable: None, Low, Medium, High
Species Observed	        Count of marine species observed during the sampling period
Marine Heatwave         	Boolean flag (True/False) indicating whether SST > 30°C

### Location of DATA: https://www.kaggle.com/datasets/atharvasoundankar/shifting-seas-ocean-climate-and-marine-life-dataset/data
 *This dataset has only 500 rows, I downloaded on the loal system for easy use and I have uploaded to GitHub also, as it's on local path.*


### Step 1: Data Inspection & Handling Missing Values
The Logic: We need to see how many categories we have and if there are any "holes" (Missing Values) in the data. In our dataset, the column Bleaching Severity has 150 missing values. If we don't fix this, the model won't know how to handle those cases.

### Phase 1: Data Preparation
*Objective: Load and clean the realistic_ocean_climate_dataset.csv.*

Key Actions:

- Data Profiling: Used .info() to understand the data distribution and identify gaps.

- Missing Value Imputation: Discovered 150 missing entries in the Bleaching Severity column.

- Logic: I just deleted the column (Bleaching Severity) as around 30% are null values, and we have High, Medium, Low as around 37, 37, and 25. Mathematically, it feels wrong, and it will cause the training results not to give importance values, as well as data separate all over because of 30% null values. 

### Phase 2: Feature Engineering & Target Selection
*Objective: Transform categorical data into numerical format and define the prediction goal.*

Key Actions:
- One-Hot Encoding: Applied to the Location column to convert geographical names into a machine-readable binary format. This prevents the model from assuming a numerical hierarchy between different ocean regions.Label 
- Selection: Designated SST (°C) (Sea Surface Temperature) as the target variable ($y$).
- Mathematical Shift: By selecting a continuous numerical value as the label, the project moves from a Classification task to a Regression task. Performance will be measured by the distance between predicted and actual temperatures rather than percentage accuracy.

### Phase 3: Feature Scaling (Standardization)
*Objective: Normalize the range of independent variables so each "clue" has an equal impact on the model.*

Key Actions:
- StandardScaler Application: Applied to numerical features including Latitude, Longitude, pH Level, and Species 
- Observed.Logic: Without scaling, the model might incorrectly prioritize features with larger numerical values (like Species Observed which ranges from 50-200) over features with smaller values (like pH Level which stays around 8.0).
- Mathematical Foundation: Used the $Z$-score formula to transform data so that the mean of each feature is $0$ and the standard deviation is $1$. This ensures the optimizer (the model's "learning engine") can find the best solution faster and more accurately.


### Phase 4: Model Validation Strategy & Data Distribution
*Objective: Partition data for evaluation and visualize feature relationships.*

**Key Actions:**

- Train/Test Split: Partitioned the dataset into an 80/20 split.
- Training Set: 400 samples used for model learning.
- Test Set: 100 samples reserved for unbiased performance evaluation.
- Dimensionality Reduction (PCA): Implemented PCA to project the 12-dimensional feature space into a 2D visualization.
- Logic: This "Data Spread" visualization confirms that the model can distinguish between geographical regions based on the climate features provided. Clear clustering indicates that the features are distinct, while overlapping clusters highlight areas where the model may require more complex "clues" to improve accuracy.

### Phase 5: Model Training & Evaluation (Regression)
*Objective: Train a Random Forest Regressor to predict Sea Surface Temperature (SST).*

**Key Actions:**
- Algorithm Choice: Selected Random Forest Regressor for its ability to handle non-linear relationships and provide feature importance.
- Training: Fitted the model using 100 decision trees on the training subset ($X_{train}, y_{train}$).
- Evaluation Metrics:MAE (Mean - Absolute Error): 0.68. Indicates that predictions are, on average, within 0.68°C of the actual value.$R^2$ Score: 0.69. Demonstrates that 69% of the variance in ocean temperature is captured by our features.
- Feature Importance Analysis: Visualized which environmental factors (like Latitude and pH) contribute most significantly to temperature fluctuations.

### Phase 6: Scenario Analysis & Visual Validation
*Objective: Use the trained model to perform "What-If" simulations and validate prediction accuracy.*

Key Actions:
- Actual vs. Predicted Analysis: Generated a regression plot to visualize the residuals. The tight grouping of data points around the $y=x$ identity line confirms a strong correlation ($R^2=0.69$) and low variance in errors.
- Climate Sensitivity Simulation: Conducted a "What-If" test by simulating a significant drop in ocean pH (Acidification).
- Findings: The model predicted a correlated rise in Sea Surface Temperature of approximately 1.18°C.
- Conclusion: This demonstrates that the model has successfully learned the complex relationship between ocean chemistry and climate warming, allowing it to be used as a tool for environmental impact forecasting.

### Phase 7: Hyperparameter Optimization
*Objective: Fine-tune the model architecture to minimize prediction error.* 

Key Actions:
- Grid Search Cross-Validation (GridSearchCV): Automatically tested various configurations of the Random Forest (Tree count, Depth, and Leaf size).
- Logic: Optimization ensures the model is neither too simple (underfitting) nor too complex (overfitting). By testing each setting against 5 different subsets of data (5-fold CV), we ensure the results are statistically stable.
- Outcome: Identified optimal parameters (n_estimators: 200).
- Performance Gain: Reduced Mean Absolute Error to $0.65^{\circ}C$ and increased the $R^2$ score to $0.72$.


