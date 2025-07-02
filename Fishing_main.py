import os
import time
from PIL import Image
BLUE = "\033[34m"
LIGHT_RED = "\033[38;5;197m"
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
ORANGE = "\033[38;5;208m"

max_trips=30
place1 = {str(i): f"Fishing/Places/place1_{i}.txt" for i in range(1, max_trips+1)} #Psatha
place2 = {str(i): f"Fishing/Places/place2_{i}.txt" for i in range(1, max_trips+1)} #Rocks below Alkyonides
place3 = {str(i): f"Fishing/Places/place3_{i}.txt" for i in range(1, max_trips+1)} #Rocks left of Sterna
place4 = {str(i): f"Fishing/Places/place4_{i}.txt" for i in range(1, max_trips+1)} #Agios Vasilios
place5 = {str(i): f"Fishing/Places/place5_{i}.txt" for i in range(1, max_trips+1)} #Porto Germeno

place1_images = {
    "1": ["Fishing/Images/IMG-80228dcffa813ad34957b11eba48b94a-V.jpg", "Fishing/Images/IMG20250619235703.jpg"],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": [],
    "10": [],
    "11": [],
    "12": [],
    "13": [],
    "14": [],
    "15": [],
    "16": [],
    "17": [],
    "18": [],
    "19": [],
    "20": [],
    "21": [],
    "22": [],
    "23": [],
    "24": [],
    "25": [],
    "26": [],
    "27": [],
    "28": [],
    "29": [],
    "30": []
}
place2_images = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": [],
    "10": [],
    "11": [],
    "12": [],
    "13": [],
    "14": [],
    "15": [],
    "16": [],
    "17": [],
    "18": [],
    "19": [],
    "20": [],
    "21": [],
    "22": [],
    "23": [],
    "24": [],
    "25": [],
    "26": [],
    "27": [],
    "28": [],
    "29": [],
    "30": []
}
place3_images = {
    "1": ["Fishing/Images/IMG20250609210910.jpg", "Fishing/Images/IMG20250609210919.jpg"],
    "2": ["Fishing/Images/IMG20250629080445.jpg", "Fishing/Images/IMG20250629080455.jpg", "Fishing/Images/IMG20250629091141.jpg", "Fishing/Images/IMG20250629091152.jpg", "Fishing/Images/IMG20250629120054.jpg", "Fishing/Images/IMG20250629120722.jpg", "Fishing/Images/IMG20250629121437.jpg", "Fishing/Images/IMG20250629121445.jpg", "Fishing/Images/IMG20250629144636.jpg"],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": [],
    "10": [],
    "11": [],
    "12": [],
    "13": [],
    "14": [],
    "15": [],
    "16": [],
    "17": [],
    "18": [],
    "19": [],
    "20": [],
    "21": [],
    "22": [],
    "23": [],
    "24": [],
    "25": [],
    "26": [],
    "27": [],
    "28": [],
    "29": [],
    "30": []
}
place4_images = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": [],
    "10": [],
    "11": [],
    "12": [],
    "13": [],
    "14": [],
    "15": [],
    "16": [],
    "17": [],
    "18": [],
    "19": [],
    "20": [],
    "21": [],
    "22": [],
    "23": [],
    "24": [],
    "25": [],
    "26": [],
    "27": [],
    "28": [],
    "29": [],
    "30": []
}
place5_images = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": [],
    "10": [],
    "11": [],
    "12": [],
    "13": [],
    "14": [],
    "15": [],
    "16": [],
    "17": [],
    "18": [],
    "19": [],
    "20": [],
    "21": [],
    "22": [],
    "23": [],
    "24": [],
    "25": [],
    "26": [],
    "27": [],
    "28": [],
    "29": [],
    "30": []
}

Fishing={"1":place1,
         "2":place2,
         "3":place3,
         "4":place4,
         "5":place5}

Fishing_images={"1":place1_images,
                "2":place2_images,
                "3":place3_images,
                "4":place4_images,
                "5":place5_images}

def clear_terminal():
    os.system('cls')

