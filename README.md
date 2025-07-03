# Fishing Logbook

This is a simple terminal-based fishing logbook application written in Python.

It allows users to record fishing trips by location. For each trip, you can log the date and time, weather conditions, fish species and quantity, as well as any personal comments.

You can also browse previous fishing trips and view any associated images from each trip if available.

## Features

The app covers five predefined fishing locations that you can rename depending on the places you fish:

- Fishing_place_1  
- Fishing_place_2  
- Fishing_place_3 
- Fishing_place_4
- Fishing_place_5

It supports photo viewing via the Pillow library. All fishing trip information is saved in organized text files per trip and location. To add photos, you need to manually place them in the correct spot of the corresponding dictionary. The picture dictionaries are created by the program. To add a photo, for example, in the first fishing place for the third trip, you use: place1_images["3"].append("photo1.jpg"). To add multiple photos at once, you use: place1_images["3"].extend(["photo1.jpg", "photo2.jpg"]).

The interface is simple and terminal-based, with input validation and color-coded output for better readability.

## Requirements & Installation

You need Python 3.6 or later and the Pillow library for image viewing.

To install Pillow, open your terminal and run:

```bash
pip install pillow
```

That’s all you need to get started.

## Folder Structure

Make sure your folders look like this:

```
Fishing/
├── Places/        # contains files like place1_1.txt, place1_2.txt, ..... , place5_30.txt
├── Images/        # contains your image files
```

**Use this code to easily create the files for each place.:

        from pathlib import Path

        def create_place_files():
            base_path = Path("**YOUR FILE PATH**")
            base_path.mkdir(parents=True, exist_ok=True)

            for i in range(1, 31):
                file_path = base_path / f"placeX_{i}.txt"
                file_path.touch(exist_ok=True) 
                print(f"Created: {file_path}")

        if __name__ == "__main__":
            create_place_files()


Each `placeX_Y.txt` file corresponds to trip number Y at location X.

## How to Use

1. Download or clone the project.
2. Open your terminal and go to the project directory.
3. Run the Python script with:

```bash
python your_script_name.py
```

4. Use the main menu to add new fishing trips, browse existing trips, or view associated images.

## Notes

- All trips are saved as text files in the `Places` folder.  
- Photos should be placed in the `Images` folder and referenced properly in the code.  
- The app handles missing or empty files without crashing.  
- File names and paths must match the naming conventions used in the script.

## License

This project is open-source and free to use. Attribution is appreciated.
