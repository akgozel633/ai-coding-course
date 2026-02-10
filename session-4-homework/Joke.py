import json
import random
import os

FILE_NAME = 'jokes.json'

# I've compiled 100 jokes for your offline database
DEFAULT_JOKES = [
    {"setup": "Why do programmers always mix up Halloween and Christmas?", "punchline": "Because Oct 31 == Dec 25."},
    {"setup": "How many programmers does it take to change a light bulb?", "punchline": "None, that's a hardware problem."},
    {"setup": "What's the object-oriented way to become wealthy?", "punchline": "Inheritance."},
    {"setup": "Why did the programmer quit his job?", "punchline": "Because he didn't get arrays (a raise)."},
    {"setup": "What is a programmer's favorite hangout place?", "punchline": "Foo Bar."},
    {"setup": "Real programmers count from...", "punchline": "0."},
    {"setup": "Why do Java developers wear glasses?", "punchline": "Because they don't C#."},
    {"setup": "A SQL query goes into a bar, walks up to two tables, and asks...", "punchline": "Can I join you?"},
    {"setup": "What do you call a programmer from Finland?", "punchline": "Nerdic."},
    {"setup": "How do you tell an introverted computer scientist from an extroverted one?", "punchline": "An extroverted computer scientist looks at YOUR shoes when talking to you."},
    {"setup": "Why was the cell phone wearing glasses?", "punchline": "Because it lost its contacts."},
    {"setup": "What do you call a fake noodle?", "punchline": "An impasta."},
    {"setup": "Why did the scarecrow win an award?", "punchline": "Because he was outstanding in his field."},
    {"setup": "Why don't skeletons fight each other?", "punchline": "They don't have the guts."},
    {"setup": "What do you call a belt made out of watches?", "punchline": "A waist of time."},
    {"setup": "Why did the bicycle fall over?", "punchline": "Because it was two-tired."},
    {"setup": "What do you call a penguin in the desert?", "punchline": "Lost."},
    {"setup": "Why did the tomato turn red?", "punchline": "Because it saw the salad dressing."},
    {"setup": "What do you call a bear with no teeth?", "punchline": "A gummy bear."},
    {"setup": "Why can't you trust atoms?", "punchline": "Because they make up everything."},
    {"setup": "What do you call a factory that makes okay products?", "punchline": "A satisfactory."},
    {"setup": "Why did the golfer bring two pairs of pants?", "punchline": "In case he got a hole in one."},
    {"setup": "What do you call a sleeping dinosaur?", "punchline": "A dino-snore."},
    {"setup": "Why did the math book look sad?", "punchline": "Because it had too many problems."},
    {"setup": "What do you call a dog that does magic tricks?", "punchline": "A labracadabrador."},
    {"setup": "Why did the cookie go to the hospital?", "punchline": "Because he felt crummy."},
    {"setup": "What do you call a pile of cats?", "punchline": "A meowntain."},
    {"setup": "Why did the gym close down?", "punchline": "It just didn't work out."},
    {"setup": "What do you call a fish with no eyes?", "punchline": "A fsh."},
    {"setup": "Why did the man put his money in the freezer?", "punchline": "He wanted cold hard cash."},
    {"setup": "What do you call a bee that can't make up its mind?", "punchline": "A maybe."},
    {"setup": "Why did the picture go to jail?", "punchline": "Because it was framed."},
    {"setup": "What do you call a cow with no legs?", "punchline": "Ground beef."},
    {"setup": "Why did the computer show up late to work?", "punchline": "It had a hard drive."},
    {"setup": "What do you call a can opener that doesn't work?", "punchline": "A can't opener."},
    {"setup": "Why did the music teacher need a ladder?", "punchline": "To reach the high notes."},
    {"setup": "What do you call a sheep with no legs?", "punchline": "A cloud."},
    {"setup": "Why did the banana go to the doctor?", "punchline": "Because it wasn't peeling well."},
    {"setup": "What do you call a snowman with a six pack?", "punchline": "An abdominal snowman."},
    {"setup": "Why did the spider get a job in IT?", "punchline": "He was a great web developer."},
    {"setup": "What do you call a deer with no eyes?", "punchline": "No eye-deer."},
    {"setup": "Why did the coffee file a police report?", "punchline": "It got mugged."},
    {"setup": "What do you call a belt with a clock on it?", "punchline": "A waist of time."},
    {"setup": "Why did the chicken cross the playground?", "punchline": "To get to the other slide."},
    {"setup": "What do you call a parrot that flew away?", "punchline": "A polygon."},
    {"setup": "Why did the student eat his homework?", "punchline": "Because the teacher said it was a piece of cake."},
    {"setup": "What do you call a cheese that isn't yours?", "punchline": "Nacho cheese."},
    {"setup": "Why did the developer go broke?", "punchline": "Because he used up all his cache."},
    {"setup": "What do you call a boomerang that doesn't come back?", "punchline": "A stick."},
    {"setup": "Why did the hipster burn his tongue?", "punchline": "He drank his coffee before it was cool."},
    {"setup": "What do you call a pig that knows karate?", "punchline": "A pork chop."},
    {"setup": "Why did the orange stop?", "punchline": "It ran out of juice."},
    {"setup": "What do you call a dinosaur that is crashing his car?", "punchline": "Tyrannosaurus Wrecks."},
    {"setup": "Why did the tree go to the dentist?", "punchline": "To get a root canal."},
    {"setup": "What do you call an alligator in a vest?", "punchline": "An investigator."},
    {"setup": "Why did the invisible man turn down the job offer?", "punchline": "He couldn't see himself doing it."},
    {"setup": "What do you call a fly without wings?", "punchline": "A walk."},
    {"setup": "Why did the melon jump into the lake?", "punchline": "It wanted to be a water-melon."},
    {"setup": "What do you call a group of disorganized cats?", "punchline": "A cat-astrophe."},
    {"setup": "Why did the belt go to jail?", "punchline": "It held up a pair of pants."},
    {"setup": "What do you call a computer that sings?", "punchline": "A Dell."},
    {"setup": "Why did the strawberry cry?", "punchline": "His parents were in a jam."},
    {"setup": "What do you call a nervous javelin thrower?", "punchline": "Shakespeare."},
    {"setup": "Why did the robot go on vacation?", "punchline": "To recharge its batteries."},
    {"setup": "What do you call a cold dog?", "punchline": "A chili dog."},
    {"setup": "Why did the scientist knock the wall down?", "punchline": "He wanted a breakthrough."},
    {"setup": "What do you call a snake that is exactly 3.14 feet long?", "punchline": "A python."},
    {"setup": "Why did the ocean break up with the shore?", "punchline": "It was just too wavy."},
    {"setup": "What do you call a guy who's had too much Tylenol?", "punchline": "Phil."},
    {"setup": "Why did the skeleton go to the dance?", "punchline": "To rattle some bones."},
    {"setup": "What do you call a cat that lives in the desert?", "punchline": "Sandy claws."},
    {"setup": "Why did the golfer wear two shirts?", "punchline": "In case he got a hole in one."},
    {"setup": "What do you call a man with a shovel?", "punchline": "Doug."},
    {"setup": "Why did the balloon go to the doctor?", "punchline": "It was feeling light-headed."},
    {"setup": "What do you call a fish that needs help with its oral hygiene?", "punchline": "A sturgeon."},
    {"setup": "Why did the girl smear peanut butter on the road?", "punchline": "To go with the traffic jam."},
    {"setup": "What do you call a dinosaur with a extensive vocabulary?", "punchline": "A thesaurus."},
    {"setup": "Why did the cookie cry?", "punchline": "Because his mother was a wafer so long."},
    {"setup": "What do you call a funny mountain?", "punchline": "Hill-arious."},
    {"setup": "Why did the teddy bear say no to dessert?", "punchline": "Because she was stuffed."},
    {"setup": "What do you call a person who is afraid of Santa?", "punchline": "Claustrophobic."},
    {"setup": "Why did the computer freeze?", "punchline": "Someone left the Windows open."},
    {"setup": "What do you call a cow during an earthquake?", "punchline": "A milkshake."},
    {"setup": "Why did the man build his house out of LEGO?", "punchline": "He wanted to block the neighbors out."},
    {"setup": "What do you call a ghost's true love?", "punchline": "A ghoul-friend."},
    {"setup": "Why did the astronaut break up with his girlfriend?", "punchline": "He needed space."},
    {"setup": "What do you call a monkey that loves potato chips?", "punchline": "A chipmunk."},
    {"setup": "Why did the tomato go to the party?", "punchline": "To ketchup with friends."},
    {"setup": "What do you call a cold dog sitting on a bunny?", "punchline": "A chili dog on a bun."},
    {"setup": "Why did the scarecrow become a successful manager?", "punchline": "Because he was outstanding in his field."},
    {"setup": "What do you call a bird that can't fly?", "punchline": "A penguin."},
    {"setup": "Why did the candle go to the gym?", "punchline": "To get a light workout."},
    {"setup": "What do you call a bear with no ears?", "punchline": "B."},
    {"setup": "Why did the pencil sharpen its mind?", "punchline": "To stay on point."},
    {"setup": "What do you call a lemon in distress?", "punchline": "Lemon-aid."},
    {"setup": "Why did the alarm clock go to therapy?", "punchline": "It was feeling wound up."},
    {"setup": "What do you call a group of sheep rolling down a hill?", "punchline": "A lamb-slide."},
    {"setup": "Why did the cloud stay home?", "punchline": "It was feeling under the weather."},
    {"setup": "What do you call a fake stone in Ireland?", "punchline": "A sham-rock."},
    {"setup": "Why did the light bulb fail the test?", "punchline": "It wasn't bright enough."}
]

def load_or_create_jokes():
    if not os.path.exists(FILE_NAME):
        print(f"File {FILE_NAME} not found. Creating a new one with 100 jokes...")
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_JOKES, f, indent=4)
        return DEFAULT_JOKES
    
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    jokes = load_or_create_jokes()
    joke = random.choice(jokes)
    
    print("\n--- RANDOM JOKE ---")
    print(f"Setup: {joke['setup']}")
    print(f"Punchline: {joke['punchline']}")
    print("-------------------\n")

if __name__ == "__main__":
    main()