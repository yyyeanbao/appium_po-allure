

注意：

1、外层conftest.py千万不能删除

2、报告生成依赖allure open和server，所以报告无法单独打开

3、使用前需要配置环境变量，在cmd输入allure -v可以执行出结果



//成功生成报告，命令01----亲测可用

步骤1上下二选1：pytest ./testcase/test_demo.py --alluredir ./allure_results/ --clean-alluredir

步骤1上下二选1：pytest --alluredir=allure_results/ testcase/test_demo.py

步骤2：allure serve allure_results/

//成功生成报告，命令02 ----亲测可用

步骤1：pytest ./testcase/test_demo.py --alluredir ./allure_results/ --clean-alluredir

步骤2：allure generate -c -o ./allure_report/ ./allure_results/

步骤3：allure open ./allure_report/





