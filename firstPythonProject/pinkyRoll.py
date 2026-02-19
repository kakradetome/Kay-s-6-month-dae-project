# Print Welcome message!
print( "Welcome to our game" )

# Priming variable
userRollResponseInt = int( input( "Press 1 to roll the die: " ) )

while userRollResponseInt != 1:
    # Ask ther user to press 1 to roll a die
    userRollResponseInt = input( "Error: Press 1 to roll the die: " )

print( "You Rolled!!!" )
