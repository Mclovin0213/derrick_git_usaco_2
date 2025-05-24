📄 Worksheet: The Hallway Flu

🧪 Scenario Recap

There’s been an outbreak of the Hallway Flu at Oakwood High! Some students have gotten sick, and others are still healthy. The illness spreads from one student to another if they are within R lockers.

Unfortunately, no one knows the value of R, but we do know:
	•	Where every student was standing (locker number)
	•	Whether they are sick (1) or healthy (0)

Your job: Figure out how many students must have started out sick.

⸻

✅ Sample Input

6
7 1
1 1
15 1
3 1
10 0
6 1

❓ Questions
	1.	Who is sick and standing next to whom?
	2.	What’s the smallest distance between a sick student and a healthy one?
	3.	Why does this distance matter?
	4.	Based on who is sick and not, how many “groups” of sick students are isolated from each other?

⸻

🧠 Hint:

You want to:
	•	Figure out an upper limit for R (from where a sick person didn’t infect a nearby healthy one).
	•	Group sick students together if they are within R units of each other.
	•	Count how many separate sick groups exist.

⸻
