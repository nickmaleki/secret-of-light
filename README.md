# secret-of-light
A code implementation of diagrams found in Walter Russell's book, The Secret of Light. 


### What I have so far
You can see from the *TODOs* in my code that I have not captured every element of the art provided by Walter, but I do have a working starting point. 
<!---My Code Running-->
![My Code Running](/pictures/live_update_walter_waves_2.gif)

### The first iteration of the periodic table as proposed by Walter Russell
<!---Walter Russell Periodic Table 1-->
<img src="https://www.meta-synthesis.com/webbook/35_pt/russ.png" width="480"/>


### The second iteration of the periodic table
In order to derive this periodic table to the previous one, you must rotate your frame of reference to look down the inertial line drawn in periodic table 1, when looking down this line, you see periodic table 2. 
<!---Walter Russell Periodic Table 2-->
<img src="https://i.pinimg.com/originals/bf/ee/4d/bfee4db958a4b95b449aa074fdc8da9a.jpg" width="480"/>





### Motivation
I found this periodic table to be very interesting because it *supposedly* generates atoms from very simple behavior. According to [Quora user Andrew Wolff, Adjunct Professor of Chemistry](https://www.quora.com/Why-was-Walter-Russells-version-of-the-periodic-table-not-adopted-by-chemists), *"The two periodic tables proposed by Walter Russell in 1926 show some remarkable insights and some incorrect predictions. The first iteration predicted a large number of elements before and after hydrogen that simply do not exist. It certainly does appear to predict elements past Uranium, and correctly leaves room for Technetium. Thus, the table had faults and insights. His second table avoids these faults while retaining the predictions of **then-unknown** elements."* I cannot find any evidence of someone trying to implement his art into code, so I decided to give it a shot. 


### Why Walter Russell's periodic table? 
Different scientists use different periodic tables to achieve different goals. In my opinion, his perioidic table is far more simple than any of the [others proposed](https://www.meta-synthesis.com/webbook/35_pt/pt_database.php). I find that many scientists tend to ignore people that disagree with their views. Walter Russell was convinced that "God is Light" and for the first 10 chapters of his book he re-iterates this idea very often. Many would stop reading, and because his second periodic table is correct, I decided to give him the benefit of the doubt. Simply put, if he dedicated his entire life to studying reality and its mechanics, only to be shunned by his peers for not having formal schooling in physics, regardless of the potential accuracy of his claims, I think his work is worth considering. Espescially because he accurately predicted then-unkown elements and, with far less scientific value, he was in the same group of people as Nikola Tesla and often spoke to Nikola about wave mechanics. This all being said, I review his teachings with vast skepticism. An interesting thing to note is that the transition metals appear on the bottom of periodic table 2 between 3+ and 3-. This means we are packing many elements between these two numbers. Somehow, the farther you deviate from the inertial line defined in periodic table 1, the descrete sampling of atoms increases. I am looking into what mechanism determines this sampling.  


### Does Walter Russell's model of the atom disagree with Quantum Mechanics? 
To answer this, I first urge you to watch a video about the [Double Slit Experiment](https://youtu.be/h53PCmEMAGo), a video about the [Schrödinger equation](https://youtu.be/BPkcDWLBsrI), and a video about [Quantum Field Theory](https://youtu.be/MmG2ah5Df4g). Even if you're a Physicsist, I believe you will gain some valuable intuition about QM from these videos, please do watch them. [Dr. Jeroen Vleggaar](http://www.huygensoptics.com/contact_en.html), author of the double slit experiment video, summarizes my view of Quantum Mechanics very well: *"In a sense, quantum mechanics is not meant to make us understand the true nature of light and matter, **it was conceived to explain our observations and measurements**. From the perspective of the photon, as described by quantum mechanics, there is no such thing as a physical distance between possible states, because position is defined as a superposition of all possible states. And, In principle, the probability function can cover half the universe if the photon is allowed to travel a long time before absorption."* Use your own intuition here, do you think we need a different equation that describes electron orbitals? If you're a physicist and you're not yet convinced, take a look at [this article](http://www7b.biglobe.ne.jp/~kcy05t/schrodinger2.html).
<!---Contradiction in Schrodinger Equation-->
<img src="http://www7b.biglobe.ne.jp/~kcy05t/zu/shro/hy12.gif" width="480"/>

*"Different from actual multi-electron atoms (with electron's "orbit"), Schrodinger's wavefunction always spread all over the space. This property makes it impossible to solve Scchrodinger equation in multi-electron atoms."* So, to answer the original question, I don't know. We need to implement the model proposed by Walter, then try to add "measurements devices" to see if the observations of these generated atoms align with the probablity functions of hydrogen generated by the Schrödinger equation. We could also use the Born-Oppenheimer approximation to test the probability functions of the oribtals of larger atoms. An implementation of QFT will also work to test the accuracy of Walter's model of the atom. 


### Old commits that look cool but likely have no real meaning to Walter's model of the atom
![Commit 2](/pictures/live_update_walter_waves.gif)
*“In the beginning, there was nothing. And God said, “Let there be light.” And there was light. There was still nothing, but you could see it a lot better.” - Woody Allen*

Philosophically, and in the context of the big bang, this quote makes a lot of sense. There was nothing then something. But how could this be possible, how could nothingness, 0, turn into something? Analogously, how could 0 = x? Well, in modern algebra, the only solution to this system is x=0. But Walter Russel argues that it is possible to leave 0 (which he deems the inertial line) by extending towards positive numbers, but every time you leave 0 towards the positive direction you must come back to 0 by extending towards the negative direction. An example of this extension is the sin wave. Where you leave 0 by extending towards positive 1 and come back to 0 by extending towards -1. If you sample an arbitrary x value, perhaps x = π, you will see y change over time but y will never leave 0. The image above is extremely useful in showing this idea, imagine adding many waves together but the net sum of all of the waves is still 0. Something equals nothing. 
