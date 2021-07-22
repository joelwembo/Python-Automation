# select depart date
datepicker = driver.find_element_by_id("departure-date-selector")
actions.move_to_element(datepicker).click().perform()

# find the calendar, month and year picker and the current date
calendar = driver.find_element_by_id("departureDateContainer")
month_picker = Select(calendar.find_element_by_class_name("ui-datepicker-month"))
year_picker = Select(calendar.find_element_by_class_name("ui-datepicker-year"))
current_date = calendar.find_element_by_class_name("ui-datepicker-current-day")

# printing out current date
month = month_picker.first_selected_option.text
year = year_picker.first_selected_option.text
print("Current departure date: {day} {month} {year}".format(day=current_date.text, month=month, year=year))

# see if we have an available date in this month
try:
    next_available_date = current_date.find_element_by_xpath("following::td[@data-handler='selectDay' and ancestor::div/@id='departureDateContainer']")
    print("Found an available departure date: {day} {month} {year}".format(day=next_available_date.text, month=month, year=year))
    next_available_date.click()
except NoSuchElementException:
# looping over until the next available date found
        while True:
# click next, if not found, select the next year
            try:
                calendar.find_element_by_class_name("ui-datepicker-next").click()
            except NoSuchElementException:
# select next year
                year = Select(calendar.find_element_by_class_name("ui-datepicker-year"))
                year.select_by_visible_text(str(int(year.first_selected_option.text) + 1))

# reporting current processed month and year
                month = Select(calendar.find_element_by_class_name("ui-datepicker-month")).first_selected_option.text
                year = Select(calendar.find_element_by_class_name("ui-datepicker-year")).first_selected_option.text
                print("Processing {month} {year}".format(month=month, year=year))

            try:
                next_available_date = calendar.find_element_by_xpath(".//td[@data-handler='selectDay']")
                print("Found an available departure date: {day} {month} {year}".format(day=next_available_date.text, month=month, year=year))
                next_available_date.click()
                break
            except NoSuchElementException:
                continue
python
