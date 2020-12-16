Feature: Без адаптера
  Scenario: Проходит
    Given circle r=10, hole r=12
  Scenario: Не проходит
    Given circle r=15, hole r=12
  Scenario: Проходит с адаптером
    Given area x=4, y=5, hole r=12
  Scenario: Не проходит с адаптером
    Given area x=20, y=18, hole r=12