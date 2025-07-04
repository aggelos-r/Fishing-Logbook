# Fishing Logbook

This is a simple terminal-based fishing logbook application written in Python.

It allows you to record fishing trips by location. For each trip, you can log the date and time, weather conditions, fish species and quantity, as well as any personal comments.  
You can also browse previous fishing trips and view any associated images if available.

---

## Features

- Five predefined fishing locations (you can rename them):
  - Fishing_place_1
  - Fishing_place_2
  - Fishing_place_3
  - Fishing_place_4
  - Fishing_place_5

- Record for each trip:
  - Date and time
  - Weather conditions
  - Fish species and quantity
  - Personal comments

- Browse previous trips:
  - View summaries and details
  - Display photos (uses Pillow)

- Simple terminal interface with:
  - Input validation
  - Color-coded output
  - Handles missing or empty files gracefully

---

## Requirements & Installation

- Python 3.6 or later
- Pillow library for image viewing

To install Pillow:

    pip install pillow

---

## Folder Structure

Your project folder should look like this:

Fishing/  
├── Places/  → Contains files like place1_1.txt, place1_2.txt, ..., place5_30.txt  
├── Images/  → Contains your image files  
├── your_script.py → Your main Python script

Example code to create the `.txt` files:

    from pathlib import Path

    def create_place_files():
        base_path = Path("Fishing/Places")
        base_path.mkdir(parents=True, exist_ok=True)

        for x in range(1, 6):
            for i in range(1, 31):
                file_path = base_path / f"place{x}_{i}.txt"
                file_path.touch(exist_ok=True)
                print(f"Created: {file_path}")

    if __name__ == "__main__":
        create_place_files()

---

## Adding Photos

Photos are added manually in your code using dictionaries.

Example:  
Add one photo for Fishing_place_1, trip #3:

    place1_images["3"].append("Images/photo1.jpg")

Add multiple photos:

    place1_images["3"].extend(["Images/photo1.jpg", "Images/photo2.jpg"])

Make sure the photos are in the `Images/` folder and the paths match.

---

## How to Use

1. Clone or download the project.
2. Open terminal and navigate to project folder.
3. Run:

    python your_script.py

4. Use menu to add trips, browse trips, or view photos.
