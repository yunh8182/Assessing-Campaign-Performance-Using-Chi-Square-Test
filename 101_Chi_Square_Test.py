
# AB Testing - Our Task for ABC Grocery

# Import Required Packages

import pandas as pd
from scipy.stats import chi2_contingency, chi2


# Import data

campaign_data = pd.read_excel('grocery_database.xlsx', sheet_name='campaign_data')

# Filter our data

campaign_data = campaign_data.loc[campaign_data['mailer_type'] != 'Control']

# Summarise to get our observed frequencies

observed_values = pd.crosstab(campaign_data['mailer_type'], campaign_data['signup_flag']).values
mailer1_signup_rate = 123/(252+123)
mailer2_signup_rate = 127/(209+127)

# State Hypotheses & set acceptance criteria

null_hypothesis = 'There is no relationsip between mailer type and signup rate.  There are independent'
alternate_hypothesis = 'There is a relationsip between mailer type and signup rate.  There are not independent'
acceptance_criteria = 0.05


# Calculate expected frequencies & Chi Square Statistic

chi2_statistic, p_value, dof, expected_values = chi2_contingency(observed_values, correction = False)
print(chi2_statistic, p_value)

# Find the critical value for our test
# ppf is the percentage function

critical_value = chi2.ppf(1-acceptance_criteria, dof)
print(critical_value)

# Print the results (Chi Square Statistic)

if chi2_statistic >= critical_value:
    
    print(f'As our chi-quare statistic of {chi2_statistic} is higher than our critical value of {critical_value} - we reject the null hypothesis, and conclude that : {alternate_hypothesis}')
else:
    print(f'As our chi-quare statistic of {chi2_statistic} is lower than our critical value of {critical_value} - we retain the null hypothesis, and conclude that : {null_hypothesis}')

# Print the results (p-value)


if p_value <= acceptance_criteria:
    
    print(f'As our p_value  of {p_value} is lower than our acceptance_criteriae of {acceptance_criteria} - we reject the null hypothesis, and conclude that : {alternate_hypothesis}')
else:
    print(f'As our p_value  of {p_value} is higher than our acceptance_criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that : {null_hypothesis}')

















