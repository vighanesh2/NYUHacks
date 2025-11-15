# NYU Hacks Arcade

A collection of classic arcade games built with Next.js, TypeScript, and HTML5 Canvas.

## Games

- 🐍 **Snake** - Classic snake game
- 🏓 **Pong** - The original arcade classic
- 🧩 **Tetris** - Stack blocks and clear lines

## Project Structure

```
├── app/                    # Next.js App Router
│   ├── games/             # Game pages
│   ├── layout.tsx         # Root layout
│   └── page.tsx           # Home page
├── components/            # React components
│   ├── GameCard.tsx      # Game card component
│   └── GameContainer.tsx # Game canvas container
├── games/                 # Game implementations
│   ├── BaseGame.ts       # Base game class
│   ├── GameRenderer.ts   # Game renderer
│   ├── snake/            # Snake game
│   ├── pong/             # Pong game
│   └── tetris/           # Tetris game
├── lib/                   # Utilities
│   └── games.ts          # Game metadata
└── types/                 # TypeScript types
    └── game.ts            # Game type definitions
```

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Build

```bash
npm run build
npm start
```

## Tech Stack

- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **HTML5 Canvas** - Game rendering
- **Tailwind CSS** - Styling (via inline styles)

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

