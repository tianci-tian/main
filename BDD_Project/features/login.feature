Feature: 用户登录功能

  Scenario: 成功登录
    Given 用户在登录页面
    When 用户输入有效的用户名和密码
    Then 用户应看到主页

  Scenario: 登录失败
    Given 用户在登录页面
    When 用户输入无效的用户名和密码
    Then 用户应看到错误消息


