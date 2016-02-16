import hhgtg_scenes

def test_strings_states_dict(strings_dict, states_dict):
    if not ('current' in states_dict):
        print "No 'current' key found it states_dict"
        exit(1)

    if not ('intro' in strings_dict):
        print "No 'intro' key found"
        exit(1)

    for key, value in states_dict.items():
        if (key == 'current'):
            print "Location: ", value
            print "Description: ", strings_dict['intro']
        else:
            if key in strings_dict:
                print "Action: %s -> Next Location: %s\nDescription: %s" % (key, value, strings_dict[key])            
            else:
                print "Can't find key %s in strings_dict" % key

test_strings_states_dict(
        hhgtg_scenes.bedroom_strings_dict,
        hhgtg_scenes.bedroom_states_dict)

raw_input("-- PRESS ENTER TO CONTINUE --")

test_strings_states_dict(
        hhgtg_scenes.bathroom_strings_dict,
        hhgtg_scenes.bathroom_states_dict)

raw_input("-- PRESS ENTER TO CONTINUE --")

test_strings_states_dict(
        hhgtg_scenes.outside_strings_dict,
        hhgtg_scenes.outside_states_dict)
exit(1)

print a_bedroom.run(True)
a_vogon = hhgtg_scenes.EndScene(
    hhgtg_scenes.vogons_came_strings_dict,
    hhgtg_scenes.vogons_came_states_dict)

a_end = hhgtg_scenes.EndScene(
    hhgtg_scenes.end_strings_dict,
    hhgtg_scenes.end_states_dict)

a_vogon.run()
a_end.run()
