from nhne.tools import Deploy, get_ninjas

deploy = Deploy(
    # ANOTHER NINJA
    get_ninjas(*(
        "Himawari Uzumaki", "Boruto Karma Mode", "Otsutsuki Urashiki", "Uchiha Sarada", "Sage Mitsuki",
        "Hanabi Hyuga", "Hashirama", "Tobirama", "Boruto", "Jiraiya", "Tsunade", "Sakura"
    )),
    # MAIN NINJA
    get_ninjas(*(
        "Menma Uzumaki", "Rinegan Sasuke", "Naruto Kyuubi Mode"
    ))
)

print(deploy.combo)