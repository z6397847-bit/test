# -*- coding: utf-8 -*-
"""
T0 Trading App - 简化版（用于排查Android崩溃）
"""

import os
import traceback

# 记录启动日志
def log_error(msg):
    try:
        with open('/sdcard/t0app_log.txt', 'a') as f:
            f.write(f"{msg}\n")
    except:
        pass

log_error("=== App Starting ===")

try:
    log_error("Step 1: Importing kivy modules...")
    
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.utils import platform
    
    log_error(f"Step 2: Platform = {platform}")
    
    # 简单的主界面
    class MainWidget(BoxLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.orientation = 'vertical'
            self.padding = 20
            self.spacing = 10
            
            log_error("Step 3: Building UI...")
            
            self.add_widget(Label(
                text='T0 Trading App',
                font_size='24sp',
                size_hint_y=0.2
            ))
            
            self.status_label = Label(
                text='Status: Ready',
                font_size='16sp',
                size_hint_y=0.3
            )
            self.add_widget(self.status_label)
            
            btn = Button(
                text='Test Network',
                font_size='18sp',
                size_hint_y=0.2
            )
            btn.bind(on_press=self.test_network)
            self.add_widget(btn)
            
            log_error("Step 4: UI built successfully")
        
        def test_network(self, instance):
            log_error("Step 5: Testing network...")
            try:
                import requests
                r = requests.get('http://qt.gtimg.cn/q=sh600586', timeout=5)
                self.status_label.text = f'Network OK: {len(r.text)} bytes'
                log_error(f"Network test success: {len(r.text)} bytes")
            except Exception as e:
                self.status_label.text = f'Network Error: {e}'
                log_error(f"Network error: {e}")

    class T0App(App):
        def build(self):
            log_error("Step 6: App.build() called")
            return MainWidget()
        
        def on_start(self):
            log_error("Step 7: App.on_start() called")
        
        def on_pause(self):
            log_error("App paused")
            return True
        
        def on_resume(self):
            log_error("App resumed")

    log_error("Step 8: Starting app...")
    
    if __name__ == '__main__':
        T0App().run()

except Exception as e:
    error_msg = f"CRASH: {e}\n{traceback.format_exc()}"
    log_error(error_msg)
    print(error_msg)
    raise
