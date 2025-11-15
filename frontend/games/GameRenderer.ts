import { BaseGame } from './BaseGame'
import { SubwaySurfersGame } from './subway-surfers/SubwaySurfersGame'
import { SquidGameGame } from './squid-game/SquidGameGame'
import { MarioGame } from './mario/MarioGame'
import { PacManGame } from './pac-man/PacManGame'

export class GameRenderer {
  private game: BaseGame | null = null
  private animationFrameId: number | null = null
  private lastTime: number = 0

  constructor(
    private ctx: CanvasRenderingContext2D,
    private gameId: string
  ) {}

  init() {
    const canvas = this.ctx.canvas

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
    this.gameLoop(0)
  }

  private setupEventListeners() {
    if (!this.game) return

    const handleKeyDown = (e: KeyboardEvent) => {
      this.game?.handleInput(e.key)
    }

    window.addEventListener('keydown', handleKeyDown)

    // Store cleanup function
    this.cleanup = () => {
      window.removeEventListener('keydown', handleKeyDown)
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
    this.game?.cleanup()
  }
}

