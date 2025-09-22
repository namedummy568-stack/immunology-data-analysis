
def process_t_cell_data(data):
    """
    Processes raw T-cell data.
    """
    print("Processing T-cell data...")
    # Placeholder for actual data processing logic
    processed_data = [d.upper() for d in data]
    return processed_data

def calculate_activation_markers(processed_data):
    """
    Calculates T-cell activation markers from processed data.
    """
    print("Calculating activation markers...")
    # Placeholder for actual activation marker calculation logic
    activation_markers = {f"{cell}_marker": len(cell) for cell in processed_data}
    return activation_markers

if __name__ == "__main__":
    sample_data = ["cell_a", "cell_b", "cell_c"]
    processed_result = process_t_cell_data(sample_data)
    print(f"Processed data: {processed_result}")

    activation_markers_result = calculate_activation_markers(processed_result)
    print(f"Activation markers: {activation_markers_result}")
