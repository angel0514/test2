import allure


class TestLogin:

    @allure.step("这是测试步骤一")
    def test_a(self):
        print("\n1111")
        assert 1

    @allure.step("这是测试步骤二")
    def test_b(self):
        print("\n2222")
        allure.attach("描述1","判断失败")
        assert 0
