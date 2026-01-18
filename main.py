import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    consecutive_hits = 0
    lives = 3
    font = pygame.font.Font(None, 36)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()  
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    consecutive_hits += 1
                    multiplier = 1 + (consecutive_hits // 5)
                    points = 100 * multiplier
                    score += points
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                asteroid.kill()
                lives -= 1
                consecutive_hits = 0
                if lives <= 0:
                    print ("Game over!")
                    print (f"Final Score: {score}")
                    sys.exit()
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)

        multiplier = 1 + (consecutive_hits // 5)
        score_text = font.render(f"Score: {score}", True, "white")
        multiplier_text = font.render(f"Multiplier: {multiplier}x (Hits: {consecutive_hits})", True, "yellow")
        lives_text = font.render(f"Lives: {lives}", True, "red")
        screen.blit(score_text, (10, 10))
        screen.blit(multiplier_text, (10, 50))
        screen.blit(lives_text, (10, 90))
        
        pygame.display.flip()
        dt = clock.tick(60)/1000
       
if __name__ == "__main__":
    main()
