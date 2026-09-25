import pygame
 
pygame.init()
 
screen = pygame.display.set_mode((300, 450))
pygame.display.set_caption("Traffic light simulators")
 
# Start the timer
start_time = pygame.time.get_ticks()
 
running = True
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # Work out how much time has passed
    elapsed = pygame.time.get_ticks() - start_time
 
    # Decide which light should be on
    if elapsed < 5000:
        light = "Red"
 
    elif elapsed < 7000:
        light = "Amber"
 
    elif elapsed < 10000:
        light = "Green"
 
    elif elapsed < 12000:
        light = "Amber"
 
    else:
        # Restart the sequence
        start_time = pygame.time.get_ticks()
 
    # Background
    screen.fill("black")
 
    # Draw the three lights
    pygame.draw.circle(screen, "grey20", (150, 75), 60)
    pygame.draw.circle(screen, "grey20", (150, 225), 60)
    pygame.draw.circle(screen, "grey20", (150, 375), 60)
 
    # Turn on the correct light
    if light == "Red":
        pygame.draw.circle(screen, "red", (150, 75), 60)
 
    elif light == "Amber":
        pygame.draw.circle(screen, "orange", (150, 225), 60)
 
    elif light == "Green":
        pygame.draw.circle(screen, "green", (150, 375), 60)
 
    pygame.display.flip()
 
pygame.quit()