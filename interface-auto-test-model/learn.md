# 自动化+报告框架：功能、结构和依赖关系


# ./Config
###  /globalConfig.py
定义各种配置设置，如文件路径、数据库信息和账户凭证。
路径:定义用于存储测试数据、日志、报告和测试脚本的各种路径。
HTTP配置:构造HTTP请求url的详细信息。
数据库配置:MySQL, Redis和Cassandra数据库的连接细节。
通知:配置通过钉钉发送通知的URL。
服务器URL:访问自动化测试服务器的URL。
# ./src
### /public
###### /ddtInput.py
自动化测试框架中数据驱动测试(DDT)功能组件
根据一个特定的标志(TestCaseFlag)从一个Excel文件中过滤和检索测试用例。
利用ReadTestData模块读取和处理测试数据。

**方法**
类:EveryTestCaseFlag
这个类负责通过TestCaseFlag从提供的Excel文件中过滤测试用例。
方法:get_every_TestCaseFlag
这个方法过滤测试用例，只包括那些带有指定TestCaseFlag的用例。


**分析：**
导入:从ReadTestData模块导入ReadExcel类。
类EveryTestCaseFlag:处理基于TestCaseFlag的测试用例的初始化和过滤。
初始化:使用Excel文件名和TestCaseFlag进行初始化，并检索所有测试数据。
方法get_every_TestCaseFlag:过滤并返回与指定TestCaseFlag匹配的测试用例。
Main Block:演示如何通过打印所有测试数据和基于TestCaseFlag的过滤测试用例来使用这个类。
###### /dynamicData.py
用于从HTTP响应中提取动态数据，特别是cookie。
这个脚本定义了一个类dynamicData，它有一个从HTTP响应中提取cookie的方法。
利用HttpCommonRequest模块中的HttpRequests类来发送HTTP请求。

**分析**
如何从HTTP响应中提取cookie，这对于会话管理或后续请求需要身份验证cookie的场景非常有用

### /script
###### /test1.py
**分析**
目的:演示使用ddt模块的数据驱动测试。
测试类UnitTest:定义了使用特定TestCaseFlag值加载数据的测试方法。
Main块:使用unittest模块的测试运行器执行测试。
该脚本展示了如何使用DDT方法构建单元测试，从而允许测试由不同测试数据集定义的多个场景。


### /utils
###### /BeautifulReport.py
**分析**
测试结果处理:处理测试结果记录，包括成功、失败、错误和跳过。
报告生成:生成带有详细信息的HTML测试报告。
图像处理:提供在测试报告中嵌入图像的功能。
该脚本作为自动化测试结果生成和报告的综合模块，具有处理报告中的图像的附加特性。

###### /CassandraUtils.py
**分析**
用于与Cassandra数据库进行交互；
提供了一种方便和封装的方式来与Cassandra数据库交互，允许用户执行常见的数据库操作，如查询、插入、更新和删除数据。它还集成了错误日志记录，以方便调试和错误处理。

###### /DingDelivery.py
**分析**
负责向钉钉(钉钉)机器人发送消息

###### /EmailDelivery.py
**分析**

###### /GetLog.py
**分析**
用于为Python应用程序生成日志，' GetLog.py '提供了一种方便的方式来为Python应用程序生成日志。它允许记录到文件和控制台，并具有可定制的日志级别和格式。该脚本可以导入到其他Python文件中，从而可以轻松地将日志功能集成到各种项目中。
主要功能
1. **初始化**:初始化指定名称和日志级别的日志记录器。
2. **文件和控制台处理程序**:创建用于记录文件和控制台的处理程序。
3. **日志格式**:定义日志信息的格式。
4. **Logger Configuration**:使用处理程序配置Logger并设置其日志级别。
5. **日志生成**:在指定目录下生成以时间戳为名称的日志文件。

###### /HttpCommonRequest.py
**分析**
提供了一种常见的方式来发出HTTP请求
主要功能
1. **Initialization**:从全局配置中使用协议、主机和端口设置HTTP请求处理程序。
2. **请求发送**:' send_request '方法根据提供的数据发送HTTP请求，包括方法类型，URL，报头和有效负载。
3. **内容类型处理**:支持多种内容类型和方法，灵活处理不同类型的请求。
4. **错误处理**:捕获并打印在请求发送过程中发生的异常。

###### /Mock.py
**分析**
' Mock.py '使用' unittest. py '封装了mock功能。模拟的模块。它提供了一种方便的方法来模拟带有预定义返回值的函数调用，这对于测试目的很有用。该脚本可以集成到测试套件中，以模拟来自api或其他外部依赖项的响应，从而促进对各种场景的独立测试。

###### /MongoUtils原型.py
**分析**
用特定数据更新MongoDB集合的原型。它被设计用来更新MongoDB数据库中的项目、组织、帐户和产品信息。' update_project_info '函数用作生成假数据和更新数据库的入口点。
###### /MysqlUtils.py
**分析**
与MySQL数据库交互的实用程序
通过封装SELECT、INSERT、DELETE和UPDATE等常见操作，提供了一种方便的方式与MySQL数据库交互
###### /ReadTestData.py
**分析**
从Excel文件中读取测试数据
用于从Excel文件中读取测试数据，并将其转换为适合在自动化测试中使用的格式。
###### /RedisUtils.py
**分析**
与Redis数据库交互的实用程序;提供了一套全面的实用函数来与Redis数据库进行交互。它涵盖了Redis支持的各种数据类型，如字符串、哈希和列表，并包括设置、更新、检索和删除数据的操作。连接池的使用确保了对Redis服务器连接的有效管理，
# /run.py
**分析**
用来运行自动化测试
通过提供执行测试脚本和生成测试报告的统一接口来促进自动化测试的运行.使用BeautifulReport生成详细的测试报告，并通过钉钉发送这些报告。
# /run_threads.py
**分析**
利用多线程来执行测试





