import pandas as pd
import matplotlib.pyplot as plt

# Prompt user for input data for each month
data = []
for i in range(1, 13):
    month = input(f"Enter the month ({i}/12): ")
    hours_worked = float(input(f"Enter hours worked in {month}: "))
    client_satisfaction = float(input(f"Enter client satisfaction percentage in {month}: "))
    projects_realized = int(input(f"Enter number of projects realized in {month}: "))
    third_party_mentions = int(input(f"Enter number of third-party mentions in {month}: "))
    collaborations = int(input(f"Enter number of collaborations in {month}: "))
    data.append({'Month': month, 'Hours_Worked': hours_worked, 'Client_Satisfaction': client_satisfaction,
                 'Projects_Realized': projects_realized, 'Third_Party_Mentions': third_party_mentions,
                 'Collaborations': collaborations})

# Convert data to DataFrame
df = pd.DataFrame(data)

# Plot general success growth for hours worked, client satisfaction, projects realized, third-party mentions, and collaborations
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Hours_Worked'], label='Hours Worked', marker='o')
plt.plot(df['Month'], df['Client_Satisfaction'], label='Client Satisfaction (%)', marker='o')
plt.plot(df['Month'], df['Projects_Realized'], label='Projects Realized', marker='o')
plt.plot(df['Month'], df['Third_Party_Mentions'], label='Third-Party Mentions', marker='o')
plt.plot(df['Month'], df['Collaborations'], label='Collaborations', marker='o')
plt.xlabel('Month')
plt.ylabel('Metrics')
plt.title('General Success Growth Over 12 Months')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
