import os
import time

def print_colored_text(text, color_code):
  """Prints text with the specified color code.

  Args:
    text: The text to print.
    color_code: The ANSI escape code for the desired color.
  """
  print(f"\033[{color_code}m{text}\033[0m")

# Print the banner
print_colored_text(
    """
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
████╗░████║██╔════╝████╗░██║██║░░░██║
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░
""",
    "34"
)

print()
print()

# Print the menu
print_colored_text(
    """
||=======================================||
|| 1.lanjut ke ToolsRenv3                ||
|| 2.exit                                ||
||=======================================||
""",
    "38;2;0;255;0"
)

# Get user input
ren9999 = input("                PILIH MENU:")

if ren9999 == "1":
  os.system("clear")
  time.sleep(1)
  print("loading... 3")
  time.sleep(2)
  os.system("clear")
  print("loading... 2")
  time.sleep(2)
  os.system("clear")
  print("loading... 1")
  time.sleep(2)
  os.system("clear")
  os.system("git clone https://github.com/THEOYS123/Ren_aja.git")
  os.chdir("Ren_aja")
  os.system("bash menu.sh")

elif ren9999 == "2":
  os.system("clear")
  print_colored_text(
    """
███████╗██╗░░██╗██╗████████╗
██╔════╝╚██╗██╔╝██║╚══██╔══╝
█████╗░░░╚███╔╝░██║░░░██║░░░
██╔══╝░░░██╔██╗░██║░░░██║░░░
███████╗██╔╝╚██╗██║░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░
""",
    "34"
  )
  time.sleep(1)
  print("[*] THANKS BRO👍❗❗")
  time.sleep(2)
  print("[*] TERIMAKASIH SUDAH MENGGUNAKAN TOOLS SAYA😊😊❗❗")
  time.sleep(3)
  exit()
