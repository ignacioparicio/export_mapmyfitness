# About
A script to automatically export fitness workouts from Under Armour's map my fitness,
in `TCX` format.

# Workflow
1. Download `csv` with links to all individual workouts from https://www.mapmyfitness.
   com/workout/export/csv
   
2. Place `csv` in the `data/` folder
3. Get a suitable version of `chromedriver`
4. Execute script `main.py`
5. Upon webdriver opening, type username and password on [mapmyfitness.com]
   (https://www.mapmyfitness.com). Change `downloads` folder, if desired
   
6. Press `enter` to continue execution and download a `TCX` file for each individual 
   workout