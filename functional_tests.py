from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # 在每个测试方法运行之前执行
        self.browser = webdriver.Chrome()

    def tearDown(self):
        # 在每个测试方法运行之后执行
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 张三听说有一个在线待办事项的应用
        # 他去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 他注意到网页的标题包含 "To-Do" 这个词
        self.assertIn('To-Do', self.browser.title, "Browser title was: " + self.browser.title)
        self.fail('Finish the test!')

        # 应用有一个输入待办事项的文本输入框
        
        # 他按下回车键后，页面更新了

        # 他访问那个URL，发现他的待办事项列表还在

        # 他满意的离开了

if __name__ == '__main__':
    # 运行测试
    unittest.main()