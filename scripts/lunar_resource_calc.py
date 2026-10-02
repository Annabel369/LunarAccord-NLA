#!/usr/bin/env python3
"""
Lunar Resource & Life Support Calculator (NLA - New Lunar Accord)
-----------------------------------------------------------------
This tool calculates essential life support requirements (water, oxygen, food)
and energy consumption for lunar habitats, with dedicated modules for agricultural
yields based on the Brazilian Sector's Bio-Dome specifications.

Author: New Lunar Accord Initiative
License: MIT
"""

import sys
import argparserequired = False

# Base daily human consumption estimates (average adult under 1/6th gravity conditions)
O2_PER_HUMAN_KG_DAY = 0.84       # kg of O2 per person/day
WATER_PER_HUMAN_L_DAY = 3.0      # Liters of hydration & basic hygiene/day
FOOD_PER_HUMAN_KG_DAY = 0.62     # kg of dry food equivalent/day
POWER_PER_HUMAN_KW = 1.2         # kW continuous life support requirement per person

# Brazilian Sector Agro-Dome Efficiency Standards (Hydroponic / Vertical Farming)
O2_PRODUCTION_PER_SQM_DAY = 0.15 # kg of O2 produced per m² of crop area/day
WATER_RECYCLING_EFFICIENCY = 0.92 # 92% efficiency in closed-loop water recovery


def calculate_base_requirements(crew_size: int, duration_days: int) -> dict:
    """Calculates total base resources needed for a given crew and duration."""
    total_o2_kg = crew_size * O2_PER_HUMAN_KG_DAY * duration_days
    total_water_l = crew_size * WATER_PER_HUMAN_L_DAY * duration_days
    total_food_kg = crew_size * FOOD_PER_HUMAN_KG_DAY * duration_days
    total_power_kwh = crew_size * POWER_PER_HUMAN_KW * 24 * duration_days

    # Adjusted water demand considering closed-loop recycling
    fresh_water_needed_l = total_water_l * (1.0 - WATER_RECYCLING_EFFICIENCY)

    return {
        "crew_size": crew_size,
        "duration_days": duration_days,
        "total_o2_kg": round(total_o2_kg, 2),
        "total_water_gross_l": round(total_water_l, 2),
        "fresh_water_required_l": round(fresh_water_needed_l, 2),
        "total_food_kg": round(total_food_kg, 2),
        "total_power_kwh": round(total_power_kwh, 2),
    }


def calculate_brazilian_sector_biodome(crew_size: int) -> dict:
    """
    Calculates the required greenhouse/biodome surface area (in sq meters)
    to achieve 100% O2 self-sufficiency for the base using Brazilian Sector standards.
    """
    daily_o2_demand_kg = crew_size * O2_PER_HUMAN_KG_DAY
    required_dome_area_sqm = daily_o2_demand_kg / O2_PRODUCTION_PER_SQM_DAY

    # Regolith processing estimate for water/ice extraction (approx. 50kg regolith per liter of H2O in ice-rich polar areas)
    daily_ice_regolith_kg = (crew_size * WATER_PER_HUMAN_L_DAY * (1.0 - WATER_RECYCLING_EFFICIENCY)) * 50.0

    return {
        "daily_o2_demand_kg": round(daily_o2_demand_kg, 2),
        "required_greenhouse_area_sqm": round(required_dome_area_sqm, 2),
        "daily_regolith_mining_for_water_kg": round(daily_ice_regolith_kg, 2),
    }


def print_report(res: dict, bio: dict):
    """Prints a formatted report to the terminal."""
    print("===============================================================")
    print("          NEW LUNAR ACCORD (NLA) - RESOURCE REPORT             ")
    print("===============================================================")
    print(f" Mission Duration : {res['duration_days']} Days")
    print(f" Personnel Count  : {res['crew_size']} Crew Members")
    print("---------------------------------------------------------------")
    print(" [CONSUMPTION FORECAST]")
    print(f" - Oxygen (O2) Needed   : {res['total_o2_kg']:>10.2f} kg")
    print(f" - Gross Water Demand   : {res['total_water_gross_l']:>10.2f} L")
    print(f" - Fresh Water (Makeup) : {res['fresh_water_required_l']:>10.2f} L  (with 92% recovery)")
    print(f" - Food Requirements    : {res['total_food_kg']:>10.2f} kg")
    print(f" - Base Power Required  : {res['total_power_kwh']:>10.2f} kWh")
    print("---------------------------------------------------------------")
    print(" [SECTOR BRAZIL - BIOSPHERE & AGRO-DOME SPECIFICATIONS]")
    print(f" - Required Crop Surface: {bio['required_greenhouse_area_sqm']:>10.2f} m² (For 100% O2 Loop)")
    print(f" - Polar Regolith Processing: {bio['daily_regolith_mining_for_water_kg']:>8.2f} kg/day (Water Extraction)")
    print("===============================================================")


def main():
    parser = argparse.ArgumentParser(
        description="NLA Lunar Resource & Life Support Calculator"
    )
    parser.add_argument(
        "-c", "--crew", type=int, default=12, help="Number of crew members (default: 12)"
    )
    parser.add_argument(
        "-d", "--days", type=int, default=30, help="Mission duration in days (default: 30)"
    )

    args = parser.parse_args()

    resource_data = calculate_base_requirements(args.crew, args.days)
    biodome_data = calculate_brazilian_sector_biodome(args.crew)

    print_report(resource_data, biodome_data)


if __name__ == "__main__":
    main()
