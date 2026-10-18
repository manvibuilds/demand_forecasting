
from pathlib import Path
import pandas as pd

# Project folders
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_FOLDER = PROJECT_ROOT / "data" / "raw"
PROCESSED_FOLDER = PROJECT_ROOT / "data" / "processed"

PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)

# Process each CSV file
for file in RAW_FOLDER.glob("*.csv"):
    df = pd.read_csv(file, low_memory=False)

    # Convert dates to datetime
    df["Date"] = pd.to_datetime(
    df["Date"],
    format="%d-%m-%Y %H:%M",
    errors="coerce"
)

    # Keep customer sales orders only
    df = df[df["Order Classification"] == "SO"].copy()

    # Count exact duplicates before removing them
    duplicate_count = df.duplicated().sum()

    # Remove exact duplicate rows
    df = df.drop_duplicates().copy()

    # Save the cleaned copy
    output_file = PROCESSED_FOLDER / f"{file.stem}_cleaned.csv"
    df.to_csv(output_file, index=False)

    print("\nFile:", file.name)
    print("Duplicate rows removed:", duplicate_count)
    print("Rows saved:", len(df))
    print("Saved to:", output_file)
