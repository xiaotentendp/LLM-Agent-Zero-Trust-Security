# 路径: target_env/send_task.py
import json
import os

TASK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'shared_dir', 'tasks'))
os.makedirs(TASK_DIR, exist_ok=True)

def create_task(task_id, source, user_input):
    task_data = {
        "task_id": task_id,
        "source": source,
        "input": user_input
    }
    file_path = os.path.join(TASK_DIR, f"task_{task_id}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(task_data, f, ensure_ascii=False, indent=2)
    print(f"\033[94m[公机] 已生成任务文件: {file_path}\033[0m")

if __name__ == "__main__":
    print("=== 模拟外部环境发送任务 ===")
    print("请选择发送通道：")
    print(" 1. 正常用户 APP (INTERNAL_TRUSTED)")
    print(" 2. 黑客恶意邮件 (EXTERNAL_UNTRUSTED)")
    
    choice = input("请输入 1 或 2 >> ").strip()
    task_id = str(int(os.times().elapsed) % 10000) # 随机生成个ID
    
    if choice == "1":
        user_input = input("请输入用户指令（例如：打开车灯）>> ").strip()
        create_task(task_id, "INTERNAL_TRUSTED", user_input)
    elif choice == "2":
        user_input = input("请输入黑客注入的恶意文本 >> ").strip()
        create_task(task_id, "EXTERNAL_UNTRUSTED", user_input)
    else:
        print("输入错误！")