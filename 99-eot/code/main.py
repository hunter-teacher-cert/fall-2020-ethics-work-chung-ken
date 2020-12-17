import titleScreen, endScreen, storySelect, govtStory

titleScreen.display();

# stories is a collection of different educational paths
#  index 0 = govtStory
#  index 1 = ???
stories = [govtStory.getStory()] # only one story right now, add more later

# have user choose their storyline
story = stories[storySelect.display()]

story.start()

endScreen.display()
