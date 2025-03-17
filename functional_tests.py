from selenium import webdriver

# (1) 从 selenium 引入 webdriver
# (2) 启动一个 Selenium WebDriver 去弹出一个 Chrome 窗口
browser = webdriver.Chrome()

# (3) 打开本地网页
browser.get('http://localhost:8000')

# (4) 测试断言，检查网页中是否包含“Django”这个词
assert 'Django' in browser.page_source

# 关闭浏览器
browser.quit()