import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import calendar



def prepare_data():
    """"Load the data from CSV files into pandas dataframes.
        Converts the date column to datetime format and
        the numeric columns to float format.
        Merges dataframes.
        """
    wig20_df = pd.read_csv(r"C:\Python Scripts\Learning\Licencjat\Dane\Dane historyczne dla WIG20.csv", delimiter=',')
    dax_df = pd.read_csv(r"C:\Python Scripts\Learning\Licencjat\Dane\Dane historyczne dla DAX.csv", delimiter=',')
    nasdaq_df = pd.read_csv(r"C:\Python Scripts\Learning\Licencjat\Dane\Dane historyczne dla NASDAQ Composite.csv", delimiter=',')
    
    wig20_df['Data'] = pd.to_datetime(wig20_df['Data'], format='%d.%m.%Y')
    dax_df['Data'] = pd.to_datetime(dax_df['Data'], format='%d.%m.%Y')
    nasdaq_df['Data'] = pd.to_datetime(nasdaq_df['Data'], format='%d.%m.%Y')

    wig20_df['Ostatnio'] = wig20_df['Ostatnio'].str.replace(".","").str.replace(",",".").astype(float)
    dax_df['Ostatnio'] = dax_df['Ostatnio'].str.replace(".","").str.replace(",",".").astype(float)
    nasdaq_df['Ostatnio'] = nasdaq_df['Ostatnio'].str.replace(".","").str.replace(",",".").astype(float)

    merged_df = pd.merge(wig20_df[['Data', 'Ostatnio']], dax_df[['Data', 'Ostatnio']], left_on='Data', right_on='Data', suffixes=('_WIG20', '_DAX'))
    merged_df = pd.merge(merged_df, nasdaq_df[['Data', 'Ostatnio']], left_on='Data', right_on='Data')
    merged_df.columns = ['Data', 'WIG20', 'DAX', 'NASDAQ']
    return merged_df
    
