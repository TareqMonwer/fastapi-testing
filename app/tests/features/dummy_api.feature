Feature: Showing off behave

  Scenario: Run a simple test
    Given the web server is running
    When requesting for endpoint get_dummy_models
    Then a 200 status code should be received