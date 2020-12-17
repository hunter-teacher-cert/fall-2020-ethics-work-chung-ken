import Story

# each page has:
#  dialogue, [an, array, of, choices], [corresponding, dict, indeces]

# start page
home = ["Feel like helping the world today?", ["Yes", "No"],["help-yes", "help-no"]]

# the 'No' thread
n1 = ["Yeah, you're right.  Why bother?\n\nAnything you do will probably end up like another Basel Convention.", ["What's that?", "Wait. I thought that helped out.", "You're right."], ["basel", "basel-bust", "give-up"]]
n11 = ["The Basel Convention on the Control of Transboundary Movements of Hazardous Wastes and their Disposal is an International treaty, designed to reduce the movements of hazardous waste between nations, and specifically to prevent dumping of hazardous waste from developed to less developed countries.", ["That didn't help e-waste dumping?", "Whatever."], ["basel-bust", "give-up"]]
n12 = ["Well, after almost three years of gathering support, the law came into force on May 5, 1992. But, soon after, countries began to circumvent the law by shipping their e-waste as “second-hand goods” instead of Hazardous waste. First-world e-waste still ended up polluting many third-world countries.", ["We should do something.", "Not my problem."], ["help-yes", "give-up"]]
n13 = ["Yeah. Better not to think about things we can't control.\nIt's not your problem anyway.\nBetter to just bury your head in the sand.", ["No. I want to know more.", "Yeah. I quit."], ["help-yes", 'end']]

# the 'Yes' thread
y1 = ["Great! How about starting to prepare for the next DMCA exemption cycle concerning e-waste?", ["Sure! Put me in, coach.", "What is DMCA?", "What's DMCA got to do with e-waste?", "What? The exemptions run out?"], ["dmca-yes", "dmca-what", "dmca-how", "dmca-exempt"]]
y11 = ["Great! Nice to have your support. Exemption rules are revised every three years. Barring any modifications, the next date is scheduled for October 2021.", ["What is DMCA?", "What does a copyright law have to do with e-waste?", "Tell me more about these exemption rules.", "Got it. I'll get on it."], ['dmca-what', 'dmca-how', 'dmca-exempt', 'end']]
y12 = ["DMCA is the Digital Millennium Copyright Act passed in 1998. The law became effective in 2000 and it updated U.S. copyright law to meet the demands of the Digital Age.", ["What does a copyright law have to do with e-waste?", "What about those exemption rules?"], ['dmca-how', 'dmca-exempt']]
y13 = ["It’s what manufacturers use to prevent consumers or unauthorized repair people from accessing their device. This results in the user not being able to attempt their own repair and instead turn to the costly manufacturers to do it. This in turn drives down lifespan of a product causing them to end up as waste much sooner than they should be.", ["What about those exemption rules?", "Why aren't there any Right to Repair laws?"], ['dmca-exempt', 'r2r']]
y14 = ["Exemption rules expire after three years. There has been talk of extending them, as long as there is no petition for the  contrary is submitted, however that hasn’t happened yet.\n\nWant to help write a proposal?", ['Yes!', "What does DMCA have to do with e-waste?"], ['r2r', 'dmca-how']]
y141 = ["There are currently 4 states in the U.S. which have “Right to Repair” Legislation. Each one has some unique strengths that when combined would create a potential outline for a Bill proposal to congress which would protect consumers on the federal level.\n\nCheck out this site to see what legislation different states have:\nhttps://www.core77.com/posts/90945/Check-This-List-to-See-if-Your-State-Has-Right-to-Repair-Laws", ["I'm ready to work on the proposal.", "What is DMCA?"], ['end', 'dmca-what']]

narrate = Story.Create()
narrate.pages["start"] = home # everyone opening page will be labeled "start"
narrate.pages["help-no"] = n1
narrate.pages["basel"] = n11
narrate.pages["basel-bust"] = n12
narrate.pages["give-up"] = n13
narrate.pages["help-yes"] = y1
narrate.pages["dmca-yes"] = y11
narrate.pages["dmca-what"] = y12
narrate.pages["dmca-how"] = y13
narrate.pages["dmca-exempt"] = y14
narrate.pages["r2r"] = y141

def getStory():
  return narrate