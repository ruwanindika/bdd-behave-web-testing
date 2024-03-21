Feature: DevOps1 webpage

Scenario: DevOps1 logo presence on the webpage - chrome browser
    Given launch chrome browser
    When open DevOps1 page
    Then verify the logo is present on the page
    And close the browser

Scenario: Contact us button presence on the webpage - chrome browser
    Given launch chrome browser
    When open DevOps1 page
    Then Click "Contact us" button
    Then verify the contact us page title is present
    And close the browser

Scenario: Services dropdown check All Services are present - chrome browser
    Given launch chrome browser
    When open DevOps1 page
    Then click on the services dropdown
    Then check for 5 items in the list
    And close the browser

Scenario: Services dropdown select All Services - chrome browser
    Given launch chrome browser
    When open DevOps1 page
    Then click on the services dropdown
    Then check for 5 items in the list
    Then Click on All Services
    Then "Uplifting engineering practices" is present in the page
    And close the browser

# Scenario: "Our services" link test "Platform Engineering" - chrome browser
#     Given launch chrome browser
#     When open DevOps1 page
#     Then check for "Platform Engineering" card
#     Then click on the platform engineering link
#     Then check for text "Platform Engineering"
#     And close the browser
