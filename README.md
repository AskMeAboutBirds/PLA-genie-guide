# PLA-genie-guide
Guide for RNG manipulation of Pokemon Legends Arceus Genies


General process
------
  

The general process for every genie is the following:

1.  SR for your spread on its spawner (usually the last active spawner) within 100 frames
	a. CFW: check your future frames with the tool attached below after reloading the map
	b. RETAIL: reload the map, save, catch the genie, trade it to a bot to check your generator seed, plug that into the tool to see future frames.
    
2.  Save when you get a good seed
    
3.  Faint the genie
   
4.  Advance the genie spawner frame
	a.  You can do this by teleporting to a camp and switching the current day night cycle to its opposite (day to night or night to day) and the flying back over the spawn area
	b.  Or you can wait in the genie spawner area until either the weather changes or the day night cycle changes (ie, morning → day → evening → night → morning)

5.  Travel to a cave on the map (do not use an occupied one)
    
6.  Save inside the cave and reset your game
    
7.  Your genie is now respawned and you can faint it again, fainting advances one spawner frame.

8. Repeat 3 - 7 until you are on frame 0 from your starting frame

9. Catch your genie when it is generated (frame 0 in provided tool)
	a. On retail, catch your genies when you get close and check their stats to make sure you do not miss your frame
	b. on CFW use capture sight or catch and check your genies when close (< 3 frames away).


------

****A note on SR’ing for a good spawner seed vs accepting advancing N frames to your target****![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/opt_frames.png)

Depending on your desired spread, you have a “frame limit” where accepting a spawner with N advances and advancing is faster than continuing to SR. The chart above lists 5 of those limits for common desired target spreads. For an example, say I want a 5iv only 31’s (say 31/31/31/xx/31/31 jolly) and only 1 desired nature (blue line). The fastest process is to SR my spawner until I have a 31/31/31/x/31/31 jolly within 86 frames or less. Another way to say this is SRing for a new closer frame is faster than accepting a frame higher than 86 and advancing the genie spawner >86 times. The chart above is also using the “worst case scenario” values for total time to SR and advance N frames, 95% of the time your RNG process will be less than the values reported above in the legend (assuming you are SRing as fast as possible and advancing the genies in 4 minutes). So to RNG for a 31/31/31/x/31/31 jolly spread, my worst case scenario time for this spread is 692 minutes – 95% of the time my total active time RNGing will be less than this value.


----------

Enamorus
---

**Prep**

Have pokeballs to catch the pokemon. Have at least 3 smoke bombs per frame advance you are willing to do, if possible bring 999 smoke bombs as this makes encountering and fainting enamorus much faster.

---

**Code input**

Go to whatever directory you installed the python codes and run:

    python pla_legend_tool_cfw.py 
     --gids=396,397,398,399,401,402,403,404,405
     --gender=0
     --filter_on=1
     --rolls=1
     --search_range=500
     --natures=Quiet,Sassy,Relaxed,Brave
     --guaranteed_ivs=3 
     --iv_filter=30,30,30,30,30,0 
     --iv_comp=">=,>=,>=,>=,>=,>="

adjust the inputs for your usage

For retail:

    python pla_legend_tool_retail.py 
     --gs=0x0
     --gender=0
     --filter_on=1
     --rolls=1
     --search_range=500
     --natures=Quiet,Sassy,Relaxed,Brave
     --guaranteed_ivs=3 
     --iv_filter=30,30,30,30,30,0 
     --iv_comp=">=,>=,>=,>=,>=,>="

replace gs with your found generator seed.

---

**Finding a seed**

  

It is recommended to SR your spawner seed by reloading the crimson mirelands until the Enamorous spawner has your desired spread within 100 frames, as each advancement takes anywhere from 2 - 5 minutes.

  

CFW


Each time you reload the area, use the provided script or other methods to check the last 10 spawners roughly 396-406, enamorus should be the -2 from the last spawner when you initially load into the area, even if its group id shifts based on outbreaks. SR until you have your desired spread within your frame limit on the last spawner listed. Empty spawners show a 0x0 / Blank. The attached tool will label which spawner in memory is Enamorus for you.

  

