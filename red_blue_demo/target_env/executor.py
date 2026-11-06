# 路径: target_env/executor.py
import json
import os
import time

RESULT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'shared_dir', 'results'))

def execute_physical(action):
    if action == "open_car_door":
        print("\033[96m🚗 [物理执行器] 车门已打开。\033[0m")
    elif action == "turn_on_light":
        print("💡 [物理执行器] 车灯已打开。")

if __name__ == "__main__":
    print("=== 外部执行器已启动，正在监听结果目录 ===")
    while True:
        if not os.path.exists(RESULT_DIR):
            time.sleep(1)
            continue
            
        results = [f for f in os.listdir(RESULT_DIR) if f.endswith('.json')]
        for res_file in results:
            path = os.path.join(RESULT_DIR, res_file)
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if data["status"] == "ALLOWED":
                execute_physical(data["action"])
            elif data["status"] == "BLOCKED":
                print("\033[91m[执行器] 收到拦截报告，拒绝执行任何物理动作。\033[0m")
            
            # 处理完删掉
            os.remove(path)
        time.sleep(1)