from colorama import Fore, Style

tamam_ghad = float(input(Fore.LIGHTBLACK_EX + 'tamam ghad: ' + Style.RESET_ALL))
dor_kamar = float(input(Fore.LIGHTBLACK_EX + 'dor kamar: ' + Style.RESET_ALL))
dor_sine = float(input(Fore.LIGHTBLACK_EX + 'dor sine: ' + Style.RESET_ALL))
dor_basan = float(input(Fore.LIGHTBLACK_EX + 'dor basan: ' + Style.RESET_ALL))

khat_sine = (dor_sine / 10) + 10.5 + 2
khat_kamar = (tamam_ghad / 4) - 1
khat_basan = khat_sine + khat_kamar
karor_posht = (dor_sine / 8) + 5.5
kaf_halghe = (dor_sine / 8) - 1.5
karor_jelo = (dor_sine / 4) - 4
nesf_fasele_sine = (dor_sine / 10) + 0.5
posht_yaghe = (dor_sine / 20) + 2

if dor_sine <= 90:
    bolandi_jelo = khat_kamar + 4
elif 90 < dor_sine <= 100:
    bolandi_jelo = khat_kamar + 4.5
elif 100 < dor_sine <= 110:
    bolandi_jelo = khat_kamar + 4.5 + ((dor_sine - 100) / 10)
elif 110 < dor_sine <= 120:
    bolandi_jelo = khat_kamar + 5 + ((dor_sine - 100) / 10)
elif 120 < dor_sine <= 130:
    bolandi_jelo = khat_kamar + 5.5 + ((dor_sine - 100) / 10)
elif dor_sine > 130:
    bolandi_jelo = khat_kamar + 6 + ((dor_sine - 100) / 10)

bolandi_markaz_sine = (dor_sine / 4) + 2

print('')
print(Fore.LIGHTBLACK_EX + f'khat sine / bolandi halghe = ' + Fore.LIGHTBLUE_EX + f'{khat_sine} _ {khat_sine + 1}' + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + f'khat kamar / bala tane posht = ' + Fore.LIGHTBLUE_EX + f'{khat_kamar}' + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + f'khat basan / bolandi basan = ' + Fore.LIGHTBLUE_EX + f'{khat_basan}' + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + f'karor posht = ' + Fore.LIGHTBLUE_EX + f'{karor_posht} _ {karor_posht + 0.5}' + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + f'kaf halghe = ' + Fore.LIGHTBLUE_EX + f'{kaf_halghe} _ {kaf_halghe + 1.5}' + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + f'karor jelo = ' + Fore.LIGHTBLUE_EX + f'{karor_jelo} _ {karor_jelo + 1.5}' + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + f'nesf fasele sine = ' + Fore.LIGHTBLUE_EX + f'{nesf_fasele_sine}' + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + f'posht yaghe = ' + Fore.LIGHTBLUE_EX + f'{posht_yaghe}' + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + f'bolandi jelo = ' + Fore.LIGHTBLUE_EX + f'{bolandi_jelo}' + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + f'bolandi markaz sine = ' + Fore.LIGHTBLUE_EX + f'{bolandi_markaz_sine} _ {bolandi_markaz_sine + 1}' + Style.RESET_ALL)
