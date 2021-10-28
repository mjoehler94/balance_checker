# uta_selenium.com ---------

# libraries
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# local modules
from slack_utils import SlackEngine
from secrets import my_secrets, slack_token

alert_level = 10
remind_to_reimburse_amount = 50
reimburse_url = "https://progleasing.service-now.com/prognation?id=sc_cat_item&sys_id=448ba5bb1361fe00d9ff30ded144b041"


def main():
    # TODO: try to do it as a headless scrape (doesn't need to open browser)

    # initializing chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # https://chromedriver.chromium.org/downloads
    driver_path = "driver/chromedriver.exe"
    driver = webdriver.Chrome(driver_path, options=chrome_options)
    url = "https://farepay.rideuta.com/"

    try:
        driver.get(url)
        time.sleep(1)

        username = driver.find_element_by_id("username")
        password = driver.find_element_by_name("j_password")

        username.send_keys(my_secrets["email"])
        password.send_keys(my_secrets["password"])
        password.send_keys(Keys.RETURN)

        time.sleep(3)
        balance = driver.find_element(By.XPATH, "//table/tbody/tr[2]/td[3]")
        current_balance = str(balance.text)
    except:
        current_balance = None
        message = ":x: Could not retreive UTA card balance."
    finally:
        driver.quit()

    if current_balance:
        numeric_balance = float(current_balance.split("$")[1])
        if numeric_balance <= alert_level:
            message = f":warning: UTA Card Balance: {current_balance}"
            # TODO: add link to refill balance to message
        elif numeric_balance >= remind_to_reimburse_amount:
            message = f":white_check_mark: UTA Card Balance: {current_balance}"
            message += (
                f"\nDon't forget to submit your <{reimburse_url}|reimbursement request>"
            )
        else:
            message = f":white_check_mark: UTA Card Balance: {current_balance}"

    slack_bot = SlackEngine(
        job_name="UTA Card Balance Checker",
        job_emoji=":steam_locomotive:",
        api_token=slack_token,
    )
    slack_bot.send_message(group=["@matthew.oehler"], message=message)
    print("Done")


if __name__ == "__main__":
    main()
