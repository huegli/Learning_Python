from sys import argv
import hhgtg_scenes

if len(argv) > 1:
    testmode = argv[1]
else:
    testmode = ""

the_bedroom = hhgtg_scenes.ActiveScene(
        hhgtg_scenes.bedroom_strings_dict,
        hhgtg_scenes.bedroom_states_dict)

the_bathroom = hhgtg_scenes.ActiveScene(
        hhgtg_scenes.bathroom_strings_dict,
        hhgtg_scenes.bathroom_states_dict)

the_outside = hhgtg_scenes.ActiveScene(
        hhgtg_scenes.outside_strings_dict,
        hhgtg_scenes.outside_states_dict)

the_vogons_came = hhgtg_scenes.EndScene(
        hhgtg_scenes.vogons_came_strings_dict,
        hhgtg_scenes.vogons_came_states_dict)

the_death = hhgtg_scenes.EndScene(
        hhgtg_scenes.death_strings_dict,
        hhgtg_scenes.death_states_dict)

the_finish = hhgtg_scenes.EndScene(
        hhgtg_scenes.finish_strings_dict,
        hhgtg_scenes.finish_states_dict)

world = {}
world['bedroom'] = the_bedroom
world['bathroom'] = the_bathroom
world['outside'] = the_outside
world['vogons came'] = the_vogons_came
world['death'] = the_death
world['finish'] = the_finish

def test_world():
    assert the_bedroom.run(False,"get up") == "bedroom"
    assert the_bedroom.run(False,"sleep") == "death"
    assert the_bedroom.run(False,"bathroom") == "bathroom"
    assert the_bedroom.run(False,"hurga") == "bedroom"
    assert the_bathroom.run(False,"shit") == "bathroom"
    assert the_bathroom.run(False,"brush teeth") == "bathroom"
    assert the_bathroom.run(False,"bedroom") == "death"
    assert the_bathroom.run(False,"shades") == "bathroom"
    assert the_bathroom.run(False,"outside") == "outside"
    assert the_bathroom.run(False,"hurga") == "bathroom"
    assert the_outside.run(False,"house") == "death"
    assert the_outside.run(False,"scream") == "outside"
    assert the_outside.run(False,"lie down") == "finish"
    assert the_outside.run(False,"run away") == "death"
    assert the_outside.run(False,"hurga") == "outside"

if (testmode == "test"):
    test_world()
    exit(1);

current_scene = world['bedroom']
last_scene = world['death']

VOGON_THRESHOLD = 3
vogon_count = 0

done_yet = False

while not (done_yet):
    if (current_scene == last_scene):
        first_time_here = False
        vogon_count += 1
    else:
        first_time_here = True
        vogon_count = 0

    if (vogon_count > VOGON_THRESHOLD):
        new_scene_string = world['vogons came'].run()
        done_yet = True
    else:
        new_scene_string = current_scene.run(first_time_here)
        if (new_scene_string == 'death') or (new_scene_string == 'finish'):
            new_scene_string = world[new_scene_string].run()
            done_yet = True
        else:
            last_scene = current_scene
            current_scene = world[new_scene_string]

