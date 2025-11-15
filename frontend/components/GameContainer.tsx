'use client'

import { useEffect, useRef, useState } from 'react'
import { useRouter } from 'next/navigation'
import { GameRenderer } from '@/games/GameRenderer'

interface GameContainerProps {
  gameId: string
}

export function GameContainer({ gameId }: GameContainerProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const containerRef = useRef<HTMLDivElement>(null)
  const router = useRouter()
  const [showExitButton, setShowExitButton] = useState(true)

  useEffect(() => {
    if (!canvasRef.current || !containerRef.current) return

    const canvas = canvasRef.current
    const container = containerRef.current
    const ctx = canvas.getContext('2d')
    if (!ctx) return

    // Set canvas to fullscreen dimensions
    const resizeCanvas = () => {
      canvas.width = window.innerWidth
      canvas.height = window.innerHeight
    }

    resizeCanvas()
    window.addEventListener('resize', resizeCanvas)

    // Initialize game
    const gameRenderer = new GameRenderer(ctx, gameId)
    gameRenderer.init()

    // Handle ESC key to exit
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        router.push('/')
      }
    }

    window.addEventListener('keydown', handleKeyDown)

    // Auto-hide exit button after 3 seconds
    const hideTimer = setTimeout(() => {
      setShowExitButton(false)
    }, 3000)

    return () => {
      window.removeEventListener('resize', resizeCanvas)
      window.removeEventListener('keydown', handleKeyDown)
      clearTimeout(hideTimer)
      gameRenderer.cleanup()
    }
  }, [gameId, router])

  const handleExit = () => {
    router.push('/')
  }

  return (
    <div ref={containerRef} className="relative w-full h-full">
      <canvas
        ref={canvasRef}
        className="absolute inset-0 w-full h-full"
      />
      {showExitButton && (
        <button
          onClick={handleExit}
          className="absolute top-4 right-4 z-10 px-4 py-2 bg-black/70 hover:bg-black/90 text-white rounded-lg border border-white/20 transition-all duration-300 backdrop-blur-sm"
          onMouseEnter={() => setShowExitButton(true)}
        >
          <span className="mr-2">←</span>
          Exit Game (ESC)
        </button>
      )}
      <div
        className="absolute top-4 right-4 z-0 w-20 h-10"
        onMouseEnter={() => setShowExitButton(true)}
      />
    </div>
  )
}

