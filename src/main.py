from selenium import webdriver
import pandas as pd
import time

workout_data = pd.read_csv("../data/user118862045_workout_history.csv")
workout_links = workout_data["Link"].to_list()

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(workout_links[0])
input(
    "Press enter once authenticated on mapmyfitness.com website and the "
    "downloads folder is changed to the desired location..."
)


for link in workout_links:
    time.sleep(2)

    driver.get(link)

    # TODO: implement more neatly with `WebDriverWait`
    time.sleep(10)

    # Buttons are given dynamic jss classes, but the button that leads to exports is
    # always the first one
    buttons = driver.find_elements_by_xpath("//button")
    buttons[0].click()

    driver.find_element_by_xpath("//*[contains(text(), 'Download as TCX')]").click()
