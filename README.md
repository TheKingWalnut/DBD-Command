# DBD-Command

Each command starts with !streak, but the next word depends on what you want to do. I am working on making it update stuff in a picture right now, but that'll take a while.
# MOD ONLY COMMANDS
!streak add {killer name} - Adds 1 to the passed in killer's streak. If that streak is now larger than the max streak, change max streak to that killer's streak. If the new killer streak is greater than that killer's old max streak, update the killer's max streak.
  
!streak set {killer name} {value} - Sets the given killer's streak to the given value.
  
!streak reset {killer name} - Sets the passed in killer's streak to zero.

# COMMANDS ANYONE CAN USE
!streak view {OPTIONAL: KILLER NAME}: Returns the max streak and who Adam was playing when he got that max streak. If a killer name is passed in, returns that killer's streak as well as their max streak and the overall max streak.
