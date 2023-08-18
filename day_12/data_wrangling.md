# Steps for Data wrangling

1. Gather the Data
2. Assess the data (EDA)
3. Cleaning the Data
   1. Dealing with missing values
   2. correcting errors in the data

      1. Removing outliers in the data

         1. Visualization
         2. IQR method

         Q1=df1.age.quantile(0.25)

         Q3=df1.age.quantile(0.75)

         IQR=Q3-Q1

         lower_bound=Q1-1.5*IQR

         upper_bound=Q3+1.5*IQR

         df=df[(df['age']>lower_bound)& (df['age']<upper_bound)]
          3. Z- Score:
          4. Dropping/ removing duplicates
4. Transform the Data
   1. Normalize the data
      1. Min-Max Scaling
      2. Standard scaler
      3. Z-score Standardization
      4. Decimal Scaling
      5. Log Transformation
      6. Robust Scaling
5. Feature Engineering
6. Organizing the data(organization)
   1. Columns creation
   2. Renaming the columns
