import pytest
from dotenv import load_dotenv
from alumnium import Alumni
from selenium.webdriver import Chrome

load_dotenv()

@pytest.fixture(scope="function")
def al():
    driver = Chrome()
    driver.get("https://duckduckgo.com")
    alumni = Alumni(driver)
    yield alumni
    driver.quit()

def test_search_with_selenium(al):
    al.do("type 'selenium' into the search field, then press 'Enter'")
    al.check("page title contains selenium")
    al.check("search results contain selenium.dev")
    assert al.get("atomic number") == 34