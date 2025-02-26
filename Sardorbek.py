            import random

            def play_game():
                print("Тас, қағаз, қайшы ойынына қош келдіңіз!")
                
                # Ойыншының таңдауы
                player_choice = input("Тас, қағаз немесе қайшы таңдаңыз: ").lower()
                
                # Компьютердің кездейсоқ таңдауы
                choices = ['тас', 'қағаз', 'қайшы']
                computer_choice = random.choice(choices)
                
                print(f"Компьютердің таңдауы: {computer_choice}")
                
                # Жеңімпазды анықтау
                if player_choice == computer_choice:
                    print("Тең ойын! Екеуің де бірдей таңдадыңыз.")
                elif (player_choice == 'тас' and computer_choice == 'қайшы') or \
                    (player_choice == 'қағаз' and computer_choice == 'тас') or \
                    (player_choice == 'қайшы' and computer_choice == 'қағаз'):
                    print("Сіз жеңдіңіз!")
                else:
                    print("Компьютер жеңді!")
                    
            # Ойынның жұмыс істеуі
            play_game()
