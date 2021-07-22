from datetime import datetime, timedelta

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def select_date(calendar, mininum_date=None):
    try:
        # check if "Your Date" is there
        your_date_elm = calendar.find_element_by_class_name("your-date")

        your_date = your_date_elm.get_attribute("data-date")
        print("Found 'Your Date': " + your_date)
        your_date_elm.click()

        # check if your_date against the minimum date if given
        your_date = datetime.strptime(your_date, "%Y-%m-%d")
        if mininum_date and your_date < mininum_date:
            raise NoSuchElementException("Minimum date violation")
        return your_date
    except NoSuchElementException:
        flight_date = None
        flight_date_elm = None
        while True:
            print("Processing " + calendar.find_element_by_css_selector("div.subheader > p").text)

            try:
                if mininum_date:
                    flight_date_elms = calendar.find_elements_by_class_name("flights")
                    flight_date_elm = next(flight_date_elm for flight_date_elm in flight_date_elms
                                           if datetime.strptime(flight_date_elm.get_attribute("data-date"), "%Y-%m-%d") >= mininum_date)
                else:
                    flight_date_elm = calendar.find_element_by_class_name("flights")
            except (StopIteration, NoSuchElementException):
                calendar.find_element_by_partial_link_text("Next month").click()

            # if found - print out the date, click and exit the loop
            if flight_date_elm:
                flight_date = flight_date_elm.get_attribute("data-date")
                print("Found 'Flight Date': " + flight_date)
                flight_date_elm.click()
                break

        return datetime.strptime(flight_date, "%Y-%m-%d")


driver = webdriver.Firefox()
driver.get("http://www.jet2.com/cheap-flights/leeds-bradford/antalya/2016-03-01/2016-04-12?adults=2&children=2&infants=1&childages=4%2c6")

wait = WebDriverWait(driver, 10)

# get the outbound date
outbound = wait.until(EC.visibility_of_element_located((By.ID, "outboundsearchresults")))
outbound_date = select_date(outbound)

# get the inbound date
inbound = driver.find_element_by_id("inboundsearchresults")
inbound_minimum_date = outbound_date + timedelta(days=7)
inbound_date = select_date(inbound, mininum_date=inbound_minimum_date)

print(outbound_date, inbound_date)

driver.close()
