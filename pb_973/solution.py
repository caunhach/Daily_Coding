def AmountsOfDecodes(str):
	amounts = 0
	if len(str) == 1 and str[0] > "0" and str[0] <= "9":
		amounts += 1
	elif len(str) > 1:
		if str[0] > "0" and str[0] <= "9":
			amounts += AmountsOfDecodes(str[1:])
	if len(str) == 2 and str[:2] >= "10" and str[:2] <= "26":
		amounts += 1
	elif len(str) > 2:
		if str[:2] >= "10" and str[:2] <= "26":
			amounts += AmountsOfDecodes(str[2:])
	return amounts

print(AmountsOfDecodes("11"))