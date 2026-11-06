# ET574 HW4 - Dice Game Simulator

Name: Qingyun Li
QCC ID: 24457146

## A. AI Usage Documentation

**AI Tool:** Claude

**Purpose:** I used Claude to help me understand how classes work in Python and to guide me through the assignment step by step. It explained the starter test file, helped me find errors in my code (such as a missing method and an indentation mistake), and helped me with Git steps like removing cache files. I typed and ran all the code myself and made sure I understood each part before committing it.

**Prompts:** 
- "Help me understand how to do HW4"
- "Why does my test show AttributeError: 'DiceGame' object has no attribute 'play_round'?"
- "Why are the .pyc files in my Source Control?"

**Evaluation and Modifications:** 
- The starter tests used `Die(sides=6)` but the assignment text used `max_side`. Claude pointed out the difference, and I decided to use `sides` so that the tests pass.
- Claude pointed out that `evaluate_roll` had lost its body when I added `play_round`, and I fixed it.
- Claude suggested removing `__pycache__` from the repository and adding a `.gitignore`. I ran the commands myself.
- After each suggestion, I ran the program and the tests to check that everything worked.

## B. Test Case Modifications

**Test 1: test_boundary_totals**
- What it tests: It checks the boundary between Win and Roll Again. The totals
  6 and 8 are right next to 7, so this test makes sure the rule is not wrong at these points.
- Inputs and expected results: evaluate_roll(6) should return "Roll Again",
  evaluate_roll(7) should return "Win", and evaluate_roll(8) should return "Roll Again".

**Test 2: test_custom_sided_die**
- What it tests: It checks that a Die can have a different number of sides, not only 6.
- Inputs and expected results: I create Die(20) and roll it 100 times.
  Every result should be between 1 and 20.

**Test 3: test_play_round_consistency**
- What it tests: It checks that the four values returned by play_round() match each other.
- Inputs and expected results: I play 100 rounds. In every round, the total
  should be equal to die 1 plus die 2, and the result should be the same as
  evaluate_roll(total).

**How I verified the tests:** I ran `python -m unittest -v` in the Codespaces
terminal. All 10 tests passed (7 starter tests and my 3 new tests).

## C. Reflection on AI Use

**1. How was AI used?**

I used Claude to guide me step by step through the assignment. It explained how classes work, explained the starter test file, and helped me understand error messages. It also suggested the three new test ideas and wrote the test code. I typed, ran, and checked the tests myself.

**2. What test scenarios did AI suggest, and which were adopted, modified, or rejected?** 

Claude suggested three test scenarios: boundary totals (6, 7, 8), a die with 20 sides, and consistency between the values returned by play_round(). I adopted all three, because each one checks something the starter tests do not check. I did not reject any suggestion.

**3. What modifications were made, and why?** 

I fixed the indentation of test_boundary_totals, because the wrong indentation caused an error. I did not change the logic of the three tests. I checked each one and made sure the expected results match the game rules.

**4. How were the results verified?**

I ran python -m unittest -v in the Codespaces terminal, and all 10 tests passed. Two tests failed before I wrote play_round() and passed after, so I knew the tests could catch a missing method.

**5. What did I learn about unit testing and using AI?** 

Unit tests find bugs quickly, even small ones like a wrong indentation. AI can guide me, but I still need to read the code, run it, and check the results myself.