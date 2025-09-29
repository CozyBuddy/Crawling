from pywinauto.application import Application
import time
# 프로그램 실행
app = Application(backend="uia").start(r"C:\Program Files (x86)\Battle.net\Battle.net.exe")


time.sleep(4)
# 메인 윈도우 가져오기
#print(app.windows())
main_window = app.window(title="Battle.net")
main_window.wait("ready", timeout=20)
# 버튼 찾고 클릭
#print(main_window.print_control_identifiers())
#main_window["확인"].click_input()
# "스타크래프트" 탭을 찾아 클릭
main_window.child_window(title="스타크래프트", control_type="TabItem").click_input()
#print(main_window.print_control_identifiers())


main_window.child_window(title_re="플레이: 스타크래프트.*", control_type="Button").click_input()