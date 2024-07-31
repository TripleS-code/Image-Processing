import pandas as pd

def process_data(file_path, output_file_path):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Display the first few rows of the dataframe
        print("Original Data:")
        print(df.head())

        # Check required columns
        required_columns = ['State', 'Center Type', 'Number of Tests']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Column '{col}' does not exist in the dataframe.")

        # Separate the data by center type (SHC and PHC)
        shc_df = df[df['Center Type'] == 'SHC']
        phc_df = df[df['Center Type'] == 'PHC']

        # Count SHCs and PHCs per state
        shc_count_per_state = shc_df.groupby('State').size()
        phc_count_per_state = phc_df.groupby('State').size()

        print("\nSHC Count per State:")
        print(shc_count_per_state)

        print("\nPHC Count per State:")
        print(phc_count_per_state)

        # For SHCs: count the number of tests
        shc_test_counts = {
            'Below 7': shc_df[shc_df['Number of Tests'] < 7].groupby('State').size(),
            '7 to 10': shc_df[(shc_df['Number of Tests'] >= 7) & (shc_df['Number of Tests'] <= 10)].groupby('State').size(),
            '11 or more': shc_df[shc_df['Number of Tests'] > 10].groupby('State').size()
        }

        print("\nSHC Test Counts by Category:")
        for category, counts in shc_test_counts.items():
            print(f"\n{category}:")
            print(counts)

        # For PHCs: count the number of tests
        phc_test_counts = {
            'Below 31': phc_df[phc_df['Number of Tests'] < 31].groupby('State').size(),
            '31 to 49': phc_df[(phc_df['Number of Tests'] >= 31) & (phc_df['Number of Tests'] <= 49)].groupby('State').size(),
            '50 or more': phc_df[phc_df['Number of Tests'] > 49].groupby('State').size()
        }

        print("\nPHC Test Counts by Category:")
        for category, counts in phc_test_counts.items():
            print(f"\n{category}:")
            print(counts)

        # Save results to a new Excel file
        with pd.ExcelWriter(output_file_path) as writer:
            shc_count_per_state.to_excel(writer, sheet_name='SHC Count per State')
            phc_count_per_state.to_excel(writer, sheet_name='PHC Count per State')

            for category, counts in shc_test_counts.items():
                counts.to_frame(name=category).to_excel(writer, sheet_name=f'SHC {category}')

            for category, counts in phc_test_counts.items():
                counts.to_frame(name=category).to_excel(writer, sheet_name=f'PHC {category}')

        print(f"\nResults saved to {output_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    file_path = 'C:\Users\SATWIK SAHOO\PycharmProjects\pythonProject\FPE_Entry_19-Jul-2024_9-15-52_AM.csv'  # Path to your Excel file
    output_file_path = 'processed_data.xlsx'     # Path to save the processed data

    process_data(file_path, output_file_path)


# Count the occurrences of a specific word, e.g., 'SHC'
word_to_count = 'SHC'
word_count = df['Column1'].str.contains(word_to_count, case=False).sum()

print(f"\nNumber of occurrences of '{word_to_count}': {word_count}")

# Save the sorted dataframe to a new Excel file
sorted_file_path = 'sorted_data.xlsx'
df_sorted.to_excel(sorted_file_path, index=False)

print(f"\nSorted data saved to {sorted_file_path}")
