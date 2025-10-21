# carbon-calculation.py

def calculate_carbon_sequestration(num_trees, years_grown, average_tree_biomass_factor=0.5, carbon_fraction=0.5):
    """
    Estimates the total carbon sequestered in a forest.

    This is a highly simplified model based on average biomass and standard
    carbon content assumptions.

    Args:
        num_trees (int): The total number of trees in the area.
        years_grown (int): The average number of years the trees have grown.
        average_tree_biomass_factor (float): A factor representing the biomass
            gain per tree per year (e.g., tons of dry biomass/tree/year).
        carbon_fraction (float): The fraction of biomass that is pure carbon (usually ~0.5).

    Returns:
        float: Estimated total carbon sequestered (in tons).
    """
    # 1. Calculate total estimated dry biomass (simplified)
    # Total Biomass = Num Trees * Years Grown * Biomass Factor
    total_biomass = num_trees * years_grown * average_tree_biomass_factor

    # 2. Calculate the total carbon sequestered
    # Carbon Sequestered = Total Biomass * Carbon Fraction
    carbon_sequestered = total_biomass * carbon_fraction

    return carbon_sequestered

# --- Example Usage ---

# Define the input parameters for a hypothetical forest
forest_trees = 1000  # 1,000 trees
forest_age = 20      # 20 years of growth
biomass_factor = 0.05 # Assuming 0.05 tons of dry biomass gain per tree per year (highly variable!)

# Run the calculation
estimated_carbon = calculate_carbon_sequestration(
    num_trees=forest_trees,
    years_grown=forest_age,
    average_tree_biomass_factor=biomass_factor
)

# Print the result
print(f"Forest Parameters:")
print(f"  Number of Trees: {forest_trees}")
print(f"  Average Growth Period (Years): {forest_age}")
print(f"  Biomass Factor (tons/tree/year): {biomass_factor}")
print("-" * 30)
print(f"Estimated Total Carbon Sequestered: {estimated_carbon:.2f} tons")

# To get CO2 equivalent (CO2e), multiply by 3.67 (the ratio of the molecular weights of CO2 to C)
co2_equivalent = estimated_carbon * 3.67
print(f"Estimated Total CO2 Equivalent (CO2e): {co2_equivalent:.2f} tons")