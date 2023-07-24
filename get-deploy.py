from nhne.tools import Deploy

print("Checking Pipes, Please wait\n")

### GANTI NINJA DI BAWAH SINI SESUAI NINJA YG DIINGINKAN ###
### TOOLS AKAN MEMBUAT PIPE YG BERHUBUNGAN SECARA OTOMATIS ###
### ============== ###
deploy = Deploy.from_row(["Himawari Uzumaki","Boruto Karma Mode","Otsutsuki Urashiki","Uchiha Sarada","Sage Mitsuki"],
["Hanabi Hyuga","Menma Uzumaki","Rinegan Sasuke","Naruto Kyuubi Mode","Hashirama"],
["Tobirama","Boruto","Jiraiya","Tsunade","Sakura"])
### ============== ###
### BIARKAN CODE DI BAWAH ###
fixed_deploy = deploy.fix_pipe()
print(fixed_deploy if fixed_deploy is not deploy else f"Pipa Saat ini sudah mencapai maximum! ({deploy.current_pipe})")
### OUTPUT ###
### ============== ###
# Connected Pipes: 15
# r1: (Boruto Karma Mode, Otsutsuki Urashiki, Sage Mitsuki, Tobirama, Hanabi Hyuga)
# r2: (Jiraiya, Menma Uzumaki, Rinegan Sasuke, Naruto Kyuubi Mode, Tsunade)
# r3: (Sakura, Hashirama, Boruto, Uchiha Sarada, Himawari Uzumaki)
### ============== ###