def find_fishing_trip(AA,BB,mt):
    while True:
        clear_terminal()
        print(f"{ORANGE}Select the location where the fishing trip took place:{RESET}")
        print(f"1. Psatha")
        print(f"2. Rocks below Alkyonides")
        print(f"3. Rocks left of Sterna")
        print(f"4. Agios Vasilios")
        print(f"5. Porto Germeno")
        print(f"0. Return to the main MENU")
        choice=input(f"{BLUE}Make a choice: {RESET}")
        while choice not in ["0","1","2","3","4","5"]:
            print(f"{RED}Invalid choice, try again{RESET}")
            choice=input(f"{BLUE}Make a choice: {RESET}")
        if choice != "0" :
            try:
                i=0
                for j in range(1,mt+1):
                    j=str(j)
                    if os.path.getsize(AA[choice][j]) != 0:
                        i+=1
                choice=str(choice)
                if i!=0:
                    clear_terminal()
                    print(f"{ORANGE}There are {i} saved fishing trips for this location{RESET}")
                    for j in range(i):
                        with open(AA[choice][str(j+1)],"r",encoding="utf-8") as file:
                            info = file.readline().strip().replace("Date/Time :", "").strip().split(",")[0].strip()
                        print(f"{j+1}. {info}")
                    print(f"{BLUE}Press a number from 1-{i} to view info about the corresponding trip{RESET}") 
                    choice1=input(f"{BLUE}Make a choice: {RESET}")
                    while choice1 not in map(str,range(1,i+1)) :
                        print(f"{RED}Invalid choice, try again{RESET}")
                        choice1=input(f"{BLUE}Make a choice: {RESET}")
                    x="a"
                    while x!="":
                        clear_terminal()
                        print(f"{ORANGE}Πληροφοριες για το ψαρεμα:{RESET}")
                        with open(AA[choice][choice1],"r",encoding="utf-8") as file:
                            print(file.read())
                        print(" ")
                        if isinstance(BB[choice][choice1], list) and len(BB[choice][choice1]) > 0:
                            print(f"{GREEN}There are {len(BB[choice][choice1])} photos from this trip")
                            for j in range(len(BB[choice][choice1])):
                                x=input(F"{GREEN}Press << ENTER >> to see a photo from this trip, or << 1 >> to skip the photos: {RESET}")
                                while x not in ["","1"]:
                                    print(f"{RED}Invalid choice, try again{RESET}")
                                    x=input(F"{GREEN}Press << ENTER >> to see a photo from this trip, or << 1 >> to skip the photos: {RESET}")
                                if x=="1":
                                    break
                                img = Image.open(BB[choice][choice1][j])
                                img.show()
                        if int(choice1)==i:
                            x=input(F"{GREEN}Press << ENTER >> to return to the MENU: {RESET}")
                        else:
                            x=input(F"{GREEN}Press << ENTER >> to return to the MENU or << 1 >> to view info about the next fishing trip in this place: {RESET}")
                            while x not in ["","1"]:
                                print(f"{RED}Invalid choice, try again{RESET}")
                                x=input(F"{GREEN}Press << ENTER >> to return to the MENU or << 1 >> to view info about the next fishing trip in this place: {RESET}")
                            choice1=str(int(choice1)+1)
                else:
                    print(" ")
                    print(F"{RED}No fishing trips saved for this location, choose another{RESET}")
                    time.sleep(2)
            except FileNotFoundError:
                print(f"{RED}A FILE DOES NOT EXIST{RESET}")
                time.sleep(2)
        else:
            break

def add_fishing_trip(AA,BB,mt):
    clear_terminal()
    print(f"{ORANGE}Select the location where the fishing trip took place:{RESET}")
    print(f"1. Psatha")
    print(f"2. Rocks below Alkyonides")
    print(f"3. Rocks left of Sterna")
    print(f"4. Agios Vasilios")
    print(f"5. Porto Germeno")
    print(f"If the location is not in the MENU, press << 0 >> to return to the main MENU")
    choice=input(f"{BLUE}Make a choice: {RESET}")
    while choice not in ["0","1","2","3","4","5"]:
            print(f"{RED}Invalid choice, try again{RESET}")
            choice=input(f"{BLUE}Make a choice: {RESET}")
    if choice != "0":
        try:
            i=1
            for j in range(1,mt+1):
                j=str(j)
                if os.path.getsize(AA[choice][j]) != 0:
                    i+=1
            i=str(i)
            choice=str(choice)
            clear_terminal()
            date="Date/Time : "+input(F"{BLUE}When did the fishing take place (day/month/year , start time-->end time): {RESET}")
            weather="\nWeather : "+input(F"{BLUE}Describe the weather (e.g. wind, waves, temperature, rain, pressure, moon, clouds): {RESET}")
            fish="\nFish : "+input(F"{BLUE}What fish were caught, how many kilos: {RESET}")
            extra="\nComments : "+input(F"{BLUE}Add any comments if you'd like: {RESET}")
            with open(AA[choice][i],"a",encoding="utf-8") as file:
                file.write(date)
                file.write(weather)
                file.write(fish)
                file.write(extra)
            print(F"{GREEN}The information for this fishing trip was saved{RESET}")
            time.sleep(2)
        except FileNotFoundError:
            print(f"{RED}A FILE DOES NOT EXIST{RESET}")
            time.sleep(2)

def main():
    while True:
        clear_terminal()
        print(f"{ORANGE}Menu{RESET}")
        print(f"1. Find previous fishing trips")
        print(f"2. Add a fishing trip")
        print(f"3. Exit program")
        choice=input(f"{BLUE}Make a choice: {RESET}")
        while choice not in ["1","2","3"]:
            print(f"{RED}Invalid choice, try again{RESET}")
            choice=input(f"{BLUE}Make a choice: {RESET}")
        choice=int(choice)
        print(" ")
        if choice == 3 :
            print(F"{LIGHT_RED}EXITING PROGRAM{RESET}")
            break
        elif choice == 1:
            find_fishing_trip(Fishing,Fishing_images,max_trips)
        elif choice == 2:
            add_fishing_trip(Fishing,Fishing_images,max_trips)


if __name__=="__main__":
    main()
