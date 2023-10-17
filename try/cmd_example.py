#!/usr/bin/python3

import cmd

class HelloWorld(cmd.Cmd):
    """simple command processor example"""

    prompt = ">>> "
    friends = ['sit', 'hayat', 'mom']

    def do_greet(self, person):
        """say hello to the user."""
        
        if person and person in self.friends:
            greeting = 'Hello, %s!' % person

        elif person:
            greeting = "hi, " + person
        
        else:
            greeting = "hi"
        print(greeting)

    """def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completion = self.friends[:]

        else:
            completion = [ f
                            for f in self.friends
                            if f.startswith(text)
                            ]
            return completion"""

    def do_EOF(self, line):
        """Exit the cli."""
        return True

    def postloop(self):
        print("wea")

if __name__ == '__main__':
    HelloWorld().cmdloop()
