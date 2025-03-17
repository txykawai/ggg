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

        # 应用有一个输入待办事项的文本输入框
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy flowers')

        # 他按下回车键后，页面更新了
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)  # 等待页面更新

        # 他访问那个URL，发现他的待办事项列表还在
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy flowers' for row in rows),
            "New to-do item did not appear in table"
        )

        # 他满意的离开了
        self.fail('Finish the test!')

if __name__ == '__main__':
    # 运行测试
    unittest.main(warnings='ignore')