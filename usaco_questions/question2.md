Sonic’s Chaos Emerald Lineup

Dr. Eggman is up to no good again! This time, he’s scrambled the N Chaos Emeralds (2 ≤ N ≤ 10³) that Sonic and his friends had lined up for a big photoshoot to celebrate saving Mobius (again). The emeralds are numbered from 1 to N, and Sonic had originally lined them up in a specific order—a permutation of these numbers.

Before Eggman snatched the list of this lineup, Tails managed to jot down some crucial info: for each pair of adjacent emeralds, Tails recorded the sum of their numbers. That means for each emerald pair, he wrote down the sum of their numbers from left to right, giving us a sequence of N-1 numbers.

Now, Sonic needs your help to recover the original lineup—the lexicographically smallest permutation of the Chaos Emeralds that matches Tails’ recorded sums.

A permutation x is lexicographically smaller than permutation y if at the first position where they differ, x has a smaller number than y. Basically, Sonic wants the earliest-in-dictionary order of the lineup that works.

You can assume that at least one valid lineup exists (Eggman’s not that clever).

⸻

INPUT FORMAT (file: photo.in):
	•	The first line contains a single integer N, the number of Chaos Emeralds.
	•	The second line contains N−1 space-separated integers b₁, b₂, …, bₙ₋₁, where each bᵢ is the sum of two adjacent emerald numbers.

⸻

OUTPUT FORMAT (file: photo.out):
	•	A single line with N space-separated integers representing Sonic’s recovered lineup of the Chaos Emeralds.

⸻

SAMPLE INPUT:

5
4 6 7 6

SAMPLE OUTPUT:

3 1 5 2 4



⸻

Explanation:

Sonic’s lineup 3 1 5 2 4 works because:
	•	3 + 1 = 4
	•	1 + 5 = 6
	•	5 + 2 = 7
	•	2 + 4 = 6

This gives Tails’ recorded sums 4 6 7 6.
