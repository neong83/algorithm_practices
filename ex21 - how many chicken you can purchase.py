"""
You have 100 bucks and would like to purchase 100 chickens
each rooter cause 5 bucks
each hen cause 3 bucks
3 checks cause 1 bucks
"""


def purchase_chickens():
	ways_to_purchase = []
	# 100 bucks can only purchase 20 rooters max
	for rooters in range(20):
		# 100 bucks can only purchase 33 hens max
		for hens in range(33):
			chicks = 100 - rooters - hens
			if chicks % 3 == 0 and rooters * 5 + hens * 3 + chicks / 3 == 100:
				ways_to_purchase.append(f"rooters: {rooters}, hens: {hens}, chicks: {chicks}")

	return ways_to_purchase

		
ways_to_purchase = purchase_chickens()

print(f"there are {len(ways_to_purchase)} ways to buy 100 chickens with 100 bucks")
for way in ways_to_purchase:
	print(way)