Retail

  
Reload the area, save, and catch the enamorus on your map and trade it to a bot to find your spawner seed, plug your generator seed into the provided python script and reset and repeat if there is not a good spread within your frame limit. Once there is, reload your last save from before you caught landorus. Take note of how many frames you need to advance and have something to keep track of how many times you have fainted landorus, if you overshoot your frame you will NOT be able to back track by saving since to advance one frame you must save your game!!

  ----------

**Advancing frames**

  

Once you find a good seed (like the one below) you need to advance the spawner.

  

Encounter and faint the enamorus that has spawned. It is easiest to encounter enamorus by flying above it, drop from a safe distance while holding the right trigger to use a smoke bomb, let go of the trigger buffer a smoke bomb when close to the ground, ensuring the smoke bomb goes off below you as you land. This should NOT alert the enamorus or surrounding pokemon, leaving you free to hit enamorus once with your pokemon’s pokeball. Fly into the air and follow it and repeat this process. This is why the fastest advancement method requires a minimum of 3 smoke bombs. By doing this you hopefully do not alert any pokemon to attack you or the enamorus so it runs away and you have to do a very annoying chase through the bog and tons of pokemon with homing missile attacks. Also unlike the other genies, enamorus seems to target you directly with its attacks, so staying still is a bad idea whereas it’s safe for other genies.

![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/img1.jpg)


Once it faints, you need to advance the spawner frame. The fastest way to do this is to teleport to the bogbound camp, sleep to switch the time day to night or vice versa based on what time it is, then fly back over the bog where enamorous spawns. If you are lazy, you can also wait on a nearby safe ledge still within the bog for either the weather to change or the day/night cycle to change. On CFW use the script to check when your frame rolls over, once the spawner frame advances one you can go to the next step. On retail, its simpler to change the clock at the bogbound camp and then fly back over the spawner area.

![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/bb_camp.jpg)

![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/bb_camp2.jpg)

![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/img2.jpg)

The spawner frame has advanced one, but **the genie will not respawn yet** you need to fly to the lake cave and save inside, reset and reload your game.

![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/img3.png)

![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/img4.jpg)

![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/img5.jpg)

![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/img6.jpg)

![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/img7.jpg)

Now that you have reloaded from inside the cave the genie is respawned and will reappear, teleport to the bogbound camp and fly north to reencounter the enamorus.

![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/img8.jpg)

![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/img9.jpg)

Repeat the above processes until you are close to your target

On retail, when you get close you may want to catch each enamorus and check its spread / stats so you do not overshoot. Reload your game from the cave and then faint it. The provided python script can print out all frames til your target to check where you are if you set the option filters=False.

 
On CFW, switch to capturesight (and close the python script as it will no longer work) or do the same process described above for retail, or just catch the spawned enamorus when the script reports it to be on frame 0.

  ![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/final_code.png)

![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/final1.jpg)

![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/final2.jpg)

![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/final3.jpg)


![enter image description here](https://raw.githubusercontent.com/AskMeAboutBirds/PLA-genie-guide/main/enamor_images/final4.jpg)





**Tips:**

  1. You can take breaks at any point during this process by leaving your game closed when you save in the cave.

1. Initiate battles with a back strike so it only considers enamorus for the battle and not the surrounding random mons

2. [check out the attached video](https://youtu.be/kpXki7hshz0) for a fast way to encounter and faint enamorus  -- basically drop out of the sky from a nonfatal height near enamorus and buffer throw a smoke bomb right where you land. If done right no mons will see you and you can hit enamorus with an item/pokemon pokeball and fly again before it has a chance to flee. After doing this 3 times enamorous is stunned and you can initiate the battle.




Acknowledgements
----

Any code is adapted from Lincoln-LM's PLA-live-map code:
@Lincoln-LM https://github.com/Lincoln-LM/PLA-Live-Map

Any new code for this project was stripping down this code, all credit goes to Lincoln and @wwwwwwzx for the original code



