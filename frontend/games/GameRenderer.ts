import { BaseGame } from './BaseGame'
import { SubwaySurfersGame } from './subway-surfers/SubwaySurfersGame'
import { SquidGameGame } from './squid-game/SquidGameGame'
import { MarioGame } from './mario/MarioGame'
import { PacManGame } from './pac-man/PacManGame'

/**
 * GameRenderer
 * Handles game initialization and rendering loop.
 * Currently uses Canvas 2D, but will be updated to use Three.js WebGLRenderer.
 * Games run in fullscreen mode when selected from the main menu.
 */
export class GameRenderer {
  private game: BaseGame | null = null
  private animationFrameId: number | null = null
  private lastTime: number = 0
  private resizeObserver: ResizeObserver | null = null

  constructor(
    private ctx: CanvasRenderingContext2D,
    private gameId: string
  ) {}

  init() {
    const canvas = this.ctx.canvas

    // Initialize game with fullscreen dimensions
    switch (this.gameId) {
      case 'subway-surfers':
        this.game = new SubwaySurfersGame(canvas.width, canvas.height)
        break
      case 'squid-game':
        this.game = new SquidGameGame(canvas.width, canvas.height)
        break
      case 'mario':
        this.game = new MarioGame(canvas.width, canvas.height)
        break
      case 'pac-man':
        this.game = new PacManGame(canvas.width, canvas.height)
        break
      default:
        console.error(`Unknown game: ${this.gameId}`)
        return
    }

    this.game.init()
    this.setupEventListeners()
    this.setupResizeObserver()
    this.gameLoop(0)
  }

  private setupEventListeners() {
    if (!this.game) return

    const handleKeyDown = (e: KeyboardEvent) => {
      // Don't capture ESC key - let it be handled by GameContainer for exit
      if (e.key === 'Escape') return
      this.game?.handleInput(e.key)
    }

    window.addEventListener('keydown', handleKeyDown)

    // Store cleanup function
    this.cleanup = () => {
      window.removeEventListener('keydown', handleKeyDown)
    }
  }

  private setupResizeObserver() {
    const canvas = this.ctx.canvas
    
    // Update game dimensions when canvas is resized (for fullscreen)
    const handleResize = () => {
      if (this.game) {
        // Note: For Three.js, we'll update the renderer size instead
        // This is a placeholder for canvas 2D
        const width = canvas.width
        const height = canvas.height
        // Game will handle resize in its update/render methods
      }
    }

    // Use ResizeObserver for better performance
    if (typeof ResizeObserver !== 'undefined') {
      this.resizeObserver = new ResizeObserver(handleResize)
      this.resizeObserver.observe(canvas)
    } else {
      window.addEventListener('resize', handleResize)
    }
  }

  private gameLoop = (currentTime: number) => {
    if (!this.game) return

    const deltaTime = currentTime - this.lastTime
    this.lastTime = currentTime

    // Update game state
    this.game.update(deltaTime)

    // Clear canvas
    this.ctx.fillStyle = '#000'
    this.ctx.fillRect(0, 0, this.ctx.canvas.width, this.ctx.canvas.height)

    // Render game
    this.game.render(this.ctx)

    this.animationFrameId = requestAnimationFrame(this.gameLoop)
  }

  cleanup() {
    if (this.animationFrameId !== null) {
      cancelAnimationFrame(this.animationFrameId)
    }
    if (this.resizeObserver) {
      this.resizeObserver.disconnect()
    }
    this.game?.cleanup()
  }
}

