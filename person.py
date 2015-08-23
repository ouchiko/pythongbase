class Person:
	
	age = None
	weight = None
	height = None

	def speak(self, what):
		print "I say this: ", what

	def eat(self, eating):
		print "Eating " , eating

	def urinate(self, howmuch):
		print "Weeing ", howmuch

	def poo(self, howmuch):
		print "Pooing", howmuch




person = Person()
person.speak("Hello world")
person.eat("Burger")
person.urinate("a lot")
person.poo("diaereha")