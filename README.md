# NYU Hacks Arcade

A collection of classic arcade games built with Next.js, TypeScript, and Three.js for 3D graphics.

## Project Structure

This is a monorepo containing both frontend and backend code:

```
├── frontend/              # Next.js frontend application
│   ├── app/              # Next.js App Router
│   ├── components/       # React components
│   ├── games/            # Game implementations
│   │   ├── subway-surfers/  # Subway Surfers game + assets
│   │   ├── squid-game/      # Squid Game + assets
│   │   ├── mario/           # Mario game + assets
│   │   └── pac-man/         # Pac-Man game + assets
│   ├── lib/              # Utilities
│   └── types/            # TypeScript types
└── backend/              # Backend API and server
```

## Games

-  **Subway Surfers** - Endless runner - dodge obstacles and collect coins!
-  **Squid Game** - Survive the challenges inspired by the popular series!
- **Mario** - Classic platformer - jump, run, and collect coins!
- **Pac-Man** - Classic maze game - eat dots and avoid ghosts!

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Frontend Build

```bash
cd frontend
npm run build
npm start
```

### Backend Setup

Backend implementation coming soon. See `backend/README.md` for details.

## Tech Stack

- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **Three.js** - 3D graphics and game rendering
- **HTML5 Canvas** - Canvas rendering (for placeholders)

## Development Guidelines

### Adding a New Game

1. Create a new game class in `games/[game-name]/[GameName]Game.ts`
2. Extend the `BaseGame` class
3. Implement required methods: `init()`, `update()`, `render()`, `handleInput()`
4. Register the game in `games/GameRenderer.ts`
5. Add game metadata to `lib/games.ts`

### Game Architecture

Each game extends `BaseGame` which provides:
- Game state management
- Common game properties (score, level, lives, etc.)
- Abstract methods for game-specific logic

## License

MIT

