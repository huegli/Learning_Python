bedroom_strings_dict = {
    'intro':  """
You wake up with a terrible hangover. As you try to get up the world spins -
around you and you feel even more sick.
"""
    ,'sleep':  """
You go back to sleep.
"""
    ,'get up': """
You get out of bed and stand shakily on your feet. You feel worse than ever.
"""
    ,'bathroom': """
You slowly make your way to the bathroom in sheer misery.
"""
}

bedroom_states_dict = {
    'current':     'bedroom',
    'sleep':       'death',
    'get up':      'bedroom',
    'bathroom':    'bathroom'
}

bathroom_strings_dict = {
    'intro':  """
You are in the bathroom. The shades are pulled down and it is dark.
"""
    ,'shit':  """
You sit down and take a good dump. What a relief.
"""
    ,'brush teeth': """
You brush your teeth and even remember to floss.
"""
    ,'bedroom': """
You stumble back into bed.
"""
    ,'shades': """
You pull up the shades. The bright morning light blinds your eyes but you can
vaguely make out the silhouette of a bulldozer heading towards you.
"""
    ,'outside': """
You run outside as fast as you can, cold sweat running down your back.
"""
}

bathroom_states_dict = {
    'current':     'bathroom',
    'shit':        'bathroom',
    'brush teeth': 'bathroom',
    'bedroom':     'death',
    'shades':      'bathroom',
    'outside':     'outside'
}

outside_strings_dict = {
    'intro':  """
You are outside your house. The big bulldozer is slowly moving closer.
"""
    ,'house':  """
You go back into the house.
"""
    ,'scream': """
You scream for the bulldozer to stop, but the noise it makes is too loud
and nobody can hear you.
"""
    ,'lie down': """
You lie down in front of the approaching bulldozer.
"""
    ,'run away': """
You run away from your house and the bulldozer.
"""
}

outside_states_dict = {
    'current':     'outside',
    'house':       'death',
    'scream':      'outside',
    'lie down':    'finish',
    'run away':    'death'
}

vogons_came_strings_dict =  {
    'intro': """
You wasted too much time. The Vogon Constructor fleet arrives and blows up the earth.
"""
}

vogons_came_states_dict = {
    'current':      'vogons came'
}

death_strings_dict = {
    'intro': """
Shortly afterwards, the earth is destroyed by the Vogons.
"""
}

death_states_dict = {
    'current': 'death'
}

finish_strings_dict = {
    'intro': """
Ford Prefect comes by and gets you on the Vogon ship right before the
earth blows up.
"""
}

finish_states_dict = {
    'current': 'finish'
}

class Scene(object):

    intro = '<- INITIALIZE ME ->'
    current = '<- INITIALIZE ME ->'

    actions = {}
    new_scenes = {}

    def __init__(self, strings_dict, states_dict):

        # break out the intro string seperately
        if strings_dict.has_key('intro'):
            self.intro = strings_dict['intro']
            del strings_dict['intro']
        else:
            print "No 'intro' key found initializing", self
            exit(1)

        # rest goes into actions dict(might be empty at this point)
        self.actions = strings_dict

        # initialize current scene property
        if states_dict.has_key('current'):
            self.current = states_dict['current']
            del states_dict['current']
        else:
            print "No 'current' key found initializing", self
            exit(1)

        # rest goes into new_scenes
        self.new_scenes = states_dict

    def enter(self):
        print self.intro


class ActiveScene(Scene):

    def run(self,first_time, action_input = ""):
        if (first_time):
            self.enter()

        # for testing purpose allow action_input to be predefined
        if action_input:
            silent = True
        else:
            action_input = raw_input("> ")
            silent = False

        action_string = "I don't understand what you mean"
        next_scene = self.current

        for actions_key, actions_value in self.actions.items():
            if (action_input.find(actions_key) >= 0):
                next_scene = self.new_scenes[actions_key]
                action_string = actions_value
                break

        if not silent:
            print action_string

        return next_scene

class EndScene(Scene):

    def run(self):
        self.enter()
