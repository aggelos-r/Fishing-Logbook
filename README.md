# Fishing Logbook

This is a simple terminal-based fishing logbook application written in Python.

It allows users to record fishing trips by location. For each trip, you can log the date and time, weather conditions, fish species and quantity, as well as any personal comments.

You can also browse previous fishing trips and view any associated images from each trip if available.

## Features

The app covers five predefined fishing locations:

- Psatha  
- Rocks below Alkyonides  
- Rocks left of Sterna  
- Agios Vasilios  
- Porto Germeno

It supports photo viewing via the Pillow library. All fishing trip information is saved in organized text files per trip and location.

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
├── Places/        # contains files like place1_1.txt, place1_2.txt, … place5_30.txt
├── Images/        # contains your image files
```

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

This project is open-source and free to use. Attribution is appreciated but not required.