def covid_analysis(df):
    """Filter merged dataframe by analysed period"""
    first_day = "2020-01-01"
    last_day = "2020-04-01"
    
    merged_df = df[(df['Data']>=first_day) & (df['Data']<= last_day)]
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Plot the first dataset with the first y-axis and include it in the legend
    wig20, = ax1.plot(merged_df['Data'], merged_df['WIG20'], label='WIG20', color='blue')
    ax1.set_xlabel('Data')
    ax1.set_ylabel('WIG20 cena zamknięcia', color='black')
    
    # Create a second y-axis
    ax2 = ax1.twinx()
    dax, = ax2.plot(merged_df['Data'], merged_df['DAX'], label='DAX', color='red')
    NASDAQ, = ax2.plot(merged_df['Data'], merged_df['NASDAQ'], label='NASDAQ', color='green')
    ax2.set_ylabel('DAX & NASDAQ cena zamknięcia', color='black')

    # Combine the legends from both axes
    lines = [wig20, dax, NASDAQ]
    labels = [line.get_label() for line in lines]
    plt.legend(lines, labels)
    plt.title('Porównanie Cen Indeksów Giełdowych')
    plt.show()
    
    # Calculate the correlation matrix
    correlation_matrix = merged_df[['WIG20', 'DAX', 'NASDAQ']].corr()

    # Visualize the correlations using a heat map
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title('Macierz korelacji indeksów giełdowych')
    plt.show()

    merged_df.set_index('Data', inplace=True)

    # Resample the data to monthly frequency and calculate the percentage change
    monthly_changes = merged_df.resample('M').mean().pct_change()
    monthly_changes.dropna(how = "all", inplace=True)
    monthly_changes['Month'] = monthly_changes.index.month
    monthly_changes['Month'] = monthly_changes['Month'].map(lambda x: calendar.month_name[x])
    monthly_changes.reset_index(inplace=True)
    monthly_changes = monthly_changes[['Month', 'WIG20', 'DAX', 'NASDAQ']]

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Hide the axes and the ticks
    ax.axis('off')

    # Create a table from the monthly changes DataFrame
    table_data = monthly_changes.applymap(lambda x: f'{x:.2%}' if not isinstance(x, str) else x)

    col_labels = table_data.columns.tolist()

    table = ax.table(cellText=table_data.values,
                    colLabels=col_labels,
                    cellLoc='center',
                    loc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    ax.set_title('Miesięczne zmiany procentowe w porównaniu do poprzedniego miesiąca')
    plt.show()
    

    merged_df.reset_index(inplace=True)
    weekly_changes = merged_df.set_index('Data').resample('W').mean().pct_change()
    weekly_changes.dropna(how = 'all',inplace=True)
    # Add a 'Week' column to the weekly changes DataFrame
    weekly_changes['Week'] = weekly_changes.index.week

    # Map week numbers to week ranges
    weekly_changes['Week'] = weekly_changes['Week'].map(lambda x: f'Week {x}')
    weekly_changes = weekly_changes[['Week', 'WIG20', 'DAX', 'NASDAQ']]

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Hide the axes and the ticks
    ax.axis('off')

    table_data = weekly_changes.applymap(lambda x: f'{x:.2%}' if not isinstance(x, str) else x)
    col_labels = table_data.columns.tolist()

    table = ax.table(cellText=table_data.values,
                    colLabels=col_labels,
                    cellLoc='center',
                    loc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    ax.set_title('Tygodniowe zmiany procentowe w porównaniu do poprzedniego tygodnia')
    plt.show()

def ru_ua_analysis(df):
    first_day = "2022-01-01"
    last_day = "2022-04-01"
    merged_df = df[(df['Data']>=first_day) & (df['Data']<= last_day)]

    # Create the figure and axes
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot the first dataset with the first y-axis and include it in the legend
    wig20, = ax1.plot(merged_df['Data'], merged_df['WIG20'], label='WIG20', color='blue')
    ax1.set_xlabel('Data')
    ax1.set_ylabel('WIG20 cena zamknięcia', color='black')

    # Create a second y-axis
    ax2 = ax1.twinx()

    # Plot the remaining datasets with the second y-axis
    dax, = ax2.plot(merged_df['Data'], merged_df['DAX'], label='DAX', color='red')
    NASDAQ, = ax2.plot(merged_df['Data'], merged_df['NASDAQ'], label='NASDAQ', color='green')
    ax2.set_ylabel('DAX & NASDAQ cena zamknięcia', color='black')

    # Combine the legends from both axes
    lines = [wig20, dax, NASDAQ]
    labels = [line.get_label() for line in lines]
    plt.legend(lines, labels)

    # Set the title
    plt.title('Porównanie Cen Indeksów Giełdowych')

    # Display the plot
    plt.show()

    # Calculate the correlation matrix
    correlation_matrix = merged_df[['WIG20', 'DAX', 'NASDAQ']].corr()

    # Visualize the correlations using a heat map
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title('Macierz korelacji indeksów giełdowych')
    plt.show()

    merged_df.set_index('Data', inplace=True)

    # Resample the data to monthly frequency and calculate the percentage change
    monthly_changes = merged_df.resample('M').mean().pct_change()
    monthly_changes.dropna(how = "all", inplace=True)
    monthly_changes['Month'] = monthly_changes.index.month
    monthly_changes['Month'] = monthly_changes['Month'].map(lambda x: calendar.month_name[x])
    monthly_changes.reset_index(inplace=True)
    monthly_changes = monthly_changes[['Month', 'WIG20', 'DAX', 'NASDAQ']]

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Hide the axes and the ticks
    ax.axis('off')

    # Create a table from the monthly changes DataFrame
    table_data = monthly_changes.applymap(lambda x: f'{x:.2%}' if not isinstance(x, str) else x)

    col_labels = table_data.columns.tolist()

    table = ax.table(cellText=table_data.values,
                    colLabels=col_labels,
                    cellLoc='center',
                    loc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    ax.set_title('Miesięczne zmiany procentowe w porównaniu do poprzedniego miesiąca')
    plt.show()
    

    merged_df.reset_index(inplace=True)
    weekly_changes = merged_df.set_index('Data').resample('W').mean().pct_change()
    weekly_changes.dropna(how = 'all',inplace=True)
    # Add a 'Week' column to the weekly changes DataFrame
    weekly_changes['Week'] = weekly_changes.index.week

    # Map week numbers to week ranges
    weekly_changes['Week'] = weekly_changes['Week'].map(lambda x: f'Week {x}')
    weekly_changes = weekly_changes[['Week', 'WIG20', 'DAX', 'NASDAQ']]

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Hide the axes and the ticks
    ax.axis('off')

    table_data = weekly_changes.applymap(lambda x: f'{x:.2%}' if not isinstance(x, str) else x)
    col_labels = table_data.columns.tolist()

    table = ax.table(cellText=table_data.values,
                    colLabels=col_labels,
                    cellLoc='center',
                    loc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    ax.set_title('Tygodniowe zmiany procentowe w porównaniu do poprzedniego tygodnia')
    plt.show()



def bank_crysis_analysis(df):
    first_day = "2007-06-01"
    last_day = "2009-01-01"

    #Filter merged dataframe by analysed period
    merged_df = df[(df['Data']>=first_day) & (df['Data']<= last_day)]
    
    # Create the figure and axes
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot the first dataset with the first y-axis and include it in the legend
    wig20, = ax1.plot(merged_df['Data'], merged_df['WIG20'], label='WIG20', color='blue')
    NASDAQ, = ax1.plot(merged_df['Data'], merged_df['NASDAQ'], label='NASDAQ', color='green')
    ax1.set_xlabel('Data')
    ax1.set_ylabel('WIG20 & NASDAQ cena zamknięcia', color='black')

    # Create a second y-axis
    ax2 = ax1.twinx()

    # Plot the remaining datasets with the second y-axis
    dax, = ax2.plot(merged_df['Data'], merged_df['DAX'], label='DAX', color='red')
    ax2.set_ylabel('DAX cena zamknięcia', color='black')

    # Combine the legends from both axes
    lines = [wig20, dax, NASDAQ]
    labels = [line.get_label() for line in lines]
    plt.legend(lines, labels)

    # Set the title
    plt.title('Porównanie Cen Indeksów Giełdowych')

    # Display the plot
    plt.show()

    # Calculate the correlation matrix
    correlation_matrix = merged_df[['WIG20', 'DAX', 'NASDAQ']].corr()

    # Visualize the correlations using a heat map
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title('Macierz korelacji indeksów giełdowych')
    plt.show()

    merged_df.set_index('Data', inplace=True)

    # Resample the data to monthly frequency and calculate the percentage change
    monthly_changes = merged_df.resample('M').mean().pct_change()
    monthly_changes.dropna(how = "all", inplace=True)
    monthly_changes['Month'] = monthly_changes.index.month
    monthly_changes['Month'] = monthly_changes['Month'].map(lambda x: calendar.month_name[x])
    monthly_changes.reset_index(inplace=True)
    monthly_changes = monthly_changes[['Month', 'WIG20', 'DAX', 'NASDAQ']]

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Hide the axes and the ticks
    ax.axis('off')

    # Create a table from the monthly changes DataFrame
    table_data = monthly_changes.applymap(lambda x: f'{x:.2%}' if not isinstance(x, str) else x)

    col_labels = table_data.columns.tolist()

    table = ax.table(cellText=table_data.values,
                    colLabels=col_labels,
                    cellLoc='center',
                    loc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    ax.set_title('Miesięczne zmiany procentowe w porównaniu do poprzedniego miesiąca')
    plt.show()
    

    merged_df.reset_index(inplace=True)
    weekly_changes = merged_df.set_index('Data').resample('W').mean().pct_change()
    weekly_changes.dropna(how = 'all',inplace=True)
    # Add a 'Week' column to the weekly changes DataFrame
    weekly_changes['Week'] = weekly_changes.index.week

    # Map week numbers to week ranges
    weekly_changes['Week'] = weekly_changes['Week'].map(lambda x: f'Week {x}')
    weekly_changes = weekly_changes[['Week', 'WIG20', 'DAX', 'NASDAQ']]

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Hide the axes and the ticks
    ax.axis('off')

    table_data = weekly_changes.applymap(lambda x: f'{x:.2%}' if not isinstance(x, str) else x)
    col_labels = table_data.columns.tolist()

    table = ax.table(cellText=table_data.values,
                    colLabels=col_labels,
                    cellLoc='center',
                    loc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    ax.set_title('Tygodniowe zmiany procentowe w porównaniu do poprzedniego tygodnia')
    plt.show()


if __name__ == "__main__":
    final_df = prepare_data()
    covid_analysis(final_df)
    # ru_ua_analysis(final_df)
    # bank_crysis_analysis(final_df)
    print("DONE")