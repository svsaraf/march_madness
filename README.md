## March Madness Calculator

This script generates a possible final four for the Men's and Women's March Madness bracket given the win probabilities from 538. Could be modified to do Monte Carlo Simulations, but this is March Madness...so it runs each possibility only once. 

#### Usage for 2019 (from either Unix shell or Mac OS Terminal): 

    git clone https://github.com/svsaraf/march_madness.git
    cd march_madness
    python march_madness_calculator.py


#### Usage if you've tweaked the probabilities in another file

    python march_madness_calculator.py file_name_of_interest


Note that you may have to modify the download from 538 to use this if there are still play-in games - all teams should have a numerical seeding (not 11a for instance). 