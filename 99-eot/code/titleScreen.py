import Print

def display():
  Print.clear()
  print(Print.greenf('\t\t _______ _________  ') + Print.redf(' _______  _______                     '))
  print(Print.greenf('\t\t(  ____ \\__   __/  ') + Print.redf('(  ____ \(  ___  )|\     /|           '))
  print(Print.greenf('\t\t| (    \/   ) (     ') + Print.redf('| (    \/| (   ) || )   ( |           '))
  print(Print.greenf('\t\t| (__       | |     ') + Print.redf('| (_____ | (___) || | _ | |           '))
  print(Print.greenf('\t\t|  __)      | |     ') + Print.redf('(_____  )|  ___  || |( )| |           '))
  print(Print.greenf('\t\t| (         | |     ') + Print.redf('      ) || (   ) || || || |           '))
  print(Print.greenf('\t\t| (____/\   | |     ') + Print.redf('/\____) || )   ( || () () |           '))
  print(Print.greenf('\t\t(_______/   )_(     ') + Print.redf('\_______)|/     \|(_______)           '))
                                                          
  print(Print.cyanf('\t _______     ') + Print.yellowf('          _______  _______ _________ _______ '))
  print(Print.cyanf('\t(  ____ \    ') + Print.yellowf('|\     /|(  ___  )(  ____ \\__   __/(  ____ \\'))
  print(Print.cyanf('\t| (    \/    ') + Print.yellowf('| )   ( || (   ) || (    \/   ) (   | (    \/'))
  print(Print.cyanf('\t| (__ ') + ' _____ ' + Print.yellowf('| | _ | || (___) || (_____    | |   | (__    '))
  print(Print.cyanf('\t|  __)') + '(_____)' + Print.yellowf('| |( )| ||  ___  |(_____  )   | |   |  __)   '))
  print(Print.cyanf('\t| (          ') + Print.yellowf('| || || || (   ) |      ) |   | |   | (      '))
  print(Print.cyanf('\t| (____/\    ') + Print.yellowf('| () () || )   ( |/\____) |   | |   | (____/\\'))
  print(Print.cyanf('\t(_______/    ') + Print.yellowf('(_______)|/     \|\_______)   )_(   (_______/'))
                                                          

  print('\n\n')
  print(Print.bold('Welcome!'))
  print("You have stumbled across Pat and Ken's e-waste game.")
  print()
  print(Print.yellowf(Print.under("What would E.T. say if he saw all of our e-waste today?")))
  print("E.T. was able to phone his buddies in outer space by throwing together" + Print.cyanf(Print.bold(" an old record player, a lantern battery, jumper wires and a Speak & Spell kids toy")) + ".  If he saw all of our electrical and electronic equipment getting thrown out and " + Print.bold(Print.redf("not being re-used, re-purposed or re-cycled")) + ", I'm sure he would use a different finger.")
  print("\n")
  input(Print.greenf('Press ENTER to start '))