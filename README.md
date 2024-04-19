# Game-of-Chance

Game: LUCKOMETER (name for now)

'no matter how sensible your choice sounds, there's always a twist'
name idea: twist of fate? lol // Twistopia //

- Base structure
  1. 1 player game
  2. Point system (luck points)
  3. Random scenarios throughout game: some interactive, some not
  4. Each event can be consequential

Game Initialisation: 
-
- Display an introduction message explaining the game mechanics and rules.
- Initialize the player's luck score to 0.

Gameplay:
-
- Start the day by triggering events in a loop until the day ends
- Each event should be randomly selected from a pool of possible scenarios
- Display each event to the player and provide interactive choices if applicable
- Based on the player's choices, update the luck score accordingly
- Store the outcomes of each event for end-of-day reporting

Events:
-
- How many per day
- How many in the 'pool'
- Description of the event
- Whether it's interactive or not
- Possible choices and their outcomes
- Impact on the luck score.

Point System:
-
- Display the player's luck score at all times during gameplay.
- Determine thresholds for different luck score ranges and provide corresponding messages eg.:
- Luck score > 50: "It's your lucky day!! Buy a lottery ticket asap!"
- Luck score < 30: "Looks like it's not your day. Maybe stay indoors?"
- 30 <= Luck score <= 50: "Not too shabby. Keep it up!"

End of Day Report:
<!-- Player ends the day, potentially. The player is presented an output "you have done all activities needed today, wanna end your day? -->
-
Once the day ends, present a summary to the player:
- Display the outcomes of each event encountered during the day.
- Show the total luck score achieved.
- Provide a message based on the luck score range.

Additional Features to think about:
-
- Luck boosters: might temporarily boost chance of positive outcome
- add any ideas to make the game more interesting

More things to think about:
-
- GUI
- Error handling

Game Example 
-
**Day starts** (Game starts --> Luck score: 0) 

_Random event 1: You walk out the door and you see a slippery sidewalk! What do you do? [interactive, immediate outcome]_
<!-- Player does not see the outcome of each choice while choosing, the outcome is a reward/ punishment and is random -->

- Choice A: Just walk on lightly!
  - Outcome 1: phew good thing you wore crocs today! (luck+5)
  - Outcome 2: nah uh those converse wont hold, your feet are taking a bath (luck-5)

- Choice B: Parkour! jump past it!
  - Outcome 1: leg days? 404 not found what made you think you could do it? full frontal splash you are now drenched (luck-10)
  - Outcome 2: way to go! those long jumps during physical education coming in clutch😎 (luck+10)
 
_Random event 2: Want to buy Stocks from Company A? [interactive, no immediate outcome]_

- Choice A: Yes
- Choice B: No

_Random announcement: Stocks A went up/down!_ ((doesnt not have to come immediately after))
- Outcome based on player's choice


<!-- Since it is a game about a day, I am thinking of slotting a food session -->

_Random event 3: Yum Yum! You earned yourself a treat in Hotel Twistinolvenia. Choose a table, each table has a luck magic and great food?_
 <!-- Interactive, Immediate outcome: Every outcome is rewarded just because eating is good in this game -->
- [A] Corner Table
  - Outcome: Your treat is Ghoulash! Your luck magic is 5 (luck +5)

- [B] Round Table
  - Outcome: Your treat is Eye Scream! Your luck magic is 1, please scream (luck +1)


# Open Source Licence Declaration

This project uses Pygame, which is a set of Python modules designed for writing video games. Pygame is licensed under the GNU Lesser General Public License (LGPL). For Pygame source, see: https://github.com/pygame/. For more details on the license, see: https://www.pygame.org/wiki/about and https://www.gnu.org/licenses/lgpl-3.0.html.