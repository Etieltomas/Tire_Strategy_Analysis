# Tire Strategy Analysis Tool

This project provides a **Tire Strategy Analysis Tool** for visualizing and comparing tire strategies employed by drivers during a Formula 1 race. The tool generates a horizontal bar chart showing the number of laps completed on each tire compound for each driver, offering insights into their stint strategies.

## Features

- **Tire Compound Analysis**: Displays stint durations for each tire compound used by drivers.
- **Driver-Specific Visualization**: Groups data by driver and shows cumulative stint lengths.
- **Customizable Color Coding**: Differentiates tire compounds using distinct colors.
- **Interactive Input**: Allows users to specify the race year and location dynamically.

## Technologies Used

- **FastF1**: Fetches and processes Formula 1 telemetry and race data.
- **Matplotlib**: Visualizes tire strategies as horizontal bar charts.
- **Pandas**: Organizes and manipulates stint data for analysis.
- **Python**: Serves as the backend for data processing and visualization.

## Usage

1. Clone the repository and ensure Python 3.x is installed.
2. Install dependencies using:
   ```bash
   pip install fastf1 matplotlib pandas numpy
3. Run the script:
   ```bash
   python3 main.py
4. Provide the required inputs:
  - **Year**: Specify the race year (e.g., `2023`).
  - **Race**: Enter the name of the race (e.g., `Monaco`).

5. View the resulting bar chart:
  - Horizontal bars represent stint durations.
  - Colors correspond to tire compounds:
    - **Yellow**: Medium
    - **White**: Hard
    - **Red**: Soft
    - **Pink**: Hypersoft
    - **Green**: Intermediate
    - **Blue**: Wet
    - **Gray**: Unknown compound
