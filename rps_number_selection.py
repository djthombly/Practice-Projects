{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89e3726a-648c-48dc-8f1c-ba36b79c2c70",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Coded by djthombly on 7/20/24.\n",
    "#Version to accept player entering their selection by submitting a number instead of typing the word.\n",
    "\n",
    "game = True\n",
    "\n",
    "choices = {\"1\": \"Rock\", \"2\": \"Paper\", \"3\": \"Scissors\"}\n",
    "\n",
    "while game == True:\n",
    "\n",
    "    print(\"\\nLet's play Rock, Paper, Scissors!\")\n",
    "    \n",
    "    player_one = input(\"\\nPlayer 1, please enter the number for your choice. 1-Rock, 2-Paper, or 3-Scissors: \")\n",
    "    \n",
    "    while player_one not in choices:\n",
    "        player_one = input(\"Invalid choice. Please enter the number for your choice. 1-Rock, 2-Paper, or 3-Scissors: \")\n",
    "\n",
    "    if player_one in choices:\n",
    "        print(\"Player 1 selected \" + choices[player_one] + \".\")\n",
    "    \n",
    "    player_two = input(\"\\nPlayer 2, please enter the number for your choice. 1-Rock, 2-Paper, or 3-Scissors: \")\n",
    "    \n",
    "    while player_two not in choices:\n",
    "        player_two = input(\"Invalid choice. Please enter the number for your choice. 1-Rock, 2-Paper, or 3-Scissors: \")\n",
    "\n",
    "    if player_two in choices:\n",
    "        print(\"Player 2 selected \" + choices[player_two] + \".\")\n",
    "        \n",
    "    if player_one == player_two:\n",
    "        print(\"\\nBoth players chose \" + choices[player_one] + \". It's a tie!\")\n",
    "    \n",
    "    elif player_one == \"1\" and player_two == \"3\":\n",
    "        print (\"\\n\" + choices[player_one] + \" beats \" + choices[player_two] + \". Player 1 wins!\")\n",
    "    \n",
    "    elif player_one == \"2\" and player_two == \"1\":\n",
    "        print (\"\\n\" + choices[player_one] + \" beats \" + choices[player_two] + \". Player 1 wins!\")\n",
    "    \n",
    "    elif player_one == \"3\" and player_one == \"1\":\n",
    "        print (\"\\n\" + choices[player_one] + \" beats \" + choices[player_two] + \". Player 1 wins!\")\n",
    "    \n",
    "    else:\n",
    "        print(\"\\n\" + choices[player_two] + \" beats \" + choices[player_one] + \". Player 2 wins!\")\n",
    "\n",
    "#updated for continued play\n",
    "\n",
    "    play_again = str(input(\"\\nDo you want to play another game? 1-Yes 2-No: \\n\"))\n",
    "\n",
    "    if play_again == \"1\":\n",
    "        game == True\n",
    "    else:\n",
    "        print(\"\\nGame Over. Thanks for playing!\")\n",
    "        break"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
