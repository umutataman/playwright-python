#noinspection NonAsciiCharacters
Feature: Flight Booking and Checkout

  Scenario: Book a flight from New York to Barcelona and complete the checkout process

    Given I am on the Kiwi.com website and accept cookies
    When I select a flight from "New York" to "Barcelona"
    And I set the departure date as "01-07-2023"
    And I set the return date as "01-07-2023"
    And I set the number of passengers as "2"
    And I click on the search button
    And I wait for the search results to load
    And I select the filter option for "Up to 1 stop" and excluding "United Kingdom"
    And I select any flight from the search results
    Then I verify that the selected flight has 1 stop
    When I click on the "Select" button for booking
    And I click "Continue as a guest" button
    And I complete the required fields on the checkout form page
      | Email            | Phone Number | Firstname | Lastname | Nationality   | Gender | Date of Birth | Passport Number | Passport Expire Date |
      | john@example.com | +1234567890  | John      | Doe      | United States | Male   | 18-05-1960    | ABC123456       | 21-03-2032           |
    And I remove second traveler button
    And I click on the "Continue" button