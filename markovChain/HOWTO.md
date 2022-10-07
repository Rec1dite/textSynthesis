# Basic Markov Chain Generator

This is a simple Markov Chain generator that generates text based purely on probability.

## To use:
1) First, place a text file containing your input text (it can be anything, though natural language is normally the most interesting) inside the `markovChain` folder.

2) Run the parser script to generate an ngrams database:
> python3 MarkovChainParser.py
(Follow the prompt and enter the name of your input file)

3) Run the reader script to generate a Markov chain based on the database:
> python3 MarkovChainReader.py
(Follow the prompts)