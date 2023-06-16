Feature: get requests validations

  Scenario: get all users
    Given user sets baseUrl
    When user sends get request
    Then user gets status code 200

    Scenario: get Single User
      Given user sets baseUrl
      When user sends get request for a specific user
      Then user gets a response body with requested details
