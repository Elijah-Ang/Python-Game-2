import asyncio
import pygame

async def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("The Great Ledger")
    clock = pygame.time.Clock()
    
    font = pygame.font.SysFont("Arial", 24)
    text = font.render("The Great Ledger - WASM Build", True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 300))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)
        pygame.display.flip()
        
        await asyncio.sleep(0)  # Very important for Pygbag/WebAssembly!

if __name__ == "__main__":
    asyncio.run(main())
