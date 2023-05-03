import os

def main():
  
  # トリガーファイルパス
  trigger_path = "./trigger.txt"
  # トリガーファイル格納
  SetTrigger(trigger_path)
  print("Set trigger file.")

#-------------------------
# トリガーファイル格納関数
#-------------------------
def SetTrigger(path):
  f = open(path, "w")
  f.close()

main()