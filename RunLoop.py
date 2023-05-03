import os
import time

def main():
  
  # トリガーファイルパス
  trigger_path = "./trigger.txt"

  while True:
    # トリガーファイルが存在する場合
    if CheckTrigger(trigger_path):
      # トリガーファイル削除
      os.remove(trigger_path)
      break
    
    # トリガーファイル待ち
    print("waiting...")
    time.sleep(1)


#-------------------------
# トリガーファイル存在チェック
#-------------------------
def CheckTrigger(path):
  # トリガーファイル存在チェック
  is_file = os.path.isfile(path)
  # トリガーファイルが存在する場合
  if is_file:
    print("trigger was found!")
    return True
  
  return False

main()