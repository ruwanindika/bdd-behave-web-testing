from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options 


@given(u'launch chrome browser')
def step_impl(context):
    
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    
    options.headless = True
    context.driver=webdriver.Chrome(options=options)

@when(u'open DevOps1 page')
def step_impl(context):
    context.driver.get('https://devops1.com.au/')
    context.driver.maximize_window()

@then(u'verify the logo is present on the page')
def step_impl(context):
    status = context.driver.find_element(By.XPATH,'//img[@src="/assets/img/logos/devops1-logo.svg"]').is_displayed()
    # status = context.driver.find_element(By.XPATH,'/html/body/header-component/header/nav/div/a/img').is_displayed()
    assert status is True

@then(u'close the browser')
def step_impl(context):
    context.driver.close()

@then(u'Click "Contact us" button')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//div[@class="column navbar-actions"]//a[@class="btn btn-primary"]').click()
    # context.driver.find_element(By.XPATH,'/html/body/header-component/header/nav/div/div/div[2]/a[2]').click()

@then(u'verify the contact us page title is present')
def step_impl(context):
    linkText = context.driver.find_element(By.XPATH,'//div[@class="contact-form"]//h2[@class="form-title"]').text
    # linkText = context.driver.find_element(By.XPATH,'/html/body/section[1]/div/div/div[2]/div/h2').text
    assert linkText == "Get in touch"

@then(u'click on the services dropdown')
def step_impl(context):
    toggle_link = context.driver.find_element(By.CSS_SELECTOR,'.nav-link.dropdown-toggle')
    toggle_link.click()
    
@then(u'check for 5 items in the list')
def step_impl(context):
    item_list = []
    service_list = context.driver.find_element(By.CSS_SELECTOR,'.dropdown-menu.show')
    
    for i in (service_list.text).splitlines():
        item_list.append(i)
    assert item_list == ['All Services', 'Platform Engineering', 'Security Engineering', 'Quality and Observability', 'Engagement models']

@then(u'Click on All Services')
def step_impl(context):
    dropdown_link = context.driver.find_element(By.XPATH,'//a[@class="dropdown-item" and text()="All Services"]')
    # dropdown_link = context.driver.find_element(By.XPATH,'/html/body/header-component/header/nav/div/div/div[1]/ul/li[1]/ul/li[1]/a')
    dropdown_link.click()

@then(u'"Uplifting engineering practices" is present in the page')
def step_impl(context):
    title_one = context.driver.find_element(By.CSS_SELECTOR,'.display-1').text
    assert title_one == "Uplifting engineering practices"

@then(u'check for "Platform Engineering" card')
def step_impl(context):
    card_title_text = context.driver.find_element(By.XPATH,'//div[@class="card-body"]//h3[@class="card-title text-white"]').text
    # card_title_text = context.driver.find_element(By.XPATH,'//*[@id="services"]/div/div[2]/div[1]/div[1]/h3').text

    assert card_title_text == "Platform Engineering"

@then(u'click on the platform engineering link')
def step_impl(context):
    context.driver.execute_script('window.scrollBy(0, 1000)')
    # context.driver.implicitly_wait(5)
    # our_services_link = context.driver.find_element(By.XPATH,'//div[@class="feature-grid"]/div[1]/div[2]/a')
    our_services_link = context.driver.find_element(By.XPATH,'//div[@class="feature-grid"]//child::div[1]//div[@class="card-footer text-white"]//a[@class="btn btn-link btn-arrow"]')
    ActionChains(context.driver).click(our_services_link).perform()
    
@then(u'check for text "Platform Engineering"')
def step_impl(context):
    services_page_title = context.driver.find_element(By.XPATH,'//div[@class="hero-content"]//h1[@class="display-1 text-white"]').text
    assert services_page_title == "Empowering innovation with solid engineering"

@then(u'get hero items list')
def step_impl(context):
    hero_title_list_class_one = context.driver.find_elements(By.XPATH,'//div[@class="hero-tile"]//p[@class="text-large text-white"]')
    hero_title_list_class_two = context.driver.find_elements(By.XPATH,'//div[@class="hero-tile fade-in"]//p[@class="text-large text-white"]')
    hero_item_list = []

    for i in hero_title_list_class_one:
        hero_item_list.append(i.get_attribute('innerHTML'))

    for j in hero_title_list_class_two:
        hero_item_list.append(j.get_attribute('innerHTML'))

    hero_item_list_from_page = ['Build Fearlessly: Engineer secure experiences for your customers at scale.\n            ',
                                'Engineer high-quality products by leveraging data-driven decision-making,\n              and seamless integration.',
                                'AI powered cloud and platform solutions to enhance your build teams\n              velocity and efficiency']
    
    assert hero_item_list_from_page == hero_item_list


@then(u'check for 3 items in the list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then check for 3 items in the list')