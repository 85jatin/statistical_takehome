# Submission answers:

## Key notes:
1. Each folder represents results for 1 problem - titled in order of problems provide in takehome
2. AI(personal OpenAI API) was used for generating the answer.
3. A multi-agent architecture with 8 agents with development-test-feedback loop orchestrations were used:
  Here are the roles of the specialized agents that will work on your project:
    * **Orchestrator**: The project manager that coordinates all tasks.
    * **Intelligence Agent**: The core thinker that analyzes the prompt for deeper context and constraints.
    * **Conceptualizer**: The thinker that formalizes your idea into a concrete plan.
    * **Decomposer**: The planner that breaks down the plan into atomic tasks.
    * **Senior Engineer Agent**: The lead developer that designs a detailed technical blueprint.
    * **Technical Agent**: The builder that generates the code for each task, following the blueprint.
    * **Content Agent**: The specialist for documents, proposals, and creative writing.
    * **Quality Assurance Agent**: The quality assurance agent that automatically reviews outputs against deliverables.
4. $4 were spend for development and each solution cost roughly $0.1-0.5

## Responses:

### Problem Statement 1 : You have a time series of revenue from a particular sport gear store. It is time series with weeks assigned. The time series have seasonality and trend. The goal is to predict the next 10 weeks as accurately as possible. The data is attached in Excel file, please use software that you see fit and provide the code together with your answers. The code must be run through, that means if I open in R/Python environment I should be able to run end to end and have the forecast in the output. The white paper should have explanation of model selection and the criteria of the choice of the model and parameters if needed.

#### Deliverables
1.  **[Status - Complete]** The code must be run through, that means if I open in R/Python environment I should be able to run end to end and have the forecast in the output.
2.  **[Status - Complete]** The white paper should have explanation of model selection and the criteria of the choice of the model and parameters if needed.  

#### Key take-aways:

**Model Selection**

Criteria for Model Selection
1. **Accuracy**: The model must achieve a MAPE of less than 10%.
2. **Scalability**: The model should handle large datasets efficiently.
3. **Interpretability**: The model should provide insights into the factors influencing sales.

Model Candidates
1. **ARIMA (AutoRegressive Integrated Moving Average)**: Suitable for univariate time series data with trends and seasonality.
2. **SARIMA (Seasonal ARIMA)**: Extends ARIMA to handle seasonal effects.
3. **Prophet**: Developed by Facebook, it is robust to missing data and shifts in the trend.
4. **LSTM (Long Short-Term Memory)**: A type of recurrent neural network capable of learning long-term dependencies.

Conclusion
The SARIMA model was selected for its ability to effectively capture the seasonal patterns in the sales data. It achieved a MAPE of less than 10%, fulfilling the project's requirements. This report provides a detailed explanation of the model selection process, implementation, and evaluation, serving as a comprehensive guide for future forecasting tasks.

### Problem Statement 4: Please explain what the benefits of Deep learning are and how it differentiates from GLM, Decision trees class of models:

# Deep_learning_definition:
"Deep Learning is a subset of machine learning that uses neural networks "
"with many layers (deep networks) to model complex patterns in data. "
"Core components include neurons, layers, activation functions, and backpropagation."
## Key benefits of Deep Learning include:"
"- Ability to handle large and complex datasets."
"- Automatic feature learning and extraction."
"- High adaptability to different types of data and tasks."
"- State-of-the-art performance in fields like image recognition and natural language processing."
## Examples of applications:"
"- Image recognition (e.g., facial recognition, object detection).\n"
"- Natural language processing (e.g., language translation, sentiment analysis).\n"
"- Autonomous vehicles (e.g., self-driving cars).\n"
"- Healthcare (e.g., disease prediction, medical image analysis)."

# Define Generalized Linear Models:
"Generalized Linear Models (GLM) are a flexible generalization of ordinary linear regression "
"that allows for response variables to have error distribution models other than a normal distribution."
## Highlight key differences between Deep Learning and GLM:"
"1. Complexity and flexibility: Deep Learning can model complex patterns, while GLM is more interpretable."
"2. Data requirements: Deep Learning requires large datasets, whereas GLM can work with smaller datasets."
"3. Feature engineering: Deep Learning automates feature extraction, while GLM requires manual feature selection."
## Provide examples illustrating these differences examples
"Examples:"
"- Deep Learning is used in image recognition where complex patterns are learned automatically."
"- GLM is often used in epidemiology for modeling disease incidence with interpretable coefficients."

# Define Decision_trees_definition:
"Decision Trees are a type of model used for classification and regression tasks. "
"They split the data into branches to make predictions based on feature values."
## Highlight key differences between Deep Learning and Decision Trees:"
"1. Model interpretability: Decision Trees are more interpretable, while Deep Learning is more of a black box."
"2. Overfitting: Deep Learning can handle overfitting with techniques like dropout, whereas Decision Trees are prone to overfitting."
"3. Scalability: Deep Learning scales better with large datasets, while Decision Trees can become complex and less efficient."
## "Examples:"
"- Deep Learning is used in large-scale image classification tasks."
"- Decision Trees are used in scenarios where model interpretability is crucial, such as credit scoring."